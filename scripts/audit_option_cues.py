# -*- coding: utf-8 -*-
"""Detect surface and stylistic cues that let a student pick the keyed option
without knowing the material.

`audit_answer_length.py` measures ONE channel: option length in characters. This
gate measures the channels it cannot see. Run both; neither replaces the other.

WHY THIS EXISTS, AND WHY VERSION 1 WAS NOT ENOUGH
-------------------------------------------------
v1 (2026-08-21) tested a hand-picked list of punctuation markers and found the
Fall 2026 midterm exploitable at 59.6% via "pick the option with a semicolon".
Those markers were scrubbed. v1 then reported 22.4% and looked clean.

An independent review (Codex, gpt-5.6-sol, 2026-08-24) showed that was an
artifact of v1's own blind spots, and re-measuring confirmed it:

  - "pick the option with the most COMMAS" scores 43.7% (it scored 34.5% BEFORE
    the scrub, so the scrub made it worse: semicolons became commas).
  - "AVOID options containing ' because '" scores 35.4%. v1 only ever tested
    picking a marked option, never avoiding one, so elimination cues were
    invisible.
  - A leave-one-form-out TF-IDF model trained on option text alone predicts the
    held-out form's keys at 88.6%. The keys share a writing register.
  - v1's MIN_APPLICABLE=15 floor hid a marker that was 3-for-3 keyed, i.e. three
    deterministic free answers.
  - v1's binomial test was misspecified: it passed a FRACTIONAL tie-credit score
    through math.ceil and compared it to Binomial(n, 0.2), which is not the null
    distribution of that statistic.

v2 fixes all five. The null is now a within-item permutation of which option is
keyed, which is exactly right for fractional tie credit and needs no closed form.

Usage:
    python3 scripts/audit_option_cues.py --bank _midterm_exam/2026F/banks
    python3 scripts/audit_option_cues.py --file <d2l.csv>
    python3 scripts/audit_option_cues.py --bank <dir> --style      # + learned-style probe
    python3 scripts/audit_option_cues.py --bank <dir> --json

Exit status is 1 if any attack clears the risk limit, so it can gate a build.
"""
import argparse
import csv
import glob
import io
import json
import os
import random
import re
import sys
from collections import Counter

# ---- risk limits ---------------------------------------------------------
N_PERM = 20000         # replicates; must be >> family size so p can clear Holm
ALPHA = 0.01           # family-wise, via Holm
MAX_ADVANTAGE = 0.08   # an attack may not beat chance by more than 8 points
DETERMINISTIC_N = 2    # a cue keyed every time it appears, this often, always fails
MIN_APPL_FAIL = 20     # below this, an attack is too rare to be a reliable strategy
SEED = 474


# ---- attack library ------------------------------------------------------
# Binary predicates. Each is tested BOTH ways: pick-marked and avoid-marked.
MARKERS = {
    "semicolon":     lambda t: ";" in t,
    "em/en dash":    lambda t: "—" in t or "–" in t,
    "colon":         lambda t: re.search(r":(?!\d)", t) is not None,
    "parenthetical": lambda t: "(" in t,
    "' because '":   lambda t: " because " in t,
    "', so '":       lambda t: ", so " in t,
    "' and '":       lambda t: " and " in t,
    "' which '":     lambda t: " which " in t,
    "absolute word": lambda t: bool(re.search(r"\b(always|never|all|none|guaranteed|any|every|only)\b", t, re.I)),
    "hedge word":    lambda t: bool(re.search(r"\b(usually|typically|generally|often|may|can|might)\b", t, re.I)),
    "has digit":     lambda t: bool(re.search(r"\d", t)),
}

VOCAB = ["concern", "should", "must", "cannot", "reject", "approve", "refuse",
         "instead", "risk", "wrong", "correct", "leak", "leakage", "baseline",
         "because", "however", "since"]

_words = lambda s: set(re.findall(r"[a-z]{4,}", s.lower()))

# Graded features. Each is tested BOTH ways: argmax and argmin.
GRADED = {
    "length (chars)":   lambda t, s: len(t),
    "word count":       lambda t, s: len(t.split()),
    "comma count":      lambda t, s: t.count(","),
    "sentence count":   lambda t, s: t.count("."),
    "clause count":     lambda t, s: t.count(",") + t.count(".") + t.count(";"),
    "stem overlap":     lambda t, s: len(_words(t) & _words(s)),
    "overlap density":  lambda t, s: len(_words(t) & _words(s)) / max(len(_words(t)), 1),
    "long-word count":  lambda t, s: sum(1 for w in t.split() if len(w) > 8),
    "digit count":      lambda t, s: len(re.findall(r"\d", t)),
    "mean word length": lambda t, s: sum(len(w) for w in t.split()) / max(len(t.split()), 1),
}


