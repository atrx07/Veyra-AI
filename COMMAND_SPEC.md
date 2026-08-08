# COMMAND_SPEC.md — Veyra Input and Intent Contract

## 1. Purpose

Veyra uses explicit keyword/pattern rules, not natural-language understanding. This file defines the supported command surface so routing behavior remains predictable.

The agent may support modest phrase variation, but must not create a large pseudo-NLP system.

---

## 2. Normalization

Before intent checks, top-level input should normally be:

1. stripped of leading/trailing whitespace
2. converted to lowercase for matching

Preserve the original string only if a feature needs it for parsing/display.

Example:

```text
"   TiMe   " -> "time"
```

---

## 3. Canonical Commands

### Help
Canonical:

```text
help
```

Optional obvious variants:

```text
commands
what can you do
```

---

### Time
Canonical:

```text
time
```

Supported natural variants may include:

```text
what time is it
current time
```

Avoid matching unrelated words containing `time` as a substring if simple token matching can prevent it.

---

### Date
Canonical:

```text
date
```

Possible variants:

```text
today's date
current date
what is the date
```

---

### Calculator
Canonical syntax:

```text
calculate 12 + 8
calculate 5 / 2
```

Required operators:

```text
+  -  *  /
```

If the user enters only `calculate`, respond with usage guidance rather than crash.

Suggested guidance:

```text
Veyra: Try: calculate 12 + 8
```

Do not add exponentiation, parentheses, arbitrary expressions, or `eval()` unless the project owner explicitly expands scope.

---

### Quote
Canonical:

```text
quote
```

Possible variant:

```text
motivate me
```

---

### Joke
Canonical:

```text
joke
```

Possible variant:

```text
tell me a joke
```

---

### Fact
Canonical:

```text
fact
```

Possible variant:

```text
random fact
```

---

### Number Guessing Game
Canonical:

```text
game
```

Possible variants:

```text
guess
number game
```

Once inside the game, raw numeric guesses belong to the game loop and should not be passed back through global intent routing.

---

### Rule-Based Recommendation
Canonical recommendation command chosen for Veyra:

```text
activity
```

Supported alias:

```text
recommend
```

Expected result: a time-of-day-based activity suggestion using explicit conditions.

This canonical naming is an implementation convention because the PRD defines the feature but not a mandatory command word.

---

### Perceptron Demo
Canonical:

```text
perceptron
```

Possible alias:

```text
neuron
```

The feature should prompt for the required 2–3 numeric inputs, show a concise educational result, then return to the main loop.

---

### Exit
Required recognized aliases from the PRD feature description:

```text
exit
quit
bye
```

Exit should be checked before generic conversational/greeting matching.

---

## 4. Optional Greeting Intent

The PRD requires a startup greeting, not necessarily a reusable `hello` command. If the agent implements conversational greetings such as `hi`, `hello`, or `hey`, keep them lightweight and do not let them interfere with required intents.

This optional greeting must not be counted as a substitute for any FR.

---

## 5. Recommended Routing Precedence

To reduce accidental collisions:

1. exit
2. help
3. calculator
4. game
5. perceptron
6. recommendation/activity
7. time
8. date
9. quote
10. joke
11. fact
12. optional greeting
13. fallback

Reasoning:
- stateful/nested commands are handled early
- calculator syntax is distinctive
- educational commands are explicit
- content commands are simple keywords
- fallback remains final

---

## 6. Fallback Contract

Any unmatched top-level input should produce a friendly recovery response and continue.

Canonical style:

```text
Veyra: I'm not sure I understood that. Type 'help' to see what I can do.
```

The exact wording may vary.

---

## 7. Blank Input

Blank or whitespace-only input is invalid but harmless.

Recommended response:

```text
Veyra: I didn't get a command. Type 'help' to see the options.
```

Do not terminate or throw.

---

## 8. Parsing Philosophy

Veyra is rule-based by design. Do not chase every possible English phrasing.

A reasonable command that falls through to fallback is an acceptable limitation of the assignment and should be discussed as such. The PRD explicitly recognizes overly literal keyword matching as an acceptable limitation rather than something to fix with external NLP libraries.
