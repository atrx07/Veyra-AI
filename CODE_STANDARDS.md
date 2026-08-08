# CODE_STANDARDS.md — Veyra Python Standards

## 1. Primary Rule

Write Python that a beginner intern can explain line by line while still meeting a professional code-quality baseline.

Clarity wins over cleverness.

---

## 2. Language and Runtime

- Python 3.x
- Standard library only
- No third-party runtime packages
- No network access
- No platform-specific requirement

---

## 3. Naming

Use descriptive `snake_case` for functions and variables.

Good:

```python
get_current_time()
play_guessing_game()
weighted_sum
max_attempts
```

Avoid vague names:

```python
do_it()
x1()
data2
thing
```

Use `UPPER_SNAKE_CASE` for meaningful constants such as game bounds, attempt limits, fixed perceptron weights, and bias.

---

## 4. Functions

Each function should have one obvious responsibility.

Prefer:

```python
parse_expression(...)
calculate(...)
```

over one large function that parses, calculates, prints help, and catches every error at once.

Keep functions short enough to understand without excessive scrolling where practical.

---

## 5. Type Hints

Simple type hints are encouraged when they improve readability, but do not introduce complex typing machinery.

Acceptable:

```python
def get_current_time() -> str:
    ...
```

Avoid turning a beginner terminal project into a typing exercise.

---

## 6. Docstrings and Comments

Use docstrings/comments when they explain:

- a module responsibility
- a non-obvious parser rule
- error-handling behavior
- the rule-based AI demonstration
- perceptron inputs/weights/bias/activation
- why a named constant exists

Do not comment obvious statements.

Bad:

```python
# Add one to attempts
attempts += 1
```

Useful:

```python
# Fixed weights are intentional: this demo performs forward calculation only;
# it does not train or update parameters.
```

---

## 7. Input Handling

Normalize top-level commands predictably using operations such as:

```python
command = raw_input.strip().lower()
```

Feature-specific parsing belongs in the feature module.

Never trust numeric input to be valid. Convert inside `try/except ValueError` or equivalent explicit validation.

---

## 8. Exceptions

- Do not use bare `except:`.
- Catch expected exception types.
- Handle user mistakes locally.
- Do not suppress unexpected programming errors silently.

Calculator division-by-zero and numeric conversion failures must be handled explicitly.

---

## 9. Calculator Safety

Forbidden:

```python
eval(user_expression)
exec(...)
```

The calculator supports only the four PRD operators. Parse those operators deliberately.

---

## 10. Randomness

Use Python's `random` module for:

- quote selection
- joke selection
- fact selection
- guessing-game target

Do not add artificial randomness to required deterministic utilities such as date, time, arithmetic, or perceptron calculation.

---

## 11. Main Loop

`main.py` coordinates. It should not become the implementation location for every feature.

The routing chain should remain visible enough to demonstrate keyword/pattern matching and rule-based behavior to a mentor.

---

## 12. Output Style

Use consistent terminal labels such as:

```text
Veyra: ...
You: ...
```

Keep output concise and readable. Do not use terminal-control/color libraries or animated output that harms portability.

Unicode decoration is optional but should not be required for comprehension.

---

## 13. Magic Values

The PRD's success criteria require code to be free of unexplained magic values.

Use named constants for behavior-defining values, especially:

- guessing minimum/maximum
- maximum attempts
- perceptron weights
- perceptron bias
- time-of-day boundaries if they are not self-explanatory

---

## 14. Dependency Hygiene

Before final submission, inspect all imports.

Every runtime import must resolve to either:

- another Veyra module, or
- the Python standard library.

Do not add a package because it shortens a few lines of code.

---

## 15. Simplicity Guard

Before introducing an abstraction, ask:

> Does this make one of the required features easier to understand, test, or maintain?

If the answer is no, do not add it.
