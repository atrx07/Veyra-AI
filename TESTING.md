# TESTING.md — Veyra Verification and Acceptance Plan

## 1. Testing Goal

The supplied PRD requires the program to survive at least **20 manual test inputs**, including invalid input. Manual verification is therefore mandatory.

Optional standard-library automated tests may supplement this plan, but they do not replace it.

---

## 2. Test Environment

Record for final verification:

- Python version: Python 3.14.6
- Operating system: Windows 11 (10.0.26200)
- Date tested: 2026-08-08
- Tester: Codex

Expected launch command:

```bash
python main.py
```

If the environment requires `python3`, README may show both forms.

---

## 3. Mandatory Manual Test Matrix

### Startup and session state

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T01 | Launch program | Veyra greets user and asks for name | FR-01 |
| T02 | Enter `Alex` as name | Name is accepted and personalized welcome appears | FR-02 |
| T03 | Use a later feature after entering name | Name appears in at least one later response where designed | FR-02 |
| T04 | Exit session | Goodbye includes or otherwise reuses name; clean termination | FR-02, FR-11 |

### Date and time

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T05 | `date` | Correct local current date | FR-03 |
| T06 | `time` | Correct local current time | FR-04 |

### Calculator

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T07 | `calculate 12 + 8` | Result `20` or equivalent numeric formatting | FR-05 |
| T08 | `calculate 12 - 8` | Result `4` | FR-05 |
| T09 | `calculate 12 * 8` | Result `96` | FR-05 |
| T10 | `calculate 12 / 4` | Result `3` or `3.0` | FR-05 |
| T11 | `calculate 5 / 0` | Friendly division-by-zero error; app continues | FR-05, NFR-02 |
| T12 | `calculate cat + 2` | Friendly invalid-number/syntax error; app continues | FR-05, NFR-02 |
| T13 | `calculate` | Usage guidance; app continues | FR-05, NFR-01 |

Additional mandatory calculator validation from `AGENTS.md`:

- `calculate 2 ^ 3` produces a friendly unsupported-operator error and the app continues.

This additional governance check does not change the PRD-derived T01–T32 numbering.

### Random content

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T14 | Request `quote` 5+ times | At least two different list entries appear across repeats | FR-06 |
| T15 | Request `joke` 5+ times | At least two different list entries appear across repeats | FR-07 |
| T16 | Request `fact` 5+ times | At least two different list entries appear across repeats | FR-08 |

Randomness note: a random system can theoretically repeat the same result. If a 5-request check repeats by chance, retry rather than modifying logic solely to force non-repetition unless the owner wants that behavior.

### Guessing game

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T17 | `game` | Veyra announces range and attempt limit | FR-09 |
| T18 | Enter a valid wrong guess below target | Correct `higher` feedback | FR-09 |
| T19 | Enter a valid wrong guess above target | Correct `lower` feedback | FR-09 |
| T20 | Guess target | Game reports win and returns to main loop | FR-09 |
| T21 | Exhaust attempt limit | Game ends after limit and reports failure/target as designed | FR-09 |
| T22 | Enter non-numeric guess | Friendly validation; no crash | FR-09, NFR-02 |
| T23 | Enter out-of-range numeric guess | Friendly range validation; no crash | FR-09, NFR-01 |

For deterministic development testing, the implementation may expose a pure/helper path or allow temporary controlled random seeding, but user-facing behavior must remain random.

### Help, fallback, exit

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T24 | `help` | Lists all required user-facing features | FR-10 |
| T25 | `asdkfj` | Friendly fallback, then returns to prompt | FR-12 |
| T26 | blank input | Friendly recovery, no crash | FR-12, NFR-02 |
| T27 | `quit` | Clean goodbye and termination | FR-11 |
| T28 | `bye` | Clean goodbye and termination | FR-11 |

### AI concept demonstrations

| ID | Input / action | Expected result | FR |
|---|---|---|---|
| T29 | `activity` | Returns activity recommendation based on current hour rules | FR-13 |
| T30 | Call recommendation logic with an hour from another band during development | Different rule path is returned | FR-13 |
| T31 | `perceptron`, then valid numeric inputs | Shows valid fixed-weight calculation result of `0` or `1` | FR-14 |
| T32 | `perceptron`, then invalid input | Friendly numeric validation; no crash | FR-14, NFR-02 |

This matrix exceeds the PRD minimum of 20 manual inputs and should be used as the canonical acceptance pass.

---

## 4. Non-Functional Verification

### Portability

- [x] no third-party imports
- [x] no network calls
- [x] no OS-specific application requirement
- [x] starts with standard Python 3

### Maintainability

- [x] each feature has a clearly named function
- [x] modules match documented responsibilities
- [x] no giant feature logic dumped into `main.py`
- [x] important constants have names

### Performance

- [x] no `sleep()` used for decoration
- [x] command responses appear immediately

### Documentation

- [x] README run instructions work
- [x] help output matches implemented commands
- [x] AI/ML/DL concept comments are accurate
- [x] no documentation claims real learning/training

---

## 5. Suggested Optional Unit Tests

If automated tests are added, use Python `unittest` only unless scope changes.

Good candidates:

- `calculate()` for all four operators
- division-by-zero behavior
- parser success/failure cases
- recommendation hour boundaries
- perceptron binary output
- date/time return types/format sanity

Avoid complicated mocking infrastructure. Manual interactive behavior remains the priority.

---

## 6. Regression Rule

When a bug fix changes behavior:

1. add or update a test case in this file if the issue is user-visible,
2. rerun the affected feature tests,
3. rerun the full manual acceptance matrix before final submission,
4. update `STATUS.md`.

---

## 7. Final Test Record

```text
Final acceptance run: PASS
Date: 2026-08-08
Python: 3.14.6
OS: Windows 11 (10.0.26200)
Tests passed: 32 / 32
FR-01..FR-14 verified: YES
Third-party dependencies found: NO
Network use found: NO
Persistent state found: NO
Crashes during invalid-input tests: NO
Submission-ready: YES
Notes: The README run-through, module import, source-scope, portability,
maintainability, performance, help, and documentation audits all passed.
```

Execution coverage:

- T01–T16, T24–T26, T29, and T31 were exercised in a complete terminal session.
- T17–T23 used the interactive game with a deterministic target of `10`, as permitted by the matrix, to verify both hint directions, invalid inputs, winning, and attempt exhaustion.
- T27, T28, and T32 were exercised in separate fresh terminal sessions.
- T30 called the recommendation helper with morning and afternoon hours and confirmed different rule paths.
- The additional unsupported calculator operator check passed and returned control to the main prompt.
