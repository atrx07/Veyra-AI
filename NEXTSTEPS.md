# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Phase 6 help menu complete; Phase 7 not started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Implement Phase 7 from `STEPS.md`:
   - explicit time-of-day `if/elif/else` recommendation rules
   - current-local-hour behavior for the user-facing command
   - an optional hour parameter for deterministic testing
   - concise documentation explaining handwritten rule-based decisions
   - `activity` and `recommend` routing in `main.py`
2. Run T29 and T30 from `TESTING.md`, checking the current-hour route and at least one different hour band.
3. Update `STATUS.md` only for behavior that passes its acceptance path.
4. Update this queue to Phase 8 after reporting the Phase 7 results.
5. Do not implement the perceptron or any later feature during Phase 7.

---

## Agent Reminder

Before coding, read `AGENTS.md` and `REQUIREMENTS.md`.

Do not interpret "Virtual AI Assistant" as permission to add an LLM, API, ML package, GUI, persistence, speech, or networking. The assignment explicitly forbids those additions.

---

## Completion Rule

When a phase is finished:

- remove it from the immediate queue,
- add the next phase,
- keep this file short,
- record completion state in `STATUS.md` rather than turning this into a changelog.
