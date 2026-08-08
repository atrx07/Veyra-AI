# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Phase 2 date and time complete; Phase 3 not started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Implement Phase 3 from `STEPS.md`:
   - safe calculator expression parsing without `eval()` or `exec()`
   - addition, subtraction, multiplication, and division
   - malformed/non-numeric input handling and usage guidance
   - division-by-zero and unsupported-operator recovery
   - `calculate ...` routing in `main.py`
2. Run T07 through T13 from `TESTING.md` plus an explicit unsupported-operator check required by `AGENTS.md`.
3. Update `STATUS.md` only for behavior that passes its acceptance path.
4. Update this queue to Phase 4 after reporting the Phase 3 results.
5. Do not implement random content or any later feature during Phase 3.

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
