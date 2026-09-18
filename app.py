from pathlib import Path
import re

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Candidate Screening", page_icon="CS", layout="wide")

st.markdown(
    """
    <style>
        :root {
            --bg: #0b1018;
            --bg-2: #121b29;
            --panel: #111a27;
            --panel-strong: #0d1622;
            --panel-soft: #1b2738;
            --border: rgba(255,255,255,0.08);
            --text: #edf3ff;
            --muted: #b5c0d5;
            --accent: #f26464;
            --accent-2: #ff8a5b;
            --success: #4be2b5;
            --warning: #f7d26b;
        }

        .stApp {
            background: linear-gradient(180deg, #0e1520 0%, #101a27 100%);
            color: var(--text);
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 3rem;
            max-width: 1400px;
        }

        div[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0d151f 0%, #111b28 100%);
            border-right: 1px solid var(--border);
        }

        div[data-testid="stSidebar"] > div {
            padding-top: 1rem;
        }

        [data-testid="stSidebarContent"] {
            background: rgba(17, 26, 39, 0.92);
        }

        .stHeader {
            background: rgba(11, 16, 24, 0.9);
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--text) !important;
        }

        .stDataFrame, .stTable {
            background: rgba(17, 24, 39, 0.92);
            border: 1px solid var(--border);
            border-radius: 12px;
            overflow: hidden;
        }

        div[data-testid="stDataFrameWrapper"] {
            overflow-x: auto;
            border-radius: 12px;
        }

        table {
            background: #0f1724 !important;
            color: var(--text) !important;
        }

        th {
            background: rgba(30, 41, 59, 0.9) !important;
            color: var(--text) !important;
            border-bottom: 1px solid var(--border) !important;
        }

        td {
            background: rgba(15, 23, 36, 0.9) !important;
            color: var(--text) !important;
            border-bottom: 1px solid rgba(255,255,255,0.05) !important;
            white-space: nowrap;
        }

        .stMetric {
            background: rgba(21, 31, 42, 0.85);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 0.8rem 1rem;
            box-shadow: none;
        }

        [data-testid="stMetricValue"] {
            color: var(--text);
        }

        [data-testid="stMetricDelta"] {
            color: var(--muted);
        }

        .stTextInput > div > div > input,
        .stSelectbox > div > div,
        .stMultiSelect > div > div,
        .stSlider > div > div,
        .stNumberInput > div > div,
        .stRadio > div,
        .stCheckbox > label {
            background: rgba(17, 24, 39, 0.8);
            color: var(--text);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 10px;
        }

        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] {
            color: var(--text) !important;
            background: transparent !important;
        }

        .stTextInput input::placeholder,
        .stSelectbox [role="button"] {
            color: var(--muted) !important;
        }

        .stCheckbox {
            color: var(--text);
        }

        .stToggle [data-testid="stBaseButton-secondary"] {
            background: rgba(17,24,39,0.8);
        }

        .stExpander {
            background: rgba(17, 24, 39, 0.7);
            border: 1px solid var(--border);
            border-radius: 12px;
        }

        .stExpander summary {
            color: var(--text) !important;
            background: transparent;
        }

        .st-emotion-cache-18ni7ap {
            color: var(--text) !important;
        }

        .stApp a {
            color: #8ec5ff;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }

            h1 {
                font-size: 2rem !important;
            }

            h2 {
                font-size: 1.45rem !important;
            }

            div[data-testid="stSidebar"] {
                position: static !important;
                width: 100% !important;
                max-width: 100% !important;
            }

            [data-testid="stSidebarContent"] {
                padding: 0.75rem 0.75rem 1rem 0.75rem;
            }

            [data-testid="stMetric"] {
                margin-bottom: 0.6rem;
            }

            .stExpander {
                margin-bottom: 0.5rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

DATA_FILE = Path(__file__).with_name("students.csv")
MISSING_VALUES = {"", "na", "n/a", "none", "null", "-"}


def clean_text(value) -> str:
    if pd.isna(value):
        return ""
    value = str(value).strip()
    return "" if value.lower() in MISSING_VALUES else value


def split_items(value) -> list[str]:
    value = clean_text(value)
    if not value:
        return []
    return [item.strip() for item in re.split(r"[,;|/]", value) if item.strip()]


def column(frame: pd.DataFrame, *names: str) -> pd.Series:
    for name in names:
        if name in frame.columns:
            return frame[name]
    return pd.Series([""] * len(frame), index=frame.index)


def load_candidates() -> pd.DataFrame:
    raw = pd.read_csv(DATA_FILE, dtype=str, keep_default_na=False).fillna("")
    candidates = pd.DataFrame(index=raw.index)
    candidates["id"] = column(raw, "student_id", "ID").map(clean_text)
    candidates["name"] = column(raw, "name", "Name").map(clean_text)
    candidates["email"] = column(raw, "email", "Email").map(clean_text)
    candidates["phone"] = column(raw, "phone", "Phone").map(clean_text)
    candidates["branch"] = column(raw, "degree", "Branch").map(clean_text)
    candidates["cgpa"] = pd.to_numeric(column(raw, "cgpa", "CGPA"), errors="coerce")
    candidates["skills"] = column(raw, "skills", "Skills").map(split_items)
    candidates["projects"] = column(raw, "projects", "Projects").map(split_items)
    candidates["internship"] = column(raw, "internship_experience", "Internships").map(clean_text)
    candidates["certifications"] = column(raw, "certifications", "Certifications").map(split_items)
    explicit_count = pd.to_numeric(column(raw, "project_count"), errors="coerce")
    candidates["project_count"] = explicit_count.fillna(candidates["projects"].map(len)).astype(int)
    candidates["has_internship"] = candidates["internship"].ne("")
    candidates["skill_count"] = candidates["skills"].map(len)
    candidates["certification_count"] = candidates["certifications"].map(len)
    candidates["score"] = candidates.apply(score_candidate, axis=1)
    candidates["category"] = candidates["score"].map(category_for_score)
    candidates["reason"] = candidates.apply(reason_for_candidate, axis=1)
    return candidates


def score_candidate(candidate: pd.Series) -> int:
    score = 0
    if pd.notna(candidate["cgpa"]):
        score += 2 if candidate["cgpa"] >= 8.5 else 1 if candidate["cgpa"] >= 7 else 0
    score += 2 if candidate["skill_count"] >= 4 else 1 if candidate["skill_count"] >= 2 else 0
    score += 2 if candidate["project_count"] >= 3 else 1 if candidate["project_count"] >= 1 else 0
    score += 2 if candidate["has_internship"] else 0
    score += 1 if candidate["certification_count"] else 0
    return score


def category_for_score(score: int) -> str:
    return "Strong" if score >= 7 else "Average" if score >= 4 else "Needs Improvement"


def reason_for_candidate(candidate: pd.Series) -> str:
    if candidate["category"] == "Strong":
        return f"{candidate['score']}/9 points from academics, skills, projects, experience and certifications."
    if candidate["category"] == "Average":
        return f"{candidate['score']}/9 points; a developing profile with some placement-ready evidence."
    return f"{candidate['score']}/9 points; more evidence of skills, projects or experience would strengthen this profile."


def display_list(values: list[str]) -> str:
    return ", ".join(values) if values else "Not listed"


@st.cache_data
def get_data() -> pd.DataFrame:
    return load_candidates()


candidates = get_data()
st.title("Candidate Screening")
st.caption("A transparent, consistent view of placement readiness")

with st.sidebar:
    st.header("Filter candidates")
    search = st.text_input("Search name, ID or branch")
    minimum_cgpa = st.slider("Minimum CGPA", 0.0, 10.0, 0.0, 0.1)
    all_skills = sorted({skill for skills in candidates["skills"] for skill in skills})
    selected_skills = st.multiselect("Required skills", all_skills)
    selected_categories = st.multiselect(
        "Categories", ["Strong", "Average", "Needs Improvement"], default=[]
    )
    show_explanation = st.toggle("Show scoring explanation", value=True)

filtered = candidates[candidates["cgpa"].fillna(-1) >= minimum_cgpa]
if search:
    query = search.strip()
    q_lower = query.lower()
    if query.isdigit():
        filtered = filtered[
            filtered["id"].astype(str).str.strip().str.lower().eq(q_lower)
        ]
    else:
        filtered = filtered[
            filtered[["name", "branch"]].fillna("").apply(
                lambda row: row.astype(str).str.lower().str.contains(q_lower, regex=False).any(), axis=1
            )
        ]
if selected_skills:
    wanted = {skill.lower() for skill in selected_skills}
    filtered = filtered[filtered["skills"].map(lambda skills: wanted.issubset({s.lower() for s in skills}))]
if selected_categories:
    filtered = filtered[filtered["category"].isin(selected_categories)]

counts = filtered["category"].value_counts()
metric_columns = st.columns(4)
metric_columns[0].metric("Students shown", len(filtered))
metric_columns[1].metric("Strong", int(counts.get("Strong", 0)))
metric_columns[2].metric("Average", int(counts.get("Average", 0)))
metric_columns[3].metric("Needs Improvement", int(counts.get("Needs Improvement", 0)))

st.divider()
st.subheader("Student list")
st.caption(f"Showing {len(filtered)} of {len(candidates)} students")

if filtered.empty:
    st.info("No students match these filters.")
else:
    table = filtered[["id", "name", "branch", "cgpa", "skill_count", "project_count", "category"]].copy()
    table.columns = ["ID", "Name", "Branch", "CGPA", "Skills", "Projects", "Category"]
    st.dataframe(
        table,
        hide_index=True,
        width="stretch",
        column_config={
            "CGPA": st.column_config.NumberColumn(format="%.2f"),
            "Category": st.column_config.TextColumn(width="medium"),
        },
    )

    st.subheader("Student details")
    for _, candidate in filtered.iterrows():
        with st.expander(f"{candidate['name']}  |  {candidate['category']}  |  {candidate['id']}"):
            left, right = st.columns(2)
            with left:
                st.write(f"**Contact:** {candidate['email'] or 'Not listed'}")
                st.write(f"**Branch:** {candidate['branch'] or 'Not listed'}")
                st.write(f"**CGPA:** {candidate['cgpa']:.2f}" if pd.notna(candidate["cgpa"]) else "**CGPA:** Not listed")
            with right:
                st.write(f"**Skills:** {display_list(candidate['skills'])}")
                st.write(f"**Projects:** {display_list(candidate['projects'])}")
                st.write(f"**Internship:** {candidate['internship'] or 'Not listed'}")
                st.write(f"**Certifications:** {display_list(candidate['certifications'])}")
            if show_explanation:
                st.caption(candidate["reason"])

with st.expander("How categorization works"):
    st.write("Each student receives up to 9 points using the same written rules for everyone.")
    st.markdown("- **CGPA:** 2 points for 8.5 or above; 1 point for 7.0–8.49.")
    st.markdown("- **Skills:** 2 points for 4 or more listed skills; 1 point for 2–3.")
    st.markdown("- **Projects:** 2 points for 3 or more projects; 1 point for 1–2.")
    st.markdown("- **Internship:** 2 points when an internship is listed.")
    st.markdown("- **Certifications:** 1 point when at least one certification is listed.")
    st.markdown("- **Strong:** 7–9 points. **Average:** 4–6 points. **Needs Improvement:** 0–3 points.")