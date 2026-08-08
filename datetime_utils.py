"""Provide local date and time formatting helpers for Veyra."""

from datetime import datetime


DATE_FORMAT = "%A, %B %d, %Y"
TIME_FORMAT = "%I:%M %p"


def get_current_date():
    """Return the machine's current local date in a readable format."""
    return datetime.now().strftime(DATE_FORMAT)


def get_current_time():
    """Return the machine's current local time in a readable format."""
    return datetime.now().strftime(TIME_FORMAT)
