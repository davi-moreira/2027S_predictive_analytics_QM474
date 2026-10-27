---
kicker: "Final Project"
title: "Overview, Components and Calendar"
fontsize: "10pt"
box:
  - label: Event
    value: "**Spring Undergraduate Research Conference, poster session, Tuesday, April 13, 2027.** Presenting is required for everyone"
  - label: Poster
    value: "Final poster (Milestone 10) due **Sunday, April 4, 2027, 11:59 PM ET**, nine days before the conference"
  - label: Weight
    value: "35% of the course grade. Poster-to-Product, after the conference, is a separate 5%"
  - label: Groups
    value: "Groups of four, randomly assigned. One member uploads each group file, named with your group number (`NN`)"
---

## What the Final Project is

The Final Project is your group's capstone. You take a real prediction problem, build and evaluate models on real data, choose the one your stakeholder should use, and present the work as a research poster at Purdue's **Spring Undergraduate Research Conference** on Tuesday, April 13, with Professor Moreira as your faculty mentor. It runs as milestones M00 to M13 (no gaps in the numbering), plus a peer review, the conference and a peer evaluation.

The project must use **real data**: observations collected from actual people, organizations, transactions, markets, public records, surveys, experiments, devices or other real processes. Synthetic, simulated, artificially generated and AI-generated datasets are not eligible, and neither is the synthetic Bank Churn data of the Course Case Competition.

For inspiration, see award-winning posters from earlier editions of this course: <https://davi-moreira.github.io/applied_projects.html>. Conference information: <https://www.purdue.edu/undergrad-research/conferences/index.php>.

## How it is graded

| Component | Share of the project | Share of the course | What it covers |
|--------------------|------:|------:|----------------------------|
| Milestone deliverables | 30% | 10.5% | The milestones below: clarity, completeness, timeliness |
| Peer evaluation (of teammates) | 20% | 7% | Your teammates' confidential ratings of you |
| Peer review (of posters) | 10% | 3.5% | Your group's feedback on other groups' posters |
| Conference presentation | 20% | 7% | Presenting your poster at the conference |
| Instructor/TA evaluation | 20% | 7% | Your final poster, scored with the poster rubric |
| **Total** | **100%** | **35%** | |

## Milestones and dates

Everything is due at 11:59 PM Eastern unless noted. Each item has its own PDF with the details.

| Item | What you do | Opens | Due | Grading |
|--------|---------------------|-------|-------|-----------|
| M00 | Round 01 meeting requests and group contract | Mon Feb 1 | Sun Feb 7 | completion |
| M01 | Initial project proposal | Wed Jan 27 | Sun Feb 7 | 50 points |
| M02 | Expanded project outline | Mon Feb 8 | Sun Feb 14 | 50 points |
| M03 | Project draft abstract | Mon Feb 15 | Sun Feb 21 | 30 points |
| M04 | Round 01 meetings: confirmation | Thu Feb 18 | Sun Feb 28 | completion |
| M05 | Apply to the conference (OURConnect) | Thu Feb 18 | Sun Feb 28 | completion |
| M06 | Simple model and evaluation | Thu Feb 18 | Sun Mar 7 | 100 points |
| M07 | Round 02 meeting requests | Thu Feb 18 | Sun Mar 7 | completion |
| M08 | More complex models and evaluation | Thu Feb 18 | Sun Mar 14 | 100 points |
| M09 | Poster first draft (`NN.pdf`) | Mon Mar 22 | Sun Mar 28 | poster rubric (feedback) |
| M10 | Final poster (`NN.pdf`) | Mon Mar 29 | Sun Apr 4 | poster rubric |
| M11 | Poster presentation planning | Sun Apr 4 | Sun Apr 11 | rubric |
| M12 | Post an invitation to your presentation | Sun Apr 4 | Sun Apr 11 | completion |
| M13 | Round 02 meetings: confirmation | Sun Apr 4 | Sun Apr 11 | completion |
| Peer review | Review five other groups' posters | Sun Apr 4 | Sun Apr 11 | 10% of the project |
| Conference | Present your poster (required; in person) | Tue Apr 13 | Tue Apr 13 | 20% of the project |
| P2P product | Poster-to-Product: team product | Fri Apr 16 | Mon Apr 26 | part of P2P's 5% |
| P2P live link | Poster-to-Product: your live link | Fri Apr 16 | Wed Apr 28 | part of P2P's 5% |
| Peer evaluation | Rate your teammates (individual) | Mon Apr 26 | Fri Apr 30 | 20% of the project |

## The meeting cycle

In each of two rounds your group asks for a meeting with the TA and one with Professor Moreira, then confirms they happened. At least one member attends each meeting, not necessarily the same one, and there are no meetings during spring break (March 15 to March 20). Round 01 is about your prediction problem, your data and your modeling plan; Round 02 is about your models, your modeling strategy and your poster.

| Round | Ask for the meetings | TA meeting | Meeting with Professor Moreira | Confirm |
|------|----------|-------------|-----------|----------|
| Round 01 | M00, due Sun Feb 7 | Mon Feb 8 to Sun Feb 21 | Mon Feb 22 to Sun Feb 28 | M04, due Sun Feb 28 |
| Round 02 | M07, due Sun Mar 7 | Mon Mar 8 to Sun Mar 14, or Mon Mar 22 to Sun Mar 28 | Mon Mar 29 to Sat Apr 3 | M13, due Sun Apr 11 |

## How your models are evaluated

As in the course from notebook 08 on: one 80/20 train/test split; all modeling on the training set with five-fold cross-validation; the test set opened once, at the end, for your chosen model. Models are compared on the same five folds through their per-fold differences, read against a margin δ set before comparing, as one of four outcomes (worthwhile gain, worthwhile loss, practically equivalent, unresolved). A more complex model replaces the baseline only on a worthwhile gain, so the baseline can be your champion. Milestones 06 and 08 walk you through it.

## Good to know

- **The conference may not fall at our class time:** tell your other instructors early about any conflict. No class on Wednesday, April 14.
- **Peer review is not peer evaluation:** one is feedback on other groups' posters, the other your confidential rating of your teammates.
- **Honors contract?** The syllabus explains how your weights change. **Notebook checkpoints** ("M1" to "M4") are skill checks, not milestones.
