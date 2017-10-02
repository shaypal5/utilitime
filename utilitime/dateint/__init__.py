"""Dateint-related utility functions."""

from .dateint import (
    decompose_dateint,
    dateint_to_date,
    tz_aware_dateint_to_timestamp,
    dateint_to_timestamp,
    dateint_to_utc_timestamp,
    dateint_to_datetime,
    dateint_to_weekday,
    dateint_to_weekday_name,
    shift_dateint,
    dateint_range,
    today_int,
    dateint_week_by_dateint,
    dateint_difference,
)
try:
    del dateint
except NameError: # pragma: no cover
    pass
