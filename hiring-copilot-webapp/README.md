# Hiring Copilot Candidate Matcher

A simple Streamlit web app for the OCBridge / Hiring Copilot Applied AI Product Intern assignment.

The app demonstrates an AI-executed, human-in-the-loop recruiting workflow:

```text
JD Understanding → Candidate Matching → Recommendation → Validation Prep → Submission-Ready Output
```

## What the app does

- Shows a role-based evaluation rubric
- Generates a recommendation table for 7 sourced candidates
- Labels candidates as:
  - Ready to Submit
  - Validate First
  - Do Not Submit
- Provides strengths and risks with evidence
- Generates recruiter validation questions
- Produces client-ready candidate summaries
- Allows the recruiter to download the recommendation table as CSV

## Why this design

This prototype is not only a resume scorer. It is designed to help recruiters and recruiting operations teams move faster while keeping humans responsible for judgment, validation, and submission approval.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Suggested deployment options

### Option 1: Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Set the app entry file to `app.py`.
5. Deploy.

### Option 2: Run from GitHub Codespaces

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files

```text
app.py                  # Streamlit web app
requirements.txt        # Python dependencies
data/candidates.json    # Structured candidate recommendation data
product_note.md         # One-page product note
```

## Human-in-the-loop principle

The AI executes first-pass matching and prepares structured output. Recruiters validate evidence, ask follow-up questions, edit summaries, and approve final submissions.
