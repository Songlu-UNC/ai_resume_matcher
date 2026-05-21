# Product Note: AI-Executed Candidate Matching Workflow

## What workflow step is the AI executing?

The prototype executes the middle of the Hiring Copilot workflow after candidates have already been sourced: JD understanding, candidate matching, recommendation generation, validation preparation, and submission-ready summary creation. It turns a job description and candidate profiles into structured recruiter-ready outputs.

## What should remain human-reviewed?

Final submission decisions should remain human-reviewed. Recruiters and account managers should validate resume evidence, check candidate risks, confirm ambiguous experience through follow-up questions, edit client-facing summaries, and decide whether the candidate should actually be submitted.

## How would recruiters use this output?

Recruiters would use the recommendation table for quick triage, then open each candidate detail view to review strengths, risks, validation questions, and a client-ready summary. Recruiting operations could use the same output for quality control before candidates are passed to an account manager or client HR.

## Assumptions

The candidates are already sourced. The prototype assumes the JD is the source of truth for evaluation criteria. It also assumes that a simple transparent scoring model is preferable for an assignment prototype because recruiters need to understand and challenge AI reasoning.

## Product and workflow tradeoffs

I prioritized clarity, explainability, and speed over complex automation. The app uses structured candidate data instead of live LLM calls so that results are deterministic, easy to demo, and recruiter-auditable. This makes the prototype less dynamic, but much easier to validate.

## What I would improve in V2

V2 would add PDF upload and parsing, LLM-based evidence extraction, configurable client-specific rubrics, recruiter feedback loops, bias/fairness checks, ATS/CRM export, confidence scoring, and audit logs showing exactly which resume lines supported each recommendation.
