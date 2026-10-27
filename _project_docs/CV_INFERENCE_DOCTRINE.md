# The corrected CV-comparison doctrine (2026-08-15)

An independent review found that the course's evaluation spine taught three
statements that are not true. They originate in `nb08` and propagate through
every notebook that compares models. This file is the single source of truth for
what replaces them. Apply it verbatim in spirit — the wording per notebook is
authored to fit that notebook's voice, but the *claims* below are fixed.

> **Amendment 1 (2026-10-26) — C2 and C3 rewritten.** The August verdict rule
> ("same sign on every fold and the mean clears the margin") is replaced by a
> fold-corrected paired interval read against ±margin, with four outcomes
> instead of three, and the parsimony rule is restated as a business policy.
> Rationale and the rollout list are in the "Amendment 1" section below. Any
> material that still reads a verdict from fold signs is pre-amendment.

## What was wrong

**W1 — "Student's *t* is the conservative choice because the folds are correlated."**
(`nb08` §1, and echoed wherever the CI formula is introduced.)
Student's *t* widens an interval to account for estimating the standard deviation
from few observations. It does nothing about dependence. Because the training
sets of adjacent folds overlap in `k-2` of their `k-1` parts, the fold scores are
positively correlated, and the usual `s/sqrt(k)` **understates** the true
variability. The naive interval is therefore optimistic — too narrow — and *t*
does not repair that. Bengio and Grandvalet (JMLR 2004) show there is no unbiased
estimator of the variance of k-fold CV.

**W2 — "If the two 95% CIs overlap, the models are statistically indistinguishable."**
(`nb08` §Exercise 1, and the decision rule repeated in nb09, nb11-nb14, nb16, nb18.)
Comparing two *marginal* intervals is not a test of the difference between them.
Non-overlap does imply a difference at the stated level, but overlap does **not**
imply the absence of one — two intervals can overlap substantially while the
paired difference is consistently one-signed. Schenker and Gentleman (*The
American Statistician*, 2001) is the standard reference.

**W3 — "A test score INSIDE the CV interval confirms the model generalises."**
(`nb14` ceremony, and the INSIDE/ABOVE/BELOW verdict wherever it appears.)
An interval around a *mean of fold scores* is not a prediction interval for a
*different* statistic computed on a *different* sample. A single test score
landing inside it is weak evidence at best, and the interval was already too
narrow by W1.

## What we teach instead

**C1 — Report the fold spread honestly, and name it descriptively.**
Keep `mean ± t_crit * s / sqrt(k)`. Keep calling the arithmetic what it is. But
label it a **descriptive interval** or **approximate 95% interval**, and state
once per notebook that it is optimistic because folds share training data. The
number is still the right thing to report; the certainty claim is what changes.
Never call it "the 95% confidence interval for the model's true performance".

**C2 — Compare models on paired per-fold differences, judged by a fold-corrected interval.** *(Amendment 1)*
Score both candidates on the **identical** folds (same splitter object, same
seed). For each fold compute `d_i = score_complex(i) - score_baseline(i)`,
signed so that a positive value favours the more complex model. For a
lower-is-better metric (MAE, RMSE) that means `d_i = error_baseline(i) -
error_complex(i)`; with scikit-learn's `neg_` scorers the plain subtraction
already has the right sign. Subtracting per fold before summarising removes the
fold-to-fold variation both models share, which is exactly the noise that made
the marginal intervals look wide.

Report the mean difference with the **corrected paired interval**:

```
mean(d) ± t(0.975, k-1) * sd(d) * sqrt(1/k + 1/(k-1))
```

The `1/(k-1)` term is the Nadeau–Bengio correction for the training rows the
folds share: it is the held-out size over the training size inside the CV, which
is `1/(k-1)` for one run of k-fold. Its k-fold use is Bouckaert and Frank's
(2004), and it is the correction in scikit-learn's own model-comparison example.
It widens the naive paired interval by a factor of 1.50 at k = 5 and 1.45 at
k = 10; the half-width is 1.86 × sd(d) at k = 5 and 1.04 × sd(d) at k = 10. For
r repeats of k-fold, replace `1/k` with `1/(r*k)` and use `r*k - 1` degrees of
freedom.

