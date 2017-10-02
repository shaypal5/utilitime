"""Weekday-related utility functions."""

from .weekday import (
    next_weekday,
    prev_weekday,
    workdays,
    weekdays
)
try:
    del weekday
except NameError: # pragma: no cover
    pass
