"""Timestamp-related utility functions."""

from datetime import datetime
import calendar

import pytz
from delorean import Delorean

from ..datetime import datetime_to_dateint


def timestamp_to_local_time(timestamp, timezone_name):
    """Convert epoch timestamp to a localized Delorean datetime object.

    Arguments
    ---------
    timestamp : int
        The timestamp to convert.
    timezone_name : datetime.timezone
        The timezone of the desired local time.

    Returns
    -------
    delorean.Delorean
        A localized Delorean datetime object.
    """
    # first convert timestamp to UTC
    utc_time = datetime.utcfromtimestamp(float(timestamp))
    delo = Delorean(utc_time, timezone='UTC')
    # shift d according to input timezone
    localized_d = delo.shift(timezone_name)
    return localized_d


def timestamp_to_local_time_str(
        timestamp, timezone_name, fmt="yyyy-MM-dd HH:mm:ss"):
    """Convert epoch timestamp to a localized datetime string.

    Arguments
    ---------
    timestamp : int
        The timestamp to convert.
    timezone_name : datetime.timezone
        The timezone of the desired local time.
    fmt : str
        The format of the output string.

    Returns
    -------
    str
        The localized datetime string.
    """
    localized_d = timestamp_to_local_time(timestamp, timezone_name)
    localized_datetime_str = localized_d.format_datetime(fmt)
    return localized_datetime_str


def get_timestamp(timezone_name, year, month, day, hour=0, minute=0):
    """Epoch timestamp from timezone, year, month, day, hour and minute."""
    tz = pytz.timezone(timezone_name)
    tz_datetime = tz.localize(datetime(year, month, day, hour, minute))
    timestamp = calendar.timegm(tz_datetime.utctimetuple())
    return timestamp


def timestamp_to_datetime(timestamp):
    """Converts a UTC timestamp to a UTC-aligned datetime object.

    Arguments
    ---------
    timestamp : int
        A UTC timestamp.

    Returns
    -------
    datetime.datetime
        A UTC-aligned datetime object corresponding to the given timestamp.
    """
    return datetime.utcfromtimestamp(timestamp)


def tz_aware_dt_from_timestamp_and_tz(timestamp, timezone_name):
    """Creates a timezone-aware datetime object from given timestamp and
    timezone."""
    return datetime.fromtimestamp(timestamp, timezone_name)


def timestamp_to_dateint(timestamp):
    """Converts a UTC timestamp to a dateint of the corresponding day.

    Arguments
    ---------
    timestamp : int
        A UTC timestamp.

    Returns
    -------
    int
        An integer object decipting the calendaric day - e.g. 20161225 -
        corresponding to the given timestamp.
    """
    return datetime_to_dateint(timestamp_to_datetime(timestamp))


_LEAP_YEAR_SINCE_EPOCH = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004,
                          2008, 2012, 2016]

_AVG_SEC_IN_YEAR = 365 * 24 * 60 * 60 + 5 * 60 * 60 + 48 * 60 + 45

# from ..constants import (SECONDS_IN_COMMON_YEAR, SECONDS_IN_LEAP_YEAR)

def _efficient_timestamp_to_dateint():
    #todo: use above constants
    pass
