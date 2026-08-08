# DECISIONS.md — Veyra Decision Log

This file records implementation decisions that the PRD leaves open. It must not be used to override explicit PRD requirements.

---

## D-001 — Product Name

**Status:** Accepted  
**Date:** 2026-08-08

### Decision
Use **Veyra** as the repository/application name.

### Context
The supplied assignment title is "Virtual AI Assistant (Mini Alexa)". The project owner selected a distinct presentation name for the repository.

### Consequence
Documentation should mention the original assignment title for traceability, but user-facing branding should use Veyra.

---

## D-002 — Modular File Layout

**Status:** Accepted  
**Date:** 2026-08-08

### Decision
Use the PRD-recommended modular structure rather than a single `main.py` implementation.

### Rationale
The PRD explicitly permits either approach and recommends modules. The modular version better demonstrates maintainability and single responsibility without introducing unnecessary architecture.

---

## D-003 — No Third-Party Dependencies

**Status:** Accepted  
**Date:** 2026-08-08

### Decision
Use only Python standard-library modules.

### Rationale
The PRD requires offline portability and explicitly forbids multiple third-party ML/data libraries. Avoiding all third-party runtime packages makes compliance obvious.

---

## D-004 — Calculator Will Not Use `eval()`

**Status:** Accepted  
**Date:** 2026-08-08

### Decision
Parse the four supported arithmetic operators explicitly.

### Rationale
`eval()` would be unnecessary, unsafe, and harder to explain than direct parsing for the required feature set.

---

## D-005 — Guessing Game Defaults

**Status:** Accepted as initial default  
**Date:** 2026-08-08

### Decision
Prefer a target range of **1–20** with **5 attempts**.

### Source basis
The PRD sample interaction uses those values. The functional requirement itself only mandates a fixed range and limited attempts.

### Consequence
Use named constants so the values are explicit and easy to change if the mentor specifies otherwise.

---

## D-006 — Recommendation Command

**Status:** Accepted as implementation convention  
**Date:** 2026-08-08

### Decision
Use `activity` as the canonical command and allow `recommend` as a simple alias.

### Context
The PRD requires a rule-based recommendation feature but does not prescribe its command word.

---

## D-007 — Perceptron Command

**Status:** Accepted as implementation convention  
**Date:** 2026-08-08

### Decision
Use `perceptron` as the canonical command and optionally `neuron` as an alias.

### Rationale
The command maps directly to the concept named in the PRD and makes the feature discoverable in `help`.

---

## D-008 — Perceptron Constants

**Status:** Pending implementation detail  
**Date:** 2026-08-08

### Decision
The exact fixed weights and bias will be selected during implementation, centralized as named constants, and documented in this file once chosen.

### Constraint
The values must remain fixed; there is no training or parameter update.

---

## D-009 — Automated Testing

**Status:** Accepted  
**Date:** 2026-08-08

### Decision
Manual acceptance testing is mandatory. Standard-library `unittest` may be added for pure logic if useful, but it is optional.

### Rationale
The PRD explicitly specifies manual testing and does not require an external test framework.

---

## D-010 — Blank Name Handling

**Status:** Accepted
**Date:** 2026-08-08

### Decision
If the startup name input is blank or whitespace-only, Veyra will ask again
until the user enters a non-blank name.

### Rationale
Re-prompting keeps the captured session name truthful and avoids inventing a
name or allowing an unusable blank value. The value remains in memory only for
the current process.

---

## D-011 — Date and Time Display Formats

**Status:** Accepted
**Date:** 2026-08-08

### Decision
Display the local date as `Weekday, Month DD, YYYY` and the local time using a
12-hour clock as `HH:MM AM/PM`.

### Rationale
These formats are readable in a terminal, match the style shown in the project
examples, and make the date and time unambiguous without adding locale or
configuration complexity.

---

## D-012 — Calculator Numeric and Result Formatting

**Status:** Accepted
**Date:** 2026-08-08

### Decision
Accept signed integer and decimal operands in the documented space-delimited
calculator syntax. Display mathematically whole results without a trailing
`.0`; retain decimal notation for non-whole results.

### Rationale
This keeps common terminal results concise while supporting the PRD's basic
arithmetic examples and simple decimal input without expanding into arbitrary
expression parsing.
