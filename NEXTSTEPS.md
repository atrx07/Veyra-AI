# NEXTSTEPS.md — Veyra Immediate Work Queue

## Current Stage

**Phase 7 rule-based recommendation complete; Phase 8 not started.**

This file should always represent the next concrete engineering actions, not a historical log.

---

## Next Actions

1. Implement Phase 8 from `STEPS.md`:
   - select and document fixed perceptron weights and bias
   - accept two or three numeric user inputs
   - calculate the weighted sum and step activation
   - return a binary output of `0` or `1`
   - recover safely from invalid numeric input
   - explain clearly that no training occurs
   - `perceptron` and optional `neuron` routing in `main.py`
2. Run T31 and T32 from `TESTING.md`, plus deterministic binary-output checks for both activation outcomes.
3. Update `STATUS.md` only for behavior that passes its acceptance path.
4. Mark Phase 8 complete in the README roadmap and update this queue to Phase 9 after reporting the results.
5. Do not perform Phase 9 UX polish or later work during Phase 8.

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
