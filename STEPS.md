# STEPS.md — Veyra Implementation Sequence

## 1. Purpose

This is the preferred build order for Codex or another coding agent. Work through the phases sequentially unless the repository already contains implementation that changes the starting point.

Each phase should leave the program runnable where practical.

---

## Phase 0 — Repository Bootstrap

### Tasks
- Create/confirm application files from `ARCHITECTURE.md`.
- Do not implement extra product features.
- Confirm Python 3 is available.
- Ensure no third-party package is required.
- Add a minimal README skeleton if none exists.

### Exit condition
- Repository structure is present.
- `python main.py` can at least start without import errors once the initial loop is added.

---

## Phase 1 — Session Startup

### Implement
- Veyra banner/title
- startup greeting
- name prompt
- in-memory name variable
- personalized welcome
- initial command loop shell
- clean fallback for blank/unknown command
- clean exit aliases

### Requirements
- FR-01
- FR-02 foundation
- FR-11
- FR-12 foundation

### Verify
- T01, T02, T25, T26, T27/T28

---

## Phase 2 — Date and Time

### Implement
- `datetime_utils.py`
- current local date function
- current local time function
- routing for `date` and `time`

### Requirements
- FR-03
- FR-04

### Verify
- T05, T06

---

## Phase 3 — Calculator

### Implement
- safe parser
- four operators
- clear syntax guidance
- divide-by-zero handling
- malformed/non-numeric handling
- route `calculate ...`

### Requirements
- FR-05
- NFR-02

### Mandatory rule
- no `eval()`

### Verify
- T07 through T13

---

## Phase 4 — Static Content Features

### Implement
- predefined quote collection
- predefined joke collection
- predefined fact collection
- random selection functions
- routes for `quote`, `joke`, `fact`

### Requirements
- FR-06
- FR-07
- FR-08

### Verify
- T14 through T16

---

## Phase 5 — Number Guessing Game

### Implement
- constants for range and attempts
- random target
- nested game input loop
- number validation
- range validation
- higher/lower hints
- win condition
- attempt exhaustion condition
- return to main Veyra loop

### Requirements
- FR-09

### Preferred defaults
- 1–20
- 5 attempts

### Verify
- T17 through T23

---

## Phase 6 — Help Menu

### Implement
- full list of commands
- one-line descriptions
- calculator syntax example
- activity/recommendation command
- perceptron command
- exit aliases or primary exit command

### Requirements
- FR-10

### Verify
- T24

---

## Phase 7 — Rule-Based AI Demonstration

### Implement
- explicit time-of-day `if/elif/else` decision
- current-hour user-facing route
- testable hour parameter/helper
- concise explanation/comment of rule-based decision-making

### Requirements
- FR-13

### Verify
- T29, T30

---

## Phase 8 — Perceptron Demonstration

### Implement
- fixed documented weights
- fixed documented bias
- 2 or 3 numeric user inputs
- weighted sum
- step activation
- binary output
- invalid-input recovery
- comments/docstring explaining that no training occurs

### Requirements
- FR-14

### Verify
- T31, T32

---

## Phase 9 — Name Reuse and UX Polish

### Implement/verify
- name appears in at least two later responses
- consistent `Veyra:` prompt/output style
- help wording matches actual routing
- no misleading claims of learning, browsing, or persistence
- no artificial delay

### Requirements
- FR-02 completion
- NFR-01
- NFR-05

### Verify
- T03, T04 plus exploratory session

---

## Phase 10 — Documentation

### Complete README
Include:
- project identity
- assignment traceability
- feature list
- Python requirement
- offline/no-dependency statement
- run instructions
- command examples
- file/module overview
- AI/ML/DL concept mapping
- limitations
- testing statement

### Requirements
- NFR-06
- PRD documentation expectation

---

## Phase 11 — Final Acceptance

### Execute
- full 32-case manual matrix in `TESTING.md`
- optional unit tests if present
- import/dependency audit
- scope audit against `AGENTS.md`
- README run-through from a clean terminal

### Update
- `STATUS.md`
- `NEXTSTEPS.md`
- `DECISIONS.md` if final choices changed

### Exit condition
All Definition-of-Done items in `AGENTS.md` are satisfied.
