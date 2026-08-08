# GOVERNANCE_INDEX.md — Veyra Governance Map

## Start Here

This directory is a pre-implementation governance/reference pack for **Veyra**, built from the supplied internship PRD for **Virtual AI Assistant (Mini Alexa)**.

For a coding agent, the first file to read is `AGENTS.md`.

---

## File Map

| File | Purpose |
|---|---|
| `AGENTS.md` | Highest-level Codex execution contract, scope guardrails, Definition of Done |
| `PROJECT.md` | Product identity, vision, goals, non-goals, user-facing positioning |
| `REQUIREMENTS.md` | Detailed FR-01–FR-14 and non-functional requirements |
| `ARCHITECTURE.md` | Module boundaries, control flow, state/dependency model |
| `COMMAND_SPEC.md` | Supported commands, aliases, normalization, routing precedence |
| `TESTING.md` | Canonical 32-case manual acceptance matrix and NFR checks |
| `STEPS.md` | Ordered implementation phases |
| `NEXTSTEPS.md` | Immediate work queue for the current development state |
| `STATUS.md` | Requirement-by-requirement implementation and verification status |
| `DECISIONS.md` | Explicit decisions where the PRD leaves behavior open |
| `CODE_STANDARDS.md` | Python coding, naming, error-handling, and simplicity rules |
| `docs/PRD_TRACEABILITY.md` | Maps source PRD requirements to files/tests |
| `docs/AI_ML_DL_REFERENCE.md` | Technically accurate explanation of the assignment's AI/ML/DL concepts |

---

## Recommended Codex Entry Instruction

When handing the repository to Codex, the owner can simply instruct it to:

```text
Read AGENTS.md and all governance/reference files it points to. Build Veyra according to the current NEXTSTEPS.md. Treat the supplied PRD and governance files as authoritative. Do not add out-of-scope capabilities. Update STATUS.md, NEXTSTEPS.md, and DECISIONS.md as required by AGENTS.md while you work.
```

The agent should not need a second project-specification prompt after reading this pack.

---

## Governance Principle

The purpose of these files is not to make Veyra architecturally complicated. The application should remain small. The governance is detailed so the **agent's decisions are constrained**, not so the runtime architecture becomes large.
