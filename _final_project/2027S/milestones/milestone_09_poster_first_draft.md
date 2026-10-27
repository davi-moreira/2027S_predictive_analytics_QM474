---
kicker: "Milestone 09"
title: "Poster First Draft"
csv: ["Milestone 09 —"]
box:
  - label: Due
    value: "**Sunday, March 28, 2027, 11:59 PM ET**"
  - label: Opens
    value: "Monday, March 22, 2027"
  - label: Submit
    value: "One PDF per group, uploaded by one member, named with your group number only: `NN.pdf` (for example `03.pdf`; no section number)"
  - label: Grading
    value: "The poster rubric, 100 points (attached on Brightspace). On this draft, criterion 6 (model comparison and champion) gets feedback, not a deduction"
---

## What this milestone is for

This is the first full version of your conference poster. Build it on the poster template and the rubric (both attached on Brightspace) and on notebook 17, *Data Communication and Poster Design*. The feedback you get on this draft is what you fix for the final poster in Milestone 10.

## What to do

**1. Put the core content on the poster.**

- **Title and authors.** A clear title that reflects your question, every team member's name, and your mentor acknowledged.
- **Abstract or introduction.** The question, why it matters, and a short summary of your data, your two models (baseline and complex) and your main finding.
- **Methods and data.** The baseline and the complex model, the dataset and its key variables, your preprocessing (feature engineering, missing data) and your tuning approach, each justified against the question. Name your **stakeholder** and the **decision** your model supports, and your **selection criteria**: the primary metric and the margin δ with what it means in the stakeholder's terms. Say when you set δ; if it was after you saw results, say so.
- **Results.** For each model, its five fold scores, their mean and their standard deviation. [[PENDING D4: whether to report a per-model 95% interval — currently: report fold scores, mean and SD]] Then the comparison from Milestone 08: the per-fold differences on the same folds, their mean, the corrected interval, and which of the four outcomes it is (worthwhile gain, worthwhile loss, practically equivalent, unresolved). A small dot plot of the per-fold differences next to ±δ works well. Add the champion's test score, from the single opening in Milestone 08. [[PENDING R7: prediction intervals]] Interpret honestly and note limitations or anomalies.
- **Conclusions and future directions.** Your champion and its four-point statement (what you recommend and for which decision; the evidence; the checks and the runner-up; what would change your mind), then the implications, possible improvements and next steps, tied back to your question.

**2. Organize it.** A logical flow (introduction, exploration, methods, results, conclusions), headings and short numbered sections, and charts placed where the text refers to them.

**3. Cite and acknowledge.** Cite the data, references and code you used. Add an **Acknowledgments** section that names, as applicable, the Mitch Daniels School of Business (if it funded your participation), Professor Davi Moreira (mentor), the TAs, and anyone else who helped.

> *Example:* "We thank Professor Davi Moreira for his mentorship throughout the project. We are also grateful to our TAs, [Name] and [Name], for their guidance. This work was supported by the Mitch Daniels School of Business. We also acknowledge the Undergraduate Research Center and Purdue University for this valuable opportunity."

**4. Disclose AI use.** Per the syllabus AI Policy, fill in the template's **AI USE DISCLOSURE** section: each AI tool you used, what it did (code, debugging, editing, figure design), and that your group reviewed and verified the output. If you used none, write "No AI tools were used." Without this section, rubric criterion 8 cannot earn more than 2 of its 5 points.

> *Example:* "We used Gemini in Google Colab to debug our cross-validation code and ChatGPT to tighten the abstract's wording. We reviewed and verified every AI-assisted output and take full responsibility for this poster."

**5. Design it to be read.** A clean layout, main text of at least 18 points, high contrast, charts and tables with titles, axes and legends, white space, short text, and consistent formatting.

**6. Protect privacy.** No personally identifiable or sensitive data on the poster. In line with any data agreement, delete detailed data permanently when the project ends. Such data on the poster scores 0 on criterion 8 and must be removed before printing.

## What to submit

One member uploads a single PDF for the whole group, named with your group number only: group 01 uploads `01.pdf`, group 17 uploads `17.pdf`.

## How it is graded

With the poster rubric (100 points): prediction goal 5, dataset overview 8, exploratory analysis 12, data preparation 18, baseline model 17, model comparison and champion selection 25, report quality and visual communication 10, and sources, acknowledgments, AI use and data privacy 5. On this first draft, criterion 6 (the comparison and the champion) gets feedback, not a deduction; it is scored from Milestone 10.

## Tips

- Every number on the poster comes from cross-validation on the training set (Milestones 06 and 08), except the champion's single test score. The test set never helps choose.
- A baseline champion, or an honest "unresolved", is a legitimate result.
- Make your stakeholder's decision and your champion easy to find at a glance.

*The Final Project Overview PDF has every date, the meeting rounds, and how the project is graded.*