def cands_marker(items, pred, avoid):
    """Precompute the candidate set an attack would choose, per item.
    Computed ONCE; the permutation null then only reassigns which option is keyed,
    so the expensive text work never runs inside the replicate loop."""
    out = []
    for opts, _, _ in items:
        marked = {i for i, t in enumerate(opts) if pred(t)}
        cand = (set(range(len(opts))) - marked) if avoid else marked
        out.append(cand if cand and len(cand) != len(opts) else None)
    return out


def cands_graded(items, fn, want_max):
    out = []
    for opts, _, stem in items:
        vals = [fn(t, stem) for t in opts]
        target = max(vals) if want_max else min(vals)
        cand = {i for i, v in enumerate(vals) if v == target}
        # A full tie stays in, with fractional (random-fallback) credit. Dropping it as None
        # while keeping it in the denominator scored 30 perfect picks + 180 ties as 14.3%
        # instead of 35.7% (Codex review, 2026-10-07).
        out.append(cand)
    return out


_tok3 = lambda s: set(re.findall(r"[a-z]{3,}", s.lower()))


def jaccard(a, b):
    return len(a & b) / len(a | b) if (a or b) else 0.0


def convergence_sums(opts):
    """Per option: summed Jaccard similarity (3+-letter tokens) with the other options."""
    toks = [_tok3(t) for t in opts]
    return [sum(jaccard(toks[i], toks[j]) for j in range(len(opts)) if j != i)
            for i in range(len(opts))]


def cands_middle(items, fn):
    """Avoid-the-extremes attack: pick among the options that are neither the max nor the
    min of a graded feature. Fixing "the key is the longest / the most convergent" by pushing
    keys to the middle creates exactly this cue (pick-the-middle by convergence scored 40.7%
    after the first convergence repair, 2026-10-12). A full tie keeps every option."""
    out = []
    for opts, _, stem in items:
        vals = [round(fn(t, stem), 9) if fn is not None else None for t in opts]
        mx, mn = max(vals), min(vals)
        cand = {i for i, v in enumerate(vals) if v != mx and v != mn}
        out.append(cand or set(range(len(opts))))
    return out


def cands_middle_convergence(items):
    out = []
    for opts, _, _ in items:
        vals = [round(v, 9) for v in convergence_sums(opts)]
        mx, mn = max(vals), min(vals)
        cand = {i for i, v in enumerate(vals) if v != mx and v != mn}
        out.append(cand or set(range(len(opts))))
    return out


def cands_convergence(items, want_max):
    """Option-to-option convergence (NBME 'convergence' flaw): the key collects the
    components repeated across distractors, so it overlaps most with the others. Uses no
    stem, no labels, no model. Added after the Codex review of 2026-10-07 found it at 47.9%."""
    out = []
    for opts, _, _ in items:
        vals = [round(v, 9) for v in convergence_sums(opts)]
        target = max(vals) if want_max else min(vals)
        out.append({i for i, v in enumerate(vals) if v == target})
    return out


def score_from_cands(cands, keys, applicable_only):
    """applicable_only=True  -> rate over items where the attack discriminates
       applicable_only=False -> rate over all items (graded attacks always apply)"""
    hit = appl = 0.0
    for c, k in zip(cands, keys):
        if c is None:
            continue
        appl += 1
        if k in c:
            hit += 1.0 / len(c)
    denom = appl if applicable_only else len(keys)
    return (hit / denom if denom else 0.0), int(appl)


def permutation_p(cands, keys, observed, applicable_only, sizes, rng):
    """Null: within each item the key is equally likely to be any option."""
    ge = 0
    for _ in range(N_PERM):
        perm = [rng.randrange(s) for s in sizes]
        r, _ = score_from_cands(cands, perm, applicable_only)
        if r >= observed - 1e-12:
            ge += 1
    return (ge + 1) / (N_PERM + 1)


def holm(pvals, alpha):
    """Return the set of indices rejected by Holm-Bonferroni."""
    order = sorted(range(len(pvals)), key=lambda i: pvals[i])
    rejected, m = set(), len(pvals)
    for rank, i in enumerate(order):
        if pvals[i] <= alpha / (m - rank):
            rejected.add(i)
        else:
            break
    return rejected