Label it an **approximate 95% interval, corrected for fold overlap**. The
correction is a heuristic that improves calibration without guaranteeing it
(pairing alone does not: Dietterich, 1998, found the ordinary 10-fold paired
*t*-test rejects too often), so it is still never "the" 95% confidence interval.
It is the instrument the C3 verdict is read from.

**Fold signs are a description, never the verdict.** "The forest won 5 of 5
folds" is worth reporting, but with five folds every difference shares a sign
1 time in 16 when there is no real difference and the folds are independent,
and roughly 1 time in 6.5 when the differences are correlated at 0.2
(simulation, equicorrelated normal). In the other direction, one near-zero fold
of the wrong sign can sit beside a clear win (see the worked examples under C3).

**C3 — Predeclare a margin, read one of four outcomes, and state parsimony as a policy.** *(Amendment 1)*
Before comparing, write down the margin δ: the smallest gain that would change
the business decision — 0.01 ROC-AUC, $2,000 of MAE, whatever the stakeholder's
problem implies. Then read the corrected interval `[L, U]` against `±δ`:

| Outcome | Condition | What to say |
|---|---|---|
| 1. **Worthwhile gain** | `L > δ` | The complex model is better by more than the margin. Adopt it. |
| 2. **Worthwhile loss** | `U < -δ` | The baseline is better by more than the margin. Keep the baseline. |
| 3. **Practically equivalent** | `-δ < L` and `U < δ` | Any difference is smaller than the margin. The simpler model wins on parsimony. |
| 4. **Unresolved** | anything else | The data cannot tell whether the gap is worth having. Keep the simpler model as a stated policy, and say so. |

**Parsimony is a business policy, not a statistical finding.** The more complex
model carries the burden of proof: it is adopted only in outcome 1. In outcomes
2–4 the simpler, cheaper, more interpretable model stays — but only outcome 3
earns the words "practically equivalent", because only there does the interval
rule out a gain as large as the margin (the equivalence-testing logic of Lakens,
2017; the ROPE of Benavoli et al., 2017). In outcome 4 the honest sentence is
"the evidence does not show a gain large enough to justify the extra complexity,
so under our policy we keep the simpler model" — never "the models are
equivalent" and never "there is no difference". A stakeholder who wants to bet
on an unresolved gain may override the policy; that is their call, made
explicitly and on the record.

**The one lower bound that gates a decision** is `L`, the lower limit of the
*paired difference*, against the margin (outcome 1). Ranking two models by the
lower limits of their *own* CV intervals stays retired: it can pick the model
that loses every fold (Amendment 1 section).

**Worked examples** — margin 0.01 ROC-AUC, differences are complex minus
baseline, k = 5 unless stated. Every number below was computed (A1).

| Case | Per-fold differences | Mean | Corrected interval | Amended verdict | August sign rule said |
|---|---|---|---|---|---|
| Clear gain | .030 .025 .035 .028 .032 | .0300 | (.0229, .0371) | 1. worthwhile gain | real difference |
| Tiny, mixed signs | .002 −.001 .001 .003 .000 | .0010 | (−.0019, .0039) | 3. practically equivalent | inconclusive |
| Small, all positive | .001 .001 .001 .001 .010 | .0028 | (−.0047, .0103) | 4. unresolved | practically equivalent |
| Large, one tiny negative (k = 10) | −.001, then nine of .030 | .0269 | (.0167, .0371) | 1. worthwhile gain | inconclusive |
| Clear loss | −.030 −.025 −.035 −.028 −.032 | −.0300 | (−.0371, −.0229) | 2. worthwhile loss | real difference (baseline) |

**Reference implementation** (instructor-facing; notebooks adopt it per A4):

