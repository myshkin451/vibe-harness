# Project Plan: SaaS Tool

## Product

Build a small B2B SaaS tool that helps teams collect customer feedback, summarize themes, and turn them into prioritized action items.

## Users

- product managers
- customer success teams
- founders reviewing early feedback

## Stage

Prototype moving toward first usable workflow.

## Stack Preference

Full-stack TypeScript, simple database, auth later if not needed for the first local loop.

## Definition Of Done

- user can paste feedback into the app
- app stores feedback locally or in a simple database
- app shows grouped themes and candidate actions
- one local validation command exists
- manual browser walkthrough is documented

## Risks

- building billing/auth before the feedback loop works
- letting AI-generated summaries become untraceable
- unclear data boundaries and privacy assumptions

## Human Decisions

- target customer segment
- pricing and packaging
- privacy posture
- whether AI summaries can be shown externally

## Recommended Harness Depth

Working. SaaS work benefits from a short architecture doc, decision records for auth/data/privacy, and execution plans for multi-step features.
