"""Datetime-related utility functions."""

from datetime import datetime, timezone

import pytz
from decore import lazy_property

from ..constants import (
    SECONDS_IN_HOUR,
)


# === datetime-related functions ===

@lazy_property
def epoch_datetime():
    """Returns the epoch as a datetime.datetime object."""
    return datetime.utcfromtimestamp(0)


def utc_time():
    """Returns the current server time as a datetime object.

    This assumes all servers run in UTC time.
    """
    return datetime.utcnow()


def utc_offset_by_timezone(timezone_name):
    """Returns the UTC offset of the given timezone in hours.

    Arguments
    ---------
    timezone_name: str
        A string with a name of a timezone.

    Returns
    -------
    int
        The UTC offset of the given timezone, in hours.
    """
    return int(pytz.timezone(timezone_name).utcoffset(
        utc_time()).total_seconds()/SECONDS_IN_HOUR)


def localize_datetime(datetime_obj, timezone_name):
    """Localizes the given UTC-aligned datetime by the given timezone.

    Arguments
    ---------
    datetime_obj : datetime.datetime
        A datetime object decipting a specific point in time, aligned by UTC.
    timezone_name: str
        A string with a name of a timezone.

    Returns
    -------
    datetime.datetime
        An datetime object aligned by the given timezone.
    """
    return datetime_obj.replace(tzinfo=pytz.utc).astimezone(
        pytz.timezone(timezone_name))


def datetime_to_dateint(datetime_obj):
    """Converts the given datetime object to the corresponding dateint.

    Arguments
    ---------
    datetime_obj : datetime.datetime
        A datetime object decipting a specific point in time.

    Returns
    -------
    int
        An integer represeting the day, month and year of the given point in
        time. For example, 3:32 AM on December 3rd 2015 will be converted to
        the integer 20151203.
    """
    return datetime_obj.year * 10000 + datetime_obj.month * 100 \
        + datetime_obj.day


def local_datetime_to_timestamp(datetime_obj):
    """Converts the given localized naive datetime object to a UTC timestamp.

    Arguments
    ---------
    datetime_obj : datetime.datetime
        A naive (not timezone-aware) datetime object decipting a specific
        point in time in the local machine timezone.

    Returns
    -------
    int
        The UTC timestamp corresponding to the given datetime object.
    """
    return int(datetime_obj.timestamp())


def utc_datetime_to_timestamp(datetime_obj):
    """Converts the given naive UTC-aligned datetime object to a UTC timestamp.

    Arguments
    ---------
    datetime_obj : datetime.datetime
        A naive (not timezone-aware) datetime object decipting a specific
        point in time in UTC time.

    Returns
    -------
    int
        The UTC timestamp corresponding to the given datetime object.
    """
    return int(datetime_obj.replace(tzinfo=timezone.utc).timestamp())
