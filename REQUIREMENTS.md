# REQUIREMENTS.md — Veyra Requirements Baseline

## 1. Authority

This file is a structured implementation baseline derived from the supplied internship PRD for **Virtual AI Assistant (Mini Alexa)**. It does not replace the PRD. Its purpose is to make the requirements directly actionable for coding agents.

All PRD functional requirements FR-01 through FR-14 must be present in the final deliverable because the PRD success criteria require all 14 to be demonstrable.

---

## 2. Functional Requirements

### FR-01 — Startup Greeting

**Requirement:** Veyra shall greet the user on startup and ask for their name.

**Implementation expectation:**
- This occurs before entering the main command loop.
- The prompt clearly requests a name.

**Acceptance evidence:**
- Starting `main.py` visibly produces a greeting and name prompt.

---

### FR-02 — Session Name Memory

**Requirement:** Veyra shall remember the user's name for the current session and use it in later responses.

**Implementation expectation:**
- Store the supplied name only in memory.
- No file/database persistence.
- Reuse the name naturally in at least two later responses, matching the PRD acceptance test.

**Acceptance evidence:**
- User name is reused after startup and again in another later response, such as goodbye.
- Restarting Veyra requires the name again.

---

### FR-03 — Current Date

**Requirement:** Veyra shall display the current date on request.

**Implementation expectation:**
- Use the Python standard library `datetime` functionality.
- Use the machine's current local date.

**Acceptance evidence:**
- A date request returns the correct current date.

---

### FR-04 — Current Time

**Requirement:** Veyra shall display the current time on request.

**Implementation expectation:**
- Use `datetime` or equivalent standard-library time functionality.
- Use the machine's current local time.

**Acceptance evidence:**
- A time request returns a correct current-time representation.

---

### FR-05 — Basic Arithmetic

**Requirement:** Veyra shall perform addition, subtraction, multiplication, and division.

**Minimum supported expression shape:**

```text
calculate <number> <operator> <number>
```

Supported operators:

```text
+  -  *  /
```

**Implementation rules:**
- Do not use `eval()` or `exec()`.
- Parse operands safely.
- Handle integer and decimal numeric input if implementation remains simple.
- Handle division by zero with a friendly message.
- Handle malformed/non-numeric input without a crash.

**Acceptance evidence:**
- Correct result for all four operators.
- Divide-by-zero is non-fatal.

---

### FR-06 — Motivational Quote

**Requirement:** Veyra shall return a random motivational quote from a predefined list.

**Implementation expectation:**
- Store multiple strings in a local Python list/tuple.
- Use `random` from the standard library.

**Acceptance evidence:**
- Repeated requests produce at least two distinct values over a reasonable sample, consistent with the PRD acceptance test.

---

### FR-07 — Joke

**Requirement:** Veyra shall return a random joke from a predefined list.

**Implementation expectation:** Same pattern as FR-06.

**Acceptance evidence:** Repeated requests show variation.

---

### FR-08 — Random Fact

**Requirement:** Veyra shall return a random fact from a predefined list.

**Implementation expectation:**
- Facts should be accurate and general-audience appropriate.
- Keep content local; no online lookup.

**Acceptance evidence:** Repeated requests show variation.

---

### FR-09 — Number Guessing Game

**Requirement:** Veyra shall support a number-guessing game with a limited number of attempts.

**Required behavior:**
- Generate a random target within a fixed documented range.
- Tell the user the range.
- Tell the user the attempt limit.
- Accept guesses.
- Report `higher` or `lower` appropriately.
- End immediately on a correct guess.
- End when attempts are exhausted.
- Invalid input must not crash the application.

**Preferred constants from the PRD example:**
- range: 1 through 20 inclusive
- attempts: 5

These are sample-derived implementation defaults, not separately stated FR text. If changed, update `DECISIONS.md` and tests.

---

### FR-10 — Help Menu

**Requirement:** Veyra shall display a help menu listing all supported commands.

**Required help coverage:**
- time
- date
- calculate
- quote
- joke
- fact
- game
- recommendation/activity demo
- perceptron demo
- help
- exit

