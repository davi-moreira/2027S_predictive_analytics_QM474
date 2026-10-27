---
kicker: "Milestone 02"
title: "Expanded Project Outline"
csv: ["Milestone 02 —"]
box:
  - label: Due
    value: "**Sunday, February 14, 2027, 11:59 PM ET**"
  - label: Opens
    value: "Monday, February 8, 2027"
  - label: Submit
    value: "One PDF per group, uploaded by one member: `NN_outline.pdf` (two to three pages, with visualizations)"
  - label: Grading
    value: "50 points: five criteria, 10 points each"
---

## What this milestone is for

Your proposal said *what* you will predict. The outline says *how*. It builds on Milestone 01, and on the feedback you received for it, by spelling out how you will prepare the data, which methods you will use, how you will measure success, and what the first look at the data already tells you.

## What to do

Write two to three pages with five parts.

1. **Revised prediction goal and objectives.** Sharpen your prediction goal if needed, and state your project objectives clearly.
2. **Data preparation.** The cleaning and preprocessing steps you will take, and the new features you plan to create to improve your models.
3. **Methodology.** The methods or models you will use, in some detail, and the evaluation metrics you will use to judge them (for example accuracy, F1 score or RMSE), with a word on why those metrics fit your goal.
4. **Exploratory data analysis.** Your first findings: summary statistics and charts (histograms, bar charts, scatter plots) that show patterns or trends in the data.
5. **Anticipated challenges.** What could go wrong (data quality problems, overfitting, and so on) and how you plan to handle it.

Use subheadings and bullet points where they help, and put charts where they support the text.

## What to submit

One member uploads `NN_outline.pdf` for the whole group, for example `03_outline.pdf`.

## How it is graded

Fifty points: one criterion per part, each worth 10 points, scored as exemplary (9–10), proficient (7–8), developing (5–6) or beginning (0–4).

- **Revised goal and objectives:** a goal clearly refined from Milestone 01 and well-stated objectives.
- **Data preparation:** cleaning, preprocessing and feature engineering described in detail, with reasons and an eye on likely problems.
- **Methodology and evaluation metrics:** methods and metrics described fully and tightly linked to the goal.
- **Exploratory analysis and visualizations:** charts that reveal real patterns, and an interpretation that informs your modeling choices.
- **Anticipated challenges and overall quality:** sensible risks with thoughtful remedies, in a well-organized, error-free, professional document.

## Tips

- Plan your preprocessing as a **pipeline** (notebooks 01 and 02), so it can be cross-validated honestly in Milestone 06.
- Choose a metric that reflects what errors cost in your problem (notebooks 03 and 07).
- Plan the evaluation the way the course does it from notebook 08 on: one 80/20 train/test split at the start, five-fold cross-validation on the training set for everything else, and the test set opened only once, at the end.
- Show that you used the Milestone 01 feedback.

*The Final Project Overview PDF has every date, the meeting rounds, and how the project is graded.*