```python
import numpy as np
from scipy import stats

def paired_verdict(scores_complex, scores_baseline, margin, higher_is_better=True):
    """Fold scores from the SAME cv object for both models, in fold order."""
    a = np.asarray(scores_complex, dtype=float)
    b = np.asarray(scores_baseline, dtype=float)
    d = a - b if higher_is_better else b - a      # positive favours the complex model
    k = d.size
    half = stats.t.ppf(0.975, k - 1) * d.std(ddof=1) * np.sqrt(1 / k + 1 / (k - 1))
    low, high = d.mean() - half, d.mean() + half
    if low > margin:
        verdict = "worthwhile gain: adopt the complex model"
    elif high < -margin:
        verdict = "worthwhile loss: keep the baseline"
    elif -margin < low and high < margin:
        verdict = "practically equivalent: the simpler model wins"
    else:
        verdict = "unresolved: keep the simpler model as a stated policy"
    return d, d.mean(), (low, high), verdict
```

Pair it with one splitter object passed to both `cross_val_score` calls, e.g.
`cv = StratifiedKFold(5, shuffle=True, random_state=RANDOM_SEED)`, so fold `i`
holds the same rows for both models. When scoring with `neg_mean_absolute_error`,
keep `higher_is_better=True`.

**C4 — The test-set ceremony compares against the predeclared tolerance, not the CV interval.**
Open the locked test set once, report the score, and judge it against the
business tolerance agreed in C3 — plus the CV mean as a rough expectation, stated
as such. Keep the INSIDE / ABOVE / BELOW vocabulary if it is useful as a shorthand
for "close to what CV suggested / better / worse", but it is a **sanity check and
a description**, never a statistical proof of generalisation and never a
deployment gate on its own.

## Where this was applied — status 2026-08-17

**Notebooks — DONE** (instructor copy first via `scripts/apply_instructor_first.py`,
then the student copy; every numeric claim re-executed before commit):

| Notebook | Edits | Note |
|---|---:|---|
| `nb02` | 2 | exercise comparison gains the predeclared-margin step |
| `nb08` | 62 | the origin; six instructor solution cells rewritten to print paired verdicts |
| `nb09` | 72 | objectives, workflow slogan, `cv_results_` reading, both plan bullets, Q&A |
| `nb11` | 29 | margins predeclared upstream; three-panel comparison figure |
| `nb12` | 64 | verdicts re-grounded; stale section pointer and depth-gap figure fixed |
| `nb13` | 67 | |
| `nb14` | 118 | the ceremony: CI-overlap tie, CV-CI-lower-bound "dominance tiebreaker", interval-as-gate, and the monitoring trigger all replaced |
| `nb16` | 60 | retrain trigger now judges the deployment tolerance |
| `nb18` | 42 | |

`nb06` needed no CV edits (it predates the nb08 spine) — but a **separate**
positive-class defect was found and fixed there and in `nb07`; see the commit
`Correct inverted positive-class reasoning in nb06/nb07`.

**Quiz banks — DONE.** 69 edits across 17 of 20 flagged banks; 3 banks were
keyword false positives. All 48 banks still PASS
`scripts/audit_answer_length.py`, and zero stems or keyed options assert the
retired rule.

**Midterm — DONE.** The 2026F banks were rebuilt to the doctrine (see
`_midterm_exam/2026F/README.md`).

**Video guides and Brightspace pages — DONE.** 159 edits across 12 files plus a
final pass over `nb08`/`nb09`/`nb13`/`nb14` guides and the `13`/`14` pages.
`scripts/voice_check_guides.py` clean on every touched guide.

**Records — DONE.** `CLAUDE.md` (CV-first rule + comparison pattern),
`_project_docs/DECISIONS.md` Decision 14. Decision 9 (test-set lock) stands
unchanged, and `scripts/audit_cv_first.py` still reports only the authorized
`nb14` cells 30/34 and the `nb18` Kaggle demo.

Locate any future instance by its **wording**, not by cell index — indices move.

## Amendment 1 — 2026-10-26: C2/C3 rewritten

**Why.** A question about using a model's CV-interval lower bound as a
tiebreaker led to a literature check (Claude and a Codex partner run working
independently, every source and number re-verified; artifacts in
`_adm/codex_collab/2026-10-26_cv-lower-bound-tiebreaker/`). It confirmed the
August retirements (W1–W3 and the lower-bound tiebreaker) and found two
weaknesses in the August replacement itself:

1. **The sign rule was weak evidence.** "Same sign on every fold" happens by
   chance 1 time in 16 at k = 5 with independent folds, and about 1 in 6.5 with
   the positive correlation CV folds have. It also misfires the other way: one
   near-zero fold of the wrong sign turned a clear win into "inconclusive".
2. **"Under the margin" was read as "practically equivalent".** Falling short
   of the margin is absence of evidence, not evidence of equivalence: in the
   "small, all positive" example the interval still reaches .0103, past the
   .01 margin. Equivalence needs the interval inside ±margin (Lakens, 2017).

**What survives unchanged:** identical folds, per-fold paired differences, a
margin declared before the results, the parsimony default, C1, C4, and the
retirement of the lower-bound tiebreaker. On that last point, the check added
a concrete failure: with fold AUCs A = .841 .848 .856 .872 .883 and
B = .840 .846 .850 .854 .860, A wins every fold and has the higher mean
(.860 vs .850), yet B has the higher lower limit (.8405 vs .8385), so the
tiebreaker picks B. Picking a pessimistic bound is a legitimate idea in other
settings (e.g. Thomas et al., 2015; Maurer & Pontil, 2009), but there the
bounds carry real guarantees and are compared with a fixed threshold — which
is what outcome 1 of the amended C3 does with the paired difference.

**Rollout.** Instructor copy first (A6); prose and code move together (A4).

| Surface | What changes | Status |
|---|---|---|
| This file | C2, C3, A2, A5 rewritten | DONE 2026-10-26 |
| `CLAUDE.md` CV-first bullet | "its three outcomes" becomes "its four outcomes" | DONE 2026-10-26 |
| `_project_docs/DECISIONS.md` Decision 14 | Addendum recording Amendment 1 | DONE 2026-10-26 |
| Poster rubric criterion 6 (docx/xlsx/pdf), M10 instructions | Exemplary/Competent wording; a Fall 2026 transition clause accepts the August three-outcome verdict for full credit; announcement drafted in `_announcements/2026F/` | DONE 2026-10-26 |
| `nb08` (origin), `nb09`, `nb11`–`nb14`, `nb16`, `nb18` | Verdict cells and solution code: corrected interval, four outcomes, fold signs as description. **nb14's verdicts will change:** a 2026-10-26 re-run of its regression case found the shipped finalists *unresolved* under the amended rule, where the August rule called a real difference — re-execute before editing (A1) | PENDING |
| `nb17` | Check the 2026-10-26 doctrine sweep for three-outcome wording | PENDING |
| Quiz banks and midterm banks | Any item keyed on the sign rule or on "under the margin = equivalent"; re-run `audit_answer_length.py` | PENDING |
| Video guides and Brightspace pages | Same wording sweep; `voice_check_guides.py` | PENDING |

## References

- Bengio, Y., & Grandvalet, Y. (2004). No unbiased estimator of the variance of
  k-fold cross-validation. *JMLR* 5. https://www.jmlr.org/papers/v5/grandvalet04a.html
- Nadeau, C., & Bengio, Y. (2003). Inference for the generalization error.
  *Machine Learning* 52.
- Schenker, N., & Gentleman, J. F. (2001). On judging the significance of
  differences by examining the overlap between confidence intervals.
  *The American Statistician* 55(3). https://doi.org/10.1198/000313001317097960

Added with Amendment 1:

- Bouckaert, R. R., & Frank, E. (2004). Evaluating the replicability of
  significance tests for comparing learning algorithms. *PAKDD 2004*, 3–12.
  https://doi.org/10.1007/978-3-540-24775-3_3
- Dietterich, T. G. (1998). Approximate statistical tests for comparing
  supervised classification learning algorithms. *Neural Computation* 10(7),
  1895–1923. https://doi.org/10.1162/089976698300017197