def load_banks(d):
    forms = []
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        b = json.load(io.open(f, encoding="utf-8"))
        forms.append((b["case_key"],
                      [(q["options"], q["correct_index"], q.get("stem", ""))
                       for q in b["questions"]]))
    return forms


def load_csv(path):
    qs, cur = [], None
    for row in csv.reader(io.open(path, encoding="utf-8")):
        if not row or not row[0]:
            continue
        if row[0] == "NewQuestion":
            if cur:
                qs.append(cur)
            cur = {"opts": [], "keys": [], "stem": ""}
        elif row[0] == "QuestionText" and cur is not None:
            cur["stem"] = row[1]
        elif row[0] == "Option" and cur is not None:
            if row[1].strip() == "100.00":
                cur["keys"].append(len(cur["opts"]))
            cur["opts"].append(row[2])
    if cur:
        qs.append(cur)
    bad = [i for i, q in enumerate(qs, 1) if len(q["keys"]) != 1]
    if bad:
        sys.exit(f"{path}: questions with != 1 keyed option: {bad}")
    return [(os.path.basename(path),
             [(q["opts"], q["keys"][0], q["stem"]) for q in qs])]


def style_probe(forms):
    """Leave-one-form-out learned-style attack. The omnibus detector: it catches
    register differences no hand-written predicate anticipates."""
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
    except ImportError:
        return None, "sklearn not installed (try /usr/local/bin/python3)"
    if len(forms) < 3:
        return None, "needs >= 3 forms"
    hit = tot = 0
    per = []
    rank_hits = {}
    for held, _ in forms:
        X, y = [], []
        for name, items in forms:
            if name == held:
                continue
            for opts, key, _ in items:
                for i, t in enumerate(opts):
                    X.append(t)
                    y.append(1 if i == key else 0)
        vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)
        A = vec.fit_transform(X)
        clf = LogisticRegression(max_iter=2000, class_weight="balanced").fit(A, y)
        items = dict(forms)[held]
        h = 0
        for opts, key, _ in items:
            scores = clf.decision_function(vec.transform(opts))
            order = sorted(range(len(opts)), key=lambda i: -scores[i])
            r = order.index(key)            # 0 = the model's top pick
            rank_hits[r] = rank_hits.get(r, 0) + 1
            h += (r == 0)
        per.append((held, h, len(items)))
        hit += h
        tot += len(items)
    ranks = {r + 1: rank_hits.get(r, 0) / tot for r in range(max(len(o) for _, its in forms for o, _, _ in its))}
    return (hit / tot, per, ranks), None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank")
    ap.add_argument("--file")
    ap.add_argument("--style", action="store_true", help="run the learned-style probe")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()
    if not (args.bank or args.file):
        sys.exit("need --bank <dir> or --file <csv>")

    rng = random.Random(SEED)
    forms = load_banks(args.bank) if args.bank else load_csv(args.file)
    items = [it for _, its in forms for it in its]
    if not items:
        sys.exit("no questions found")
    n_opts = Counter(len(o) for o, _, _ in items)
    chance = sum((1 / k) * c for k, c in n_opts.items()) / len(items)

    attacks = []   # (name, observed_rate, applicable, p, deterministic_n)
    keys = [k for _, k, _ in items]
    sizes = [len(o) for o, _, _ in items]

    def run(label, cands, applicable_only, det=0):
        rate, appl = score_from_cands(cands, keys, applicable_only)
        if appl == 0:
            return
        p = permutation_p(cands, keys, rate, applicable_only, sizes, rng)
        attacks.append((label, rate, appl, p, det))

    for name, pred in MARKERS.items():
        for avoid in (False, True):
            c = cands_marker(items, pred, avoid)
            det = 0
            if not avoid:
                det = sum(1 for cc, k in zip(c, keys) if cc == {k})
            run(f"{'avoid' if avoid else 'pick '} {name}", c, True, det)

    for term in VOCAB:
        pred = (lambda t, w=term: re.search(rf"\b{re.escape(w)}\b", t, re.I) is not None)
        for avoid in (False, True):
            run(f"{'avoid' if avoid else 'pick '} '{term}'",
                cands_marker(items, pred, avoid), True)

    for name, fn in GRADED.items():
        for want_max in (True, False):
            run(f"{'most ' if want_max else 'fewest'} {name}",
                cands_graded(items, fn, want_max), False)

    for want_max in (True, False):
        run(f"{'most ' if want_max else 'fewest'} option convergence",
            cands_convergence(items, want_max), False)
    run("middle option convergence", cands_middle_convergence(items), False)
    for name, fn in GRADED.items():
        run(f"middle {name}", cands_middle(items, fn), False)

    pvals = [a[3] for a in attacks]
    sig = holm(pvals, ALPHA)

    # Effect size is the operative limit, not significance. An attack beating
    # chance by 20+ points over 200 items is an exam-security fact regardless of
    # where a multiplicity-corrected threshold happens to fall; Holm is reported
    # as supporting evidence, not as the gate.
    failures = []
    for i, (label, rate, appl, p, det) in enumerate(attacks):
        adv = rate - chance
        if det >= DETERMINISTIC_N and rate > 0.999:
            failures.append(f"{label}: keyed on ALL {det} items where it applies "
                            f"(deterministic free answers)")
        elif adv > MAX_ADVANTAGE and appl >= MIN_APPL_FAIL and p < ALPHA:
            holm_note = "Holm-significant" if i in sig else f"p={p:.2g} unadjusted"
            failures.append(f"{label}: {100*rate:.1f}% on {appl} items, "
                            f"{100*adv:+.1f} pts over chance ({holm_note})")

    style = None
    style_error = None
    if args.style:
        style, style_error = style_probe(forms)
        if style_error:
            # A requested check that cannot run is a failure, not a silent pass.
            failures.append(f"learned style probe unavailable: {style_error}")
        elif style:
            rate, per, ranks = style
            # Every rank is an attack: "pick the model's second choice" is as usable as its
            # first (Codex 2026-10-07: rank 2 held 35.2% of keys when rank 1 held 21.4%).
            for r, rr in ranks.items():
                if rr - chance > MAX_ADVANTAGE:
                    failures.append(f"learned style probe, rank {r}: key at the model's rank-{r} "
                                    f"option {100*rr:.1f}% ({100*(rr-chance):+.1f} pts over chance)")

    if args.as_json:
        print(json.dumps({
            "chance": chance, "items": len(items), "forms": len(forms),
            "attacks": [{"attack": l, "rate": r, "applicable": a, "p": p,
                         "deterministic_n": d, "holm_significant": i in sig}
                        for i, (l, r, a, p, d) in enumerate(attacks)],
            "style": None if not style else {"rate": style[0], "per_form": style[1], "rank_rates": style[2]},
            "style_error": style_error,
            "failures": failures, "pass": not failures}, indent=1))
        sys.exit(0 if not failures else 1)

    print(f"items: {len(items)}   forms: {len(forms)}   options/item: {dict(n_opts)}   "
          f"chance: {100*chance:.1f}%")
    print(f"null: {N_PERM} within-item key permutations   family: Holm at alpha={ALPHA}   "
          f"risk limit: {100*MAX_ADVANTAGE:.0f} pts over chance on >={MIN_APPL_FAIL} items\n")
    print(f"  {'attack':<26}{'rate':>8}{'appl.':>7}{'adv':>8}{'p':>10}  verdict")
    for i, (label, rate, appl, p, det) in enumerate(sorted(
            attacks, key=lambda a: -a[1])[:22]):
        j = attacks.index((label, rate, appl, p, det))
        bad = (det >= DETERMINISTIC_N and rate > 0.999) or \
              (rate - chance > MAX_ADVANTAGE and appl >= MIN_APPL_FAIL and p < ALPHA)
        print(f"  {label:<26}{100*rate:7.1f}%{appl:>7}{100*(rate-chance):+7.1f}{p:>10.4f}"
              f"  {'FAIL' if bad else 'ok'}")

    if style_error:
        print(f"\nLEARNED STYLE PROBE UNAVAILABLE: {style_error}")
    if style:
        rate, per, ranks = style
        print(f"\nLEARNED STYLE PROBE (leave-one-form-out, option text only)")
        print("  key rank under the model: " + "  ".join(f"rank {r}: {100*v:.1f}%" for r, v in ranks.items()))
        for c, h, n in sorted(per, key=lambda r: -r[1]):
            print(f"  {c:<14}{h:>3}/{n}  {100*h/n:5.1f}%")
        print(f"  {'POOLED':<14}{100*rate:>8.1f}%   (chance {100*chance:.1f}%)")

    print()
    if failures:
        print(f"FAIL — {len(failures)} attack(s) over the risk limit:")
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("PASS — no attack in the library clears the risk limit")


if __name__ == "__main__":
    main()
