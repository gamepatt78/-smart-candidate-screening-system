# Smart Candidate Screening System

Live repo: https://github.com/gamepatt78/-smart-candidate-screening-system
Local preview for validation: http://127.0.0.1:8501

## Problem and understanding

The goal of this project is to help a placement coordinator quickly review a large group of student profiles and identify which candidates look strongest for internship and job opportunities. The issue is not just raw academic marks; it is also the mix of technical skills, projects, work exposure, and certifications that together show how job-ready a student is.

This app turns that review into a consistent, explainable process. Instead of relying on gut feeling or scattered spreadsheets, the system gives each student a transparent score and a category so the coordinator can compare people fairly and make quicker decisions.

## What the application does

- Shows all students in one dashboard
- Filters students by name, branch, CGPA minimum, skills, and category
- Summarizes the visible shortlist with category counts
- Explains the reason behind each student’s category
- Lets the reviewer inspect each candidate’s profile without losing context

## Categorization logic in plain language

A student is scored based on five simple signals. Each signal adds points for evidence of readiness:

- CGPA: 2 points for a strong academic record at 8.5 or above, 1 point for 7.0 to 8.49
- Skills: 2 points for 4 or more listed skills, 1 point for 2 to 3 skill areas
- Projects: 2 points for 3 or more projects, 1 point for 1 to 2 projects
- Internship experience: 2 points if an internship is included
- Certifications: 1 point if at least one certificate is present

The total score ranges from 0 to 9.

- Strong: 7 to 9 points
- Average: 4 to 6 points
- Needs Improvement: 0 to 3 points

This is designed to be easy to trust. A placement coordinator can look at the score and immediately understand why a student landed in a category. Missing information does not hurt a student by itself; it simply means that signal is not present in the profile.

## How to run

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

The application reads the CSV file in the same folder and supports both the provided template columns and the original alternate column variations.

## Screenshots and product views

The app has the following key screens:

1. Full student list and dashboard
2. Filter panel for CGPA, skills, and category
3. Student detail expansion with scoring explanation
4. Category summary counts

These views are visible in the running Streamlit app at the local preview URL above. If the app is deployed to a public hosting platform later, the same screenshots can be refreshed there as part of the final presentation pack.

## Technical notes

The project is intentionally deterministic and explainable. It uses a simple rule-based scoring model instead of a black-box model so the result can be reviewed and justified by a human recruiter or coordinator.

## What I would improve with more time

- Allow uploading a new CSV from the interface instead of editing the file locally
- Add export of shortlisted students to CSV or PDF
- Add role-specific matching for different job tracks such as software, data, or mechanical roles
- Add more advanced filters and recruiter notes
- Add authentication and role-based access for placement teams

## Repository status

This project is already pushed to GitHub and is available at the repository link above. The app itself has been validated locally with the working dataset and is ready for deployment to a public platform when a hosting account is available.