- Lakens, D. (2017). Equivalence tests: A practical primer for t tests,
  correlations, and meta-analyses. *Social Psychological and Personality
  Science* 8(4), 355–362. https://doi.org/10.1177/1948550617697177
- Benavoli, A., Corani, G., Demšar, J., & Zaffalon, M. (2017). Time for a
  change: A tutorial for comparing multiple classifiers through Bayesian
  analysis. *JMLR* 18(77). https://www.jmlr.org/papers/v18/16-305.html
- Bates, S., Hastie, T., & Tibshirani, R. (2024). Cross-validation: What does
  it estimate and how well does it do it? *JASA* 119(546), 1434–1445.
  https://doi.org/10.1080/01621459.2023.2197686
- Thomas, P. S., Theocharous, G., & Ghavamzadeh, M. (2015). High confidence
  policy improvement. *ICML*, PMLR 37, 2380–2388.
  https://proceedings.mlr.press/v37/thomas15.html
- Maurer, A., & Pontil, M. (2009). Empirical Bernstein bounds and sample
  variance penalization. *COLT*. https://arxiv.org/abs/0907.3740
- scikit-learn. Statistical comparison of models using grid search (corrected
  paired t-test and Bayesian ROPE).
  https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html

---

## Authoring rules for anyone applying this correction

A first pass at rewriting the notebooks produced 294 edits, and verification — which *executed* the
notebooks rather than only reading them — rejected a large fraction. Every rejection fell into one of
five patterns. Do not repeat them.

**A1 — Never assert a number you have not computed.** The failed pass wrote sentences like "the
paired fold differences never favour the forest" and "the random forest gives back about 0.007
ROC-AUC". Both were false against the notebook's own output. If a replacement needs a specific
figure, run the cell and read it; if you cannot run it, write the sentence so it does not depend on
the figure ("whether the differences all point the same way is the thing to check in the output
below"). Qualitative and correct beats quantitative and wrong.

**A2 — Keep the four outcomes distinct.** *(Amendment 1)* C3 has four, all read
from the corrected paired interval `[L, U]` against `±δ`:
*`L > δ`* = worthwhile gain, adopt the complex model;
*`U < -δ`* = worthwhile loss, keep the baseline;
*interval inside `±δ`* = practically equivalent, the simpler model wins;
*anything else* = unresolved, the simpler model stays as a stated policy.
Collapsing "unresolved" into "practically equivalent" rebuilds W2 in new words,
and reading any verdict from fold signs alone rebuilds the August sign rule.
(Before Amendment 1 this rule listed three sign-based outcomes; material still
stating them is pre-amendment.)

**A3 — Declare the margin before the results, once, in one form.** The failed pass routed decisions
through a "business tolerance" that appeared nowhere in the notebook, and stated the rule in three
incompatible ways across cells. Pick one wording, introduce the margin *before* the first comparison
that uses it, and use that same wording everywhere.

**A4 — Prose and code must move together.** The notebooks keep only means and CI half-widths; the
per-fold arrays are discarded. A rule the student cannot execute from any cell's output is not a
rule, it is a slogan. Any notebook whose prose adopts the paired comparison must also expose the
fold arrays and compute the differences — that is a code edit, not only a markdown edit.

**A5 — Sweep the whole notebook, not the mapped cells.** W2 survived in Gemini verify checklists,
wrap-up bullets, and monitoring cards the map did not list, one cell away from an edited paragraph.
Search for the *wording* — overlap, statistically tied, indistinguishable, INSIDE, a model's own CI
lower bound as a gate or tiebreaker — and fix every instance or none. After Amendment 1, also search
for sign-rule verdicts: "every fold", "same sign", "signs flip", "change sign", "under the margin".
(The lower limit of the *paired difference* against the margin is the sanctioned gate, C3 outcome 1.)

**A6 — Instructor copy first.** Per `CLAUDE.md`, the instructor notebook is the source of truth. Use
`scripts/apply_instructor_first.py`, which applies each edit to `*_instructor.ipynb` and refuses the
edit outright if the text is not found there. Instructor solution cells also *print* verdicts
("CIs OVERLAP — not statistically significant"); those need the same correction as the prose.
