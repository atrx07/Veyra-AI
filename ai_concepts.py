"""Provide Veyra's rule-based recommendation and perceptron demonstrations."""

from datetime import datetime


MORNING_START = 5
AFTERNOON_START = 12
EVENING_START = 17
NIGHT_START = 21


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
