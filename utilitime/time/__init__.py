"""datetime.time-related utility functions."""

from .time import (
    decompose_seconds_in_day,
    seconds_in_day_to_time,
    minutes_in_day_to_time,
)
try:
    del time
except NameError: # pragma: no cover
    pass
