# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Phase 5 number-guessing game complete; Phase 6 not started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Implement Phase 6 from `STEPS.md`:
   - complete supported-command list in `help_menu.py`
   - one-line descriptions and calculator syntax guidance
   - discovery for activity/recommendation and perceptron commands
   - exit aliases or primary exit guidance
   - `help` routing in `main.py`
2. Run T24 from `TESTING.md` and verify every required user-facing feature is listed.
3. Update `STATUS.md` only for behavior that passes its acceptance path.
4. Update this queue to Phase 7 after reporting the Phase 6 results.
5. Do not implement recommendation or any later feature during Phase 6.

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
