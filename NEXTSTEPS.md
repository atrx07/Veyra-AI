# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Phase 4 random content features complete; Phase 5 not started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Implement Phase 5 from `STEPS.md`:
   - named constants for the 1–20 range and five-attempt limit
   - standard-library random target generation
   - nested game input loop with numeric and range validation
   - higher/lower hints, win handling, and attempt exhaustion
   - return to the main command loop after the game ends
   - `game` routing in `main.py`
2. Run T17 through T23 from `TESTING.md`, including deterministic development checks for both hint directions and attempt exhaustion.
3. Update `STATUS.md` only for behavior that passes its acceptance path.
4. Update this queue to Phase 6 after reporting the Phase 5 results.
5. Do not implement the help menu or any later feature during Phase 5.

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
