import json
from pathlib import Path

import pandas as pd
import streamlit as st

APP_TITLE = "Hiring Copilot Candidate Matcher"
DATA_PATH = Path(__file__).parent / "data" / "candidates.json"

st.set_page_config(page_title=APP_TITLE, page_icon="🤖", layout="wide")

@st.cache_data
def load_candidates():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data

candidates = load_candidates()

st.title("🤖 Hiring Copilot Candidate Matcher")
st.caption("AI-executed candidate matching workflow for recruiter validation and client-ready submission.")

with st.sidebar:
    st.header("Workflow")
    st.markdown(
        """
        **AI executes:**  
        JD understanding → candidate matching → recommendation → validation prep → submission-ready summary

        **Human reviews:**  
        evidence accuracy, risk level, final submission decision, and client communication.
        """
    )
    selected_recommendation = st.multiselect(
        "Filter by recommendation",
        ["Ready to Submit", "Validate First", "Do Not Submit"],
        default=["Ready to Submit", "Validate First", "Do Not Submit"],
    )

st.subheader("Role Understanding")
st.write(
    "The role values AI-native product thinking, workflow design, rapid prototyping, Python/API execution, "
    "strong communication, ownership, and comfort operating inside ambiguous recruiting operations."
)

rubric = pd.DataFrame(
    [
        ["Workflow/Product Thinking", "Can understand messy operations and translate them into product workflows."],
        ["AI Execution", "Can design LLM/agent/automation workflows that execute useful tasks."],
        ["Rapid Prototyping", "Can quickly build practical tools, not just strategy docs."],
        ["Technical Depth", "Python, APIs, data processing, automation, workflow orchestration."],
        ["Communication & Ownership", "Can ask good questions, drive follow-up, and work with operators."],
        ["Recruiting/Ops Sensitivity", "Can understand recruiter, account manager, and client HR workflows."],
    ],
    columns=["Signal", "What it means"],
)
st.dataframe(rubric, use_container_width=True, hide_index=True)

filtered = [c for c in candidates if c["recommendation"] in selected_recommendation]

table = pd.DataFrame(
    [
        {
            "Candidate": c["candidate"],
            "Recommendation": c["recommendation"],
            "Brief Reason": c["brief_reason"],
            "Main Risk": c["main_risk"],
        }
        for c in filtered
    ]
)

st.subheader("Recommendation Table")
st.dataframe(table, use_container_width=True, hide_index=True)
st.download_button(
    "Download recommendation table as CSV",
    table.to_csv(index=False),
    file_name="recommendation_table.csv",
    mime="text/csv",
)

st.subheader("Candidate Review Workspace")
for c in filtered:
    with st.expander(f"{c['candidate']} — {c['recommendation']}", expanded=c["recommendation"] == "Ready to Submit"):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("#### Strengths with evidence")
            for item in c["strengths"]:
                st.markdown(f"- {item}")
            st.markdown("#### Risks")
            for item in c["risks"]:
                st.markdown(f"- {item}")
        with col2:
            st.markdown("#### Scorecard")
            score_df = pd.DataFrame(
                [{"Signal": k.replace("_", " ").title(), "Score": v} for k, v in c["scores"].items()]
            )
            st.bar_chart(score_df.set_index("Signal"))

        st.markdown("#### Recruiter validation questions")
        for q in c["validation_questions"]:
            st.markdown(f"- {q}")

        st.markdown("#### Client-ready summary")
        st.info(c["client_summary"])

st.subheader("Submission Logic")
st.markdown(
    """
    - **Ready to Submit:** strong evidence already supports client submission after light recruiter review.  
    - **Validate First:** promising signals, but recruiter should confirm one or two key gaps.  
    - **Do Not Submit:** talented candidate, but not enough alignment for this specific role.
    """
)
