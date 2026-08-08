"""Provide Veyra's rule-based recommendation and perceptron demonstrations."""

from datetime import datetime


MORNING_START = 5
AFTERNOON_START = 12
EVENING_START = 17
NIGHT_START = 21
PERCEPTRON_WEIGHTS = (0.6, -0.4)
PERCEPTRON_BIAS = -0.1
ACTIVATION_THRESHOLD = 0.0


def recommend_activity(hour=None):
    """Return a handwritten time-band recommendation; no model is trained."""
    if hour is None:
        hour = datetime.now().hour

    if not 0 <= hour <= 23:
        raise ValueError("Hour must be from 0 through 23.")

    if MORNING_START <= hour < AFTERNOON_START:
        return "Morning is a good time for a short walk or planning your day."
    if AFTERNOON_START <= hour < EVENING_START:
        return "This afternoon is a good time for focused study or project work."
    if EVENING_START <= hour < NIGHT_START:
        return "This evening could be a good time for exercise or a hobby."
    return "This is a good time to wind down with some quiet reading."


def calculate_weighted_sum(inputs):
    """Return the fixed weighted sum used by Veyra's perceptron demo."""
    if len(inputs) != len(PERCEPTRON_WEIGHTS):
        raise ValueError(
            f"The perceptron requires {len(PERCEPTRON_WEIGHTS)} inputs."
        )

    products = (
        value * weight
        for value, weight in zip(inputs, PERCEPTRON_WEIGHTS)
    )
    return sum(products) + PERCEPTRON_BIAS


def perceptron(inputs):
    """Apply a fixed weighted sum and step activation; no training occurs."""
    weighted_sum = calculate_weighted_sum(inputs)
    return 1 if weighted_sum > ACTIVATION_THRESHOLD else 0


def perceptron_demo():
    """Prompt for two numeric inputs and display the educational calculation."""
    print("Veyra: This perceptron demo uses fixed values and does not train.")
    print(
        f"Veyra: Weights = {PERCEPTRON_WEIGHTS}; "
        f"bias = {PERCEPTRON_BIAS}."
    )

    inputs = []
    for input_number in range(1, len(PERCEPTRON_WEIGHTS) + 1):
        try:
            value = float(input(f"You (input {input_number}): ").strip())
        except ValueError:
            print(
                "Veyra: Please enter numeric values. "
                "Returning to the main menu."
            )
            return
        inputs.append(value)

    weighted_sum = calculate_weighted_sum(inputs)
    output = perceptron(inputs)
    print(f"Veyra: Weighted sum = {weighted_sum:.2f}.")
    print(f"Veyra: Step activation output = {output}.")
    print("Veyra: The fixed weights were not learned or updated.")
