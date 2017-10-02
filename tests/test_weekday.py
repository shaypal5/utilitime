"""Testing the lazy_property decorator."""

from utilitime.weekday import (
    next_weekday,
    prev_weekday,
    workdays,
    weekdays,
)


WEEKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

ISRAEL_WEEKDAYS = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]

US_WORKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]

ISRAEL_WORKDAYS = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
]

def test_next_weekday():
    """Basic test of the next_weekday function."""
    for i in range(0, 6):
        assert next_weekday(WEEKDAYS[i]) == WEEKDAYS[i+1]
    assert next_weekday(WEEKDAYS[6]) == WEEKDAYS[0]


def test_prev_weekday():
    """Basic test of the prev_weekday function."""
    for i in range(1, 7):
        assert prev_weekday(WEEKDAYS[i]) == WEEKDAYS[i-1]
    assert prev_weekday(WEEKDAYS[0]) == WEEKDAYS[6]


def test_workdays():
    """Basic test of the prev_weekday function."""
    assert workdays() == US_WORKDAYS
    assert workdays('Monday') == US_WORKDAYS
    assert workdays('monday') == US_WORKDAYS
    assert workdays('Sunday') == ISRAEL_WORKDAYS
    assert workdays('sunday') == ISRAEL_WORKDAYS


def test_weekdays():
    """Basic test of the weekdays function."""
    assert weekdays() == WEEKDAYS
    assert weekdays('Monday') == WEEKDAYS
    assert weekdays('monday') == WEEKDAYS
    assert weekdays('Sunday') == ISRAEL_WEEKDAYS
    assert weekdays('sunday') == ISRAEL_WEEKDAYS
