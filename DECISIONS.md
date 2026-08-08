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

**Status:** Accepted
**Date:** 2026-08-08

### Decision
Use a target range of **1–20** with **5 attempts**.

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

**Status:** Accepted
**Date:** 2026-08-08

### Decision
Use two numeric inputs with fixed weights **0.6** and **-0.4**, fixed bias
**-0.1**, and a step activation that returns `1` only when the weighted sum is
greater than `0`; otherwise return `0`.

### Constraint
The values must remain fixed; there is no training or parameter update.

### Rationale
The small values make both activation outcomes easy to demonstrate by hand
while keeping the arithmetic readable for a beginner-level explanation.

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

---

## D-013 — Guessing Game Invalid-Input Attempts

**Status:** Accepted
**Date:** 2026-08-08

### Decision
Non-numeric and out-of-range guesses do not consume one of the five game
attempts. Only valid in-range whole-number guesses advance the attempt counter.

### Rationale
This keeps the attempt limit focused on actual guesses and lets a beginner
recover from typing mistakes without shortening the game.

---

## D-014 — Activity Recommendation Time Bands

**Status:** Accepted
**Date:** 2026-08-08

### Decision
Use four local-hour bands: night from 21:00 through 04:59, morning from 05:00
through 11:59, afternoon from 12:00 through 16:59, and evening from 17:00
through 20:59.

### Rationale
Four explicit bands make the handwritten rules easy to demonstrate and test
while providing meaningfully different suggestions without pretending to use a
trained recommendation model.
