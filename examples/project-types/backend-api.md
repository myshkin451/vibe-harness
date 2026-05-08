# Project Plan: Backend API

## Product

Build a backend API that accepts visit notes, extracts structured follow-up tasks, and exposes them to an internal dashboard.

## Users

- internal operators
- dashboard frontend
- future agents debugging API behavior

## Stage

Prototype with real integration risk.

## Stack Preference

Python or TypeScript API, SQLite/Postgres locally, simple OpenAPI documentation.

## Definition Of Done

- API endpoint accepts a sample note
- structured task output is deterministic enough to test
- OpenAPI or route docs are available
- local test command exists
- one sample request/response is committed

## Risks

- unclear request/response contract
- no golden samples for agent-generated changes
- hidden assumptions about auth, tenancy, or data retention

## Human Decisions

- API contract naming
- data retention rules
- deployment target
- whether output is customer-facing

## Recommended Harness Depth

Working. Add `docs/architecture.md`, sample payloads, and an exec-plan template if multiple agents will touch API, storage, and dashboard code.