If user-visible aliases are intentionally supported, the help menu may mention them without becoming cluttered.

**Acceptance evidence:** Every supported feature can be discovered from help.

---

### FR-11 — Graceful Exit

**Requirement:** Veyra shall exit cleanly on an exit/quit command.

**Required aliases:**
- `exit`
- `quit`
- `bye`

**Acceptance evidence:**
- A goodbye message is printed.
- The main loop terminates without an exception.

---

### FR-12 — Unknown Input Fallback

**Requirement:** Veyra shall respond to unrecognized input with a friendly fallback rather than crashing.

**Expected behavior:**
- Blank/unknown text returns a short recovery hint.
- Recommend `help` when useful.
- Continue the main loop.

**Acceptance evidence:** Arbitrary input such as `asdkfj` produces fallback output and a new prompt.

---

### FR-13 — Rule-Based Recommendation Demo

**Requirement:** Veyra shall include at least one educational rule-based decision demonstration.

The PRD's example recommends an activity based on time of day using `if/elif/else`.

**Implementation baseline:**
- Use current local hour.
- Map hour bands to simple activity suggestions.
- Keep rules explicit and easy to explain.

**Testing consideration:**
- Structure the underlying function so different hour values can be checked without waiting for the clock, while the user-facing command may use the current hour.

**Acceptance evidence:** Different time bands lead to different recommendations.

---

### FR-14 — Simplified Perceptron Demo

**Requirement:** Veyra shall include a non-trained perceptron calculation demonstrating:

- numeric inputs
- fixed weights
- bias
- weighted sum
- simple step activation
- output `0` or `1`

**Implementation rules:**
- Use 2 or 3 user-provided numeric inputs.
- Use documented fixed weights and bias.
- No training.
- No external numeric/ML libraries.
- Clearly label this as an educational demo.

**Recommended output explanation:** Show the values conceptually enough that the user can see how the result was produced without flooding the terminal.

**Acceptance evidence:** Valid inputs produce only `0` or `1`; invalid numeric input is handled safely.

---

## 3. Non-Functional Requirements

### NFR-01 — Usability

Prompts and help text must be understandable to a first-time user.

Agent interpretation:
- consistent prompt style
- concise examples where parsing format matters
- clear error recovery

---

### NFR-02 — Reliability

Invalid input must not crash the program.

At minimum this includes:
- divide by zero
- non-numeric calculator input
- invalid guessing-game input
- malformed commands
- unrecognized top-level input

---

### NFR-03 — Portability

Veyra must run on any machine with standard Python 3 installed, with no internet required.

Therefore:
- no third-party runtime dependency
- no OS-specific shell commands in application logic
- no required environment variables

---

### NFR-04 — Maintainability

Code must be organized into clearly named functions with single responsibilities.

Prefer the PRD module split. Avoid giant command-handling functions where a feature deserves its own module function.

---

### NFR-05 — Performance

Responses must appear immediately.

Therefore:
- no artificial `sleep()`
- no unnecessary long-running loops
- no network wait
- no simulated typing effect

---

### NFR-06 — Documentation

Code must include comments/docstrings explaining major functions and any AI/ML/DL concept they demonstrate.

Documentation must distinguish actual behavior from analogy.

---

## 4. Explicit Out-of-Scope Requirements

The following are forbidden under the source PRD:

- real ML training/inference
- external datasets
- CSV/Excel/database dependency
- APIs/network calls/cloud services
- speech recognition
- text-to-speech
- voice/audio I/O
- TensorFlow
- PyTorch
- Keras
- scikit-learn
- OpenCV
- pandas
- NumPy
- persistence between sessions
- multi-user support
- multi-threaded/networked operation
- GUI

These restrictions are acceptance constraints, not enhancement suggestions.

---

## 5. Success Criteria

The project is considered submission-ready when:

1. FR-01 through FR-14 are demonstrable.
2. At least 20 manual test inputs have been executed without crashing the program.
3. The developer can explain the AI/ML/DL mapping in their own words.
4. Code is organized and commented.
5. Unexplained magic values are absent.
6. README/setup instructions are complete.
7. The app runs offline on Python 3.
