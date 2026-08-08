# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Phase 1 session startup complete; Phase 2 not started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Implement Phase 2 from `STEPS.md`:
   - local date formatting in `datetime_utils.py`
   - local time formatting in `datetime_utils.py`
   - `date` and `time` command routing in `main.py`
2. Run T05 and T06 from `TESTING.md` against the machine's local date and time.
3. Update `STATUS.md` only for behavior that passes its acceptance path.
4. Update this queue to Phase 3 after reporting the Phase 2 results.
5. Do not implement calculator or any later feature during Phase 2.

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
