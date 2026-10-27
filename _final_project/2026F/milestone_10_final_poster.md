# Milestone 10 — Final Poster Submission

## About the Final Project

The Final Project is a **group capstone** (groups of four, randomly assigned) culminating in a **research poster** and a post-conference **Poster-to-Product** build sprint. Across the term your group completes milestones **M00 through M13** (no gaps in the numbering); each member also submits a confidential intra-group peer evaluation at the end. The project is worth **35%** of the course grade — Milestone Deliverables 30%, Peer Evaluation 20%, Peer Review 10%, Poster Presentation at the conference 20%, Instructor/TA Evaluation 20%. The post-conference **Poster-to-Product** sprint is graded separately as its own **5%** of the course grade. **Presentation at the Purdue Undergraduate Research Conference is required for all students**; the final poster is due nine days before the conference.

---

## What to Submit on Brightspace

| # | File | Description |
|---|------|-------------|
| 1 | **`NN.pdf`** *(e.g., group 03 → `03.pdf`)* | One single PDF — your final poster. There is no need to inform your section number. |

---

## Instructions

1. Review the attached **rubric**, the **Data Communication & Poster Design** material (**nb17**), and the **feedback you received on your first draft (M09)**.
2. **Submission** — submit one single PDF named with your group number (group 01 → `01.pdf`, group 17 → `17.pdf`).

By following these instructions, **the instructor will print your poster for free** in time for the conference.

> **Deadline rationale.** The final poster is due exactly **9 days before** the Undergraduate Research Conference, to leave time for printing and final presentation prep (M11/M12).

---

**Course alignment.** Incorporate the M09 feedback; ensure every claim is backed by the **cross-validated** results from M06/M08; keep the test set out of model selection; and make sure both the **Acknowledgments** and the **AI Use Disclosure** sections are present. Make your stakeholder's decision and your recommended model easy to find. All students present this poster at the conference (required).

**Model comparison (rubric criterion 6).** State the primary metric and your practical margin (the smallest gain that would change your stakeholder's decision, and what it means in their terms). Report each model's cross-validated mean with its SD and approximate 95% interval, labeled descriptive (nb08). Compare the baseline and the tuned model (and any other finalist) on the same folds (same splitter and seed): report the per-fold differences and their mean, and name the verdict under nb08's rule: **real difference** (every fold favors the same model and the mean gap clears the margin), **no winner** (the sign changes across folds), or **practically equivalent** (same sign, but the mean gap is under the margin). Whether two intervals overlap does not decide the comparison, and the test set is not used to select. Your nb08 and nb14 exercises walk through the computation.

**Champion (rubric criterion 6).** Name one champion as nb14 teaches (the baseline can win) and justify it in a short statement in your stakeholder's terms that covers four points: what you recommend and for which decision; the evidence (verdict, mean gain, margin); the checks (secondary metrics, fit time, interpretability) and the runner-up; and what would change your mind. Adopt the more complex model only on a real difference; on no winner or practically equivalent, keep the simpler model and say which verdict it was. With more than two candidates, show the comparisons that led to the champion. If you set the margin after seeing your M06/M08 results, say so: honest disclosure is not penalized. A baseline champion or an honest "no winner" verdict can earn full credit, and no new model search or test-set opening is required.

---

Please feel free to let me know if you have any questions.

All the best,

Prof. Moreira
