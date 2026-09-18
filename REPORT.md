# Smart Candidate Screening System Report

## Project Links

- **Live app:** https://gamepatt78--smart-candidate-screening-system-app-1fibjl.streamlit.app/
- **GitHub repository:** https://github.com/gamepatt78/-smart-candidate-screening-system
- **Local preview:** http://127.0.0.1:8501

## 1. Executive Summary

The Smart Candidate Screening System is a transparent web application for helping placement coordinators review student profiles quickly and consistently. It replaces slow, manual spreadsheet screening with a shared rule-based scoring process. Each candidate is evaluated using the same written criteria, and the application explains the reason for every category assigned.

The system is designed to support human decision-making rather than replace it. Coordinators can quickly filter candidates by identity, branch, CGPA, skills, and readiness category before preparing a shortlist for recruitment drives.

## 2. Problem Statement

Manual candidate screening becomes unreliable as the number of students increases. Two coordinators reviewing the same dataset may reach different conclusions because the meaning of a "strong" candidate is not formally defined. This creates several problems:

- Screening takes too long when every resume or spreadsheet row must be reviewed manually.
- Strong candidates may be overlooked because reviews are inconsistent or rushed.
- Different coordinators may apply different standards.
- Recruitment teams may not have enough time to prepare a fair shortlist before a company visit.
- Students and coordinators may not understand why a candidate was placed in a particular category.

The placement team therefore needs a system that is fast, consistent, explainable, and easy to use.

## 3. Project Objectives

The project aims to:

1. Create a shared definition of candidate readiness.
2. Apply the same evaluation rules to every student.
3. Provide a transparent explanation for each result.
4. Reduce the time required to prepare recruitment shortlists.
5. Allow coordinators to locate candidates using practical filters.
6. Present candidate information in a clear dashboard instead of a difficult-to-scan spreadsheet.

## 4. Proposed Solution

The application is built with Python, Pandas, and Streamlit. It reads candidate information from a CSV file, transforms the data into a consistent format, calculates a score for each student, and displays the results in an interactive dashboard.

The system uses deterministic rules rather than a black-box artificial intelligence model. This means that the same candidate data always produces the same score and category. A coordinator can inspect the rules and explain the result in one sentence.

## 5. Evaluation Method

Each candidate can receive a maximum of 9 points:

| Evaluation area | Scoring rule | Maximum points |
|---|---|---:|
| CGPA | 2 points for 8.5 or above; 1 point for 7.0 to 8.49 | 2 |
| Skills | 2 points for 4 or more skills; 1 point for 2 to 3 skills | 2 |
| Projects | 2 points for 3 or more projects; 1 point for 1 to 2 projects | 2 |
| Internship | 2 points when internship experience is listed | 2 |
| Certifications | 1 point when at least one certification is listed | 1 |
| **Total** |  | **9** |

Candidates are categorized using the total score:

- **Strong:** 7 to 9 points
- **Average:** 4 to 6 points
- **Needs Improvement:** 0 to 3 points

These thresholds provide a common standard for placement coordinators while keeping the final decision explainable.

## 6. Main Features

### Candidate dashboard

The dashboard displays the complete candidate list, total students shown, and counts for each readiness category.

### Search

Coordinators can search by candidate name, ID, or branch. Numeric ID searches use exact matching, so searching for ID `2` does not incorrectly return ID `12`.

### CGPA range filtering

The CGPA range slider supports both minimum and maximum values. For example, a coordinator can select a range from `3.40` to `6.60`. The Reset CGPA range button restores the visible slider to the default range of `0.0` to `10.0`.

### Skills filtering

The required-skills filter can be used to find candidates with a particular skill, such as React. This allows a coordinator to combine requirements such as a CGPA range and technical skills.

### Category filtering

Coordinators can display only Strong, Average, or Needs Improvement candidates, or any combination of these categories.

### Explainable student details

Each candidate has an expandable detail section containing contact information, branch, CGPA, skills, projects, internship experience, certifications, and a short scoring explanation.

## 7. Technical Implementation

The system uses:

- **Python** for application logic
- **Streamlit** for the interactive web interface
- **Pandas** for CSV loading, data cleaning, filtering, and calculations
- **CSV storage** for the candidate dataset

The application cleans missing values, converts CGPA values into numbers, separates comma- or delimiter-based lists such as skills and projects, calculates scores, assigns categories, and applies the selected filters.

The application is available locally through Streamlit and is also deployed online for access by the placement team.

## 8. Benefits

The proposed system provides the following benefits:

- Faster shortlist preparation for recruitment drives
- More consistent evaluation across coordinators
- Clear and defensible placement decisions
- Less manual spreadsheet scanning
- Easy combination of academic and technical filters
- Better visibility into each student profile
- A simple interface that does not require machine-learning expertise

## 9. Limitations

The current system is a screening aid, not a complete recruitment decision-maker. Its results depend on the accuracy and completeness of the CSV data. The scoring rules are intentionally simple and may not capture communication ability, interview performance, leadership, or role-specific requirements.

The system also does not currently include user authentication, direct CSV upload, shortlist export, recruiter notes, or separate scoring models for different job roles.

## 10. Future Enhancements

Future versions could include:

- Uploading and validating new candidate files through the interface
- Exporting filtered shortlists to CSV or PDF
- Role-specific rules for software, data, mechanical, or other recruitment tracks
- Recruiter notes and shortlist status tracking
- Authentication and coordinator-level access control
- Audit history for changes to scoring rules
- Additional evaluation fields such as communication, aptitude, and interview scores

## 11. Conclusion

The Smart Candidate Screening System addresses the central problems of manual candidate review: inconsistency, delay, and lack of explainability. By applying the same written scoring rules to every student and providing practical filters, it helps placement coordinators prepare fair shortlists more efficiently.

The system does not make mysterious decisions. Instead, it provides a transparent starting point that coordinators can inspect, explain, and use alongside their professional judgment.
