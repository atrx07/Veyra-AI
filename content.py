"""Provide Veyra's predefined quotes, jokes, facts, and random selection."""

import random


QUOTES = (
    "Small steps still move you forward.",
    "Progress begins when you decide to try.",
    "Consistency turns effort into improvement.",
    "Mistakes are evidence that you are learning.",
    "Focus on the next useful step.",
)

JOKES = (
    "Why did the computer get cold? It left its Windows open.",
    "Why was the math book sad? It had too many problems.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why do programmers prefer dark mode? Light attracts bugs.",
    "What did one wall say to the other? I'll meet you at the corner.",
)

FACTS = (
    "Earth takes about 365.25 days to orbit the Sun.",
    "An adult human skeleton typically has 206 bones.",
    "Water freezes at 0 degrees Celsius at standard atmospheric pressure.",
    "The Pacific Ocean is the largest ocean on Earth.",
    "Light travels faster than sound.",
)


def get_random_quote():
    """Return one motivational quote from Veyra's local collection."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return one general-audience joke from Veyra's local collection."""
    return random.choice(JOKES)


def get_random_fact():
    """Return one fact from Veyra's local collection."""
    return random.choice(FACTS)
