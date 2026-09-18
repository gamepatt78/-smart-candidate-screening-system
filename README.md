# Smart Candidate Screening System

Streamlit application for quickly reviewing final-year student profiles using consistent, explainable rules.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

The app reads `students.csv` from the same folder. It supports the provided dataset columns and the assessment template column names, including missing values and comma, semicolon, pipe, or slash-separated lists.

## Categorization logic

Every student receives a score out of 9:

| Signal | Points |
| --- | --- |
| CGPA 8.5+ / 7.0–8.49 | 2 / 1 |
| 4+ skills / 2–3 skills | 2 / 1 |
| 3+ projects / 1–2 projects | 2 / 1 |
| Internship listed | 2 |
| Certification listed | 1 |

Scores of 7–9 are **Strong**, 4–6 are **Average**, and 0–3 are **Needs Improvement**. Missing information earns no points; it is never treated as evidence against a student beyond the absence of that signal.

The dashboard metrics are calculated from the currently filtered rows, so the summary always describes the visible shortlist.

## Product notes

The current version is intentionally deterministic and auditable. Future improvements could include uploading a new CSV from the interface, role-specific skill matching, configurable scoring weights, exportable shortlists, and authentication for student data.