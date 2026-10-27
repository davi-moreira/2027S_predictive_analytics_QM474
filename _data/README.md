# Course datasets

`data.zip` is the archive to post for students. It is **edition-agnostic** — it carries only the
datasets the notebook arc uses, so the same archive works in any offering of the course. Extracting
it creates exactly one folder:

```
data/
├── california_housing.csv
└── us_employment.csv
```

The zip is gitignored (the repo carries no `.zip` files); `build_data_zip.sh` is tracked and rebuilds
it byte-for-byte from `notebooks/`.

```bash
bash _data/build_data_zip.sh
```

## Who needs which file

| File | Notebooks | Required? |
|---|---|---|
| `california_housing.csv` | nb01–nb05, nb08, nb09, nb11–nb14, nb19 | No — those notebooks call `fetch_california_housing()`. Offline convenience only. |
| `us_employment.csv` | nb16 | No — nb16 reads it from a raw GitHub URL. Offline convenience only. |

The MedScreen breast-cancer case ships inside scikit-learn (`load_breast_cancer`), so there is no file
to distribute.

## What is deliberately NOT here

**Case-competition data is per-edition and lives with its edition**, not in this archive:

```
_course_case_competition/2026F/fall-2026-qm-47400-case-competition-bank-churn.zip   ← the Kaggle download, untouched
_course_case_competition/2026F/fall-2026-qm-47400-case-competition-bank-churn/      ← extracted: train.csv, test.csv, sample_submission.csv
```

Students get those files from the competition's **Data** tab on Kaggle — that page is the
authoritative source, and downloading from it is part of the exercise. Keeping the competition data
out of `data.zip` is what lets `data.zip` be reused unchanged next term.
