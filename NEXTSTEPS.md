# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Governance bootstrap complete; application implementation not yet started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Create the PRD-recommended application modules:
   - `main.py`
   - `greetings.py`
   - `datetime_utils.py`
   - `calculator.py`
   - `content.py`
   - `game.py`
   - `ai_concepts.py`
   - `help_menu.py`
   - `README.md`
2. Implement Phase 1 from `STEPS.md`: startup greeting, name capture, command loop, fallback, and exit.
3. Run the Phase 1 tests from `TESTING.md`.
4. Update `STATUS.md` only after those tests pass.
5. Continue through phases in `STEPS.md` without adding out-of-scope features.

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
