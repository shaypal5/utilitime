"""Weekday-related utility functions."""

from decore import lazy_property

from ..constants import (
    WEEKDAYS,
)


# === weekday-related functions ===

def next_weekday(weekday):
    """Returns the name of the weekday after the given weekday name."""
    ix = WEEKDAYS.index(weekday)
    if ix == len(WEEKDAYS)-1:
        return WEEKDAYS[0]
    return WEEKDAYS[ix+1]


def prev_weekday(weekday):
    """Returns the name of the weekday before the given weekday name."""
    ix = WEEKDAYS.index(weekday)
    if ix == 0:
        return WEEKDAYS[len(WEEKDAYS)-1]
    return WEEKDAYS[ix-1]


@lazy_property
def _lower_weekdays():
    return [day.lower() for day in WEEKDAYS]


@lazy_property
def _double_weekdays():
    return WEEKDAYS + WEEKDAYS


def workdays(first_day=None):
    """Returns a list of workday names.

    Arguments
    ---------
    first_day : str, default None
        The first day of the five-day work week. If not given, 'Monday' is
        used.

    Returns
    -------
    list
        A list of workday names.
    """
    if first_day is None:
        first_day = 'Monday'
    ix = _lower_weekdays().index(first_day.lower())
    return _double_weekdays()[ix:ix+5]


def weekdays(first_day=None):
    """Returns a list of weekday names.

    Arguments
    ---------
    first_day : str, default None
        The first day of the week. If not given, 'Monday' is used.

    Returns
    -------
    list
        A list of weekday names.
    """
    if first_day is None:
        first_day = 'Monday'
    ix = _lower_weekdays().index(first_day.lower())
    return _double_weekdays()[ix:ix+7]
