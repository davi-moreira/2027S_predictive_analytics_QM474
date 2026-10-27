# Milestone 09 — Poster First Draft

## About the Final Project

The Final Project is a **group capstone** (groups of four, randomly assigned) culminating in a **research poster** and a post-conference **Poster-to-Product** build sprint. Across the term your group completes milestones **M00 through M13** (no gaps in the numbering); each member also submits a confidential intra-group peer evaluation at the end. The project is worth **35%** of the course grade — Milestone Deliverables 30%, Peer Evaluation 20%, Peer Review 10%, Poster Presentation at the conference 20%, Instructor/TA Evaluation 20%. The post-conference **Poster-to-Product** sprint is graded separately as its own **5%** of the course grade. **Presentation at the Purdue Undergraduate Research Conference is required for all students**; the final poster is due one week before the conference.

---

## What to Submit on Brightspace

| # | File | Description |
|---|------|-------------|
| 1 | **`NN.pdf`** *(e.g., group 03 → `03.pdf`)* | A single-PDF first draft of your poster. No need to inform your section number. |

Use the attached **template** and **rubric**, plus the **Data Communication & Poster Design** material (**nb17**).

---

## 1. Prepare Your Core Content

**a) Title and Authors** — clear, concise title reflecting your research question; all team members' names (plus advisor/mentor acknowledgments).

**b) Abstract / Introduction** — state the research question/problem; provide context and importance; briefly summarize methods (baseline + advanced), data, and main findings.

**c) Methods and Data** — describe your **baseline model** (Linear/Logistic) and **advanced model** (e.g., Random Forest, SVM, Gradient Boosting); summarize the dataset, key variables, preprocessing (feature engineering, missing data); summarize the **hyperparameter-tuning** approach; justify each method against your question. Name your **stakeholder** and the **decision** your model supports, and state your **selection criteria**: the primary metric and a **practical margin** (the smallest gain that would change that decision, and what it means in your stakeholder's terms, e.g., dollars, missed cases, customers). Say when you set the margin.

**d) Results and Analysis** — report each model's primary metric as its **cross-validated mean with its SD and approximate 95% interval**, labeled descriptive (nb08). Compare the baseline and the tuned model (and any other finalist) on the **same folds** (same splitter and seed): show the **per-fold differences and their mean**, and name the verdict under nb08's rule: **real difference** (every fold favors the same model and the mean gap clears the margin), **no winner** (the sign changes across folds), or **practically equivalent** (same sign, but the mean gap is under the margin). Whether two intervals overlap does not decide the comparison. A small dot plot of the per-fold differences next to the margin works well (nb17). Interpret accurately, noting limitations or anomalies.

**e) Conclusions and Future Directions** — **declare your champion** as nb14 teaches (the baseline can win): the more complex model wins only on a real difference; on no winner or practically equivalent, keep the simpler model and say which verdict it was. Justify the pick in a short statement in your stakeholder's terms that covers four points: what you recommend and for which decision; the evidence (verdict, mean gain, margin); the checks (secondary metrics, fit time, interpretability) and the runner-up; and what would change your mind. Then give implications, possible improvements, and next steps, tied back to your research question.

## 2. Organize Effectively
Logical flow (Introduction → EDA → Methods → Results → Conclusion); tie conclusions to data/analysis; highlight implications for future work. Use headings, bullets, and numbered sections; place visuals where they belong and reference them in text.

## 3. Document Sources & Acknowledge Collaborators
Proper citations for references/data/code; credit sources; acknowledge partners and advisors (TAs, domain experts).

## 4. Design an Effective Visual Presentation
Clean, attractive layout with readable fonts (≥18 pt for main text); high-contrast color scheme; clearly labeled charts/tables (titles, axes, legends); effective white space. Keep text concise; highlight significant results; keep formatting consistent.

## 5. Data Privacy & NDA Compliance
Your poster must **not** contain personally identifiable or sensitive data. In line with any NDA, all detailed data must be permanently deleted upon completion of your project. Any such data on the poster scores 0 on rubric criterion 8 and must be removed before the poster is printed.

## 6. Acknowledgments Section (include on the poster)
As applicable: **Mitch Daniels School of Business** (if it funded your participation); **Professor Davi Moreira** (mentor); **Teaching Assistants**; any other contributing individuals or institutions.
> *Example:* "We thank Professor Davi Moreira for his mentorship throughout the project. We are also grateful to our TAs, [Name] and [Name], for their guidance. This work was supported by the Mitch Daniels School of Business. We also acknowledge the Undergraduate Research Center and Purdue University for this valuable opportunity."

## 7. AI Use Disclosure (include on the poster)
Per the syllabus **AI Policy**, every poster discloses AI use in the template's **AI USE DISCLOSURE** section: name each AI tool you used (e.g., Gemini in Colab), say what it did (code, debugging, text editing, figure design), and state that your group reviewed and verified the output. If you used no AI tools, write *"No AI tools were used."* A poster without this section cannot earn more than 2 of the 5 points in rubric criterion 8.
> *Example:* "We used Gemini in Google Colab to debug our cross-validation code and ChatGPT to tighten the abstract's wording. We reviewed and verified every AI-assisted output and take full responsibility for this poster."

## 8. Submission
Submit one PDF named with your group number — group 01 → `01.pdf`, group 17 → `17.pdf`.

---

**Course alignment.** Your headline numbers come from M06 (baseline) and M08 (tuned model), all **cross-validated** (course rule). Compare the two on **identical folds** with **per-fold paired differences** read against your practical margin (nb08), and **name a champion** as nb14 teaches, with a rationale tied to your stakeholder's decision (rubric criterion 6). If you set the margin after seeing your M06/M08 results, say so on the poster: honest disclosure is not penalized. A baseline champion or an honest "no winner" verdict can earn full credit, and no new model search or test-set opening is required. On this draft criterion 6 gets feedback only; it is scored on the final poster (M10). Keep the test set out of model selection. Apply the six principles + eleven-section poster architecture from **nb17**. This draft gets feedback you incorporate into the final poster (M10).

---

Please feel free to let me know if you have any questions.

All the best,

Prof. Moreira
