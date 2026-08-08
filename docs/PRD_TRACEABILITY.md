# PRD_TRACEABILITY.md — Source-to-Implementation Map

## 1. Purpose

This file maps the supplied internship PRD to Veyra's planned implementation and verification artifacts. It allows a coding agent or reviewer to see that the project remains requirement-driven.

---

## 2. Functional Traceability

| PRD ID | Source requirement summary | Planned owner | Primary verification |
|---|---|---|---|
| FR-01 | Greet on startup and ask name | `greetings.py`, `main.py` | T01 |
| FR-02 | Remember name during session and reuse it | `main.py`, greeting/output helpers | T02–T04 |
| FR-03 | Display current date | `datetime_utils.py` | T05 |
| FR-04 | Display current time | `datetime_utils.py` | T06 |
| FR-05 | +, -, *, / calculator | `calculator.py` | T07–T13 |
| FR-06 | Random motivational quote | `content.py` | T14 |
| FR-07 | Random joke | `content.py` | T15 |
| FR-08 | Random fact | `content.py` | T16 |
| FR-09 | Limited-attempt number guessing game | `game.py` | T17–T23 |
| FR-10 | Help listing supported commands | `help_menu.py` | T24 |
| FR-11 | Graceful exit | `main.py` | T04, T27, T28 |
| FR-12 | Friendly unknown-input fallback | `main.py` | T25, T26 |
| FR-13 | Rule-based recommendation demo | `ai_concepts.py` | T29, T30 |
| FR-14 | Simplified fixed-weight perceptron | `ai_concepts.py` | T31, T32 |

---

## 3. Non-Functional Traceability

| PRD category | Source expectation | Governance/implementation control |
|---|---|---|
| Usability | Clear prompts/help | `COMMAND_SPEC.md`, README, help menu |
| Reliability | Invalid input must not crash | feature-level validation + `TESTING.md` |
| Portability | Standard Python 3, offline | `AGENTS.md` dependency lock |
| Maintainability | Clear single-responsibility functions | `ARCHITECTURE.md` module ownership |
| Performance | Immediate responses | no network, no artificial delays |
| Documentation | Major functions/concepts explained | README + docstrings/comments |

---

## 4. PRD System Features to Files

| PRD system feature | Veyra implementation |
|---|---|
| Greeting & Name Capture | `greetings.py` |
| Date & Time Reporting | `datetime_utils.py` |
| Basic Calculator | `calculator.py` |
| Motivational Quote Generator | `content.py` |
| Joke Generator | `content.py` |
| Random Fact Generator | `content.py` |
| Number Guessing Game | `game.py` |
| Help Menu | `help_menu.py` |
| Graceful Exit | `main.py` |
| Conceptual ML/DL Demonstrations | `ai_concepts.py` |

---

## 5. PRD Workflow Mapping

Source workflow:

```text
User Input
   -> normalize text
   -> keyword/pattern match
   -> matched feature function OR fallback
   -> print response
   -> loop
```

Veyra retains that structure directly. It does not introduce model inference or external routing.

---

## 6. PRD Acceptance Highlights

The source PRD specifically expects:

- name reuse in at least two later responses
- correct current date/time
- correct arithmetic and safe divide-by-zero handling
- varying quote/joke/fact results across repeated calls
- correct guessing-game higher/lower hints and attempt limit
- complete help listing
- clean exit
- fallback that leaves the program running

`TESTING.md` encodes each of these as explicit manual cases.

---

## 7. Source-Specified Technology Restrictions

The source PRD places the following outside scope:

- real ML model training or inference
- external datasets
- CSV/Excel/database requirements
- external APIs
- OpenAI/Gemini-style services
- cloud services
- speech recognition/TTS
- voice/audio I/O
- TensorFlow/PyTorch/Keras/scikit-learn/OpenCV/pandas/NumPy
- persistent storage
- multi-user/threaded/networked operation

Veyra's `AGENTS.md` promotes these restrictions to hard agent guardrails.

---

## 8. Naming Note

Source PRD product title: **Virtual AI Assistant (Mini Alexa)**.  
Repository/application presentation name: **Veyra**.

The rename does not alter feature or acceptance requirements.
