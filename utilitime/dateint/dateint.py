"""Datetime-related utility functions."""

from datetime import datetime, timedelta, date
import math

from ..timestamp import get_timestamp
from ..datetime import (
    utc_time,
    datetime_to_dateint,
)
from ..constants import (
    WEEKDAYS,
)


def decompose_dateint(dateint):
    """Decomposes the given dateint into its year, month and day components.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    year : int
        The year component of the given dateint.
    month : int
        The month component of the given dateint.
    day : int
        The day component of the given dateint.
    """
    year = int(dateint / 10000)
    leftover = dateint - year * 10000
    month = int(leftover / 100)
    day = leftover - month * 100
    return year, month, day


def dateint_to_date(dateint):
    """Converts the given integer to a datetime.date object.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    datetime.date
        The corresponding date object.

    Example
    -------
    >>> dateint_to_date(20170223)
    datetime.date(2017, 2, 23)
    """
    return date(*decompose_dateint(dateint))


def tz_aware_dateint_to_timestamp(dateint, timezone_name):
    """Returns the epoch timestamp for the given timezone and dateint.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.
    timezone_name : str
        The name of the timezone.

    Returns
    -------
    int
        The timestamp corresponding to the start of the given day (so at 0
        hours, 0 minutes, etc...) at the given timezone.
    """
    return get_timestamp(timezone_name, *decompose_dateint(dateint))


def dateint_to_timestamp(dateint):
    """Converts the given dateint to a timestamp, using the local timezone.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    int
        The timestamp corresponding to the start of the given day (so at 0
        hours, 0 minutes, etc...) at the local timezone.
    """
    return int(dateint_to_datetime(dateint).timestamp())


def dateint_to_utc_timestamp(dateint):
    """Converts the given dateint to the corresponding UTC timestamp.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    int
        The UTC timestamp corresponding to the start of the given day (so at 0
        hours, 0 minutes, etc...).
    """
    return tz_aware_dateint_to_timestamp(dateint, 'UTC')


def dateint_to_datetime(dateint):
    """Converts the given dateint to a datetime object, in local timezone.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    datetime.datetime
        A timezone-unaware datetime object representing the start of the given
        day (so at 0 hours, 0 minutes, etc...) in the local timezone.
    """
    if len(str(dateint)) != 8:
        raise ValueError(
            'Dateints must have exactly 8 digits; the first four representing '
            'the year, the next two the months, and the last two the days.')
    year, month, day = decompose_dateint(dateint)
    return datetime(year=year, month=month, day=day)


def dateint_to_weekday(dateint, first_day='Monday'):
    """Returns the weekday of the given dateint.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.
    first_day : str, default 'Monday'
        The first day of the week.

    Returns
    -------
    int
        The weekday of the given dateint, when first day of the week = 0,
        last day of the week = 6.

    Example
    -------
    >>> dateint_to_weekday(20170213)
    0
    >>> dateint_to_weekday(20170212)
    6
    >>> dateint_to_weekday(20170214)
    1
    >>> dateint_to_weekday(20170212, 'Sunday)
    0
    >>> dateint_to_weekday(20170214, 'Sunday')
    2
    """
    weekday_ix = dateint_to_datetime(dateint).weekday()
    return (weekday_ix - WEEKDAYS.index(first_day)) % 7


def dateint_to_weekday_name(dateint):
    """Returns the weekday of the given dateint.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    str
        The weekday name of the given dateint.

    Example
    -------
    >>> dateint_to_weekday_name(20170213)
    'Monday'
    >>> dateint_to_weekday_name(20170212)
    'Sunday'
    >>> dateint_to_weekday_name(20170214)
    'Tuesday'
    """
    return dateint_to_datetime(dateint).strftime("%A")


def shift_dateint(dateint, day_shift):
    """Shifts the given dateint by the given amount of days.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.
    days : int
        The number of days to shift the given dateint by. A negative number
        shifts the dateint backwards.

    Returns
    -------
    int
       A dateint corresponding to the given date shifted by the given amount
       of days.

    Example
    -------
    >>> shift_dateint(20170228, 1)
    20170301
    >>> shift_dateint(20170301, -1)
    20170228
    >>> shift_dateint(20170220, 5)
    20170225
    """
    dtime = dateint_to_datetime(dateint)
    delta = timedelta(days=abs(day_shift))
    if day_shift > 0:
        dtime = dtime + delta
    else:
        dtime = dtime - delta
    return datetime_to_dateint(dtime)


def dateint_range(first_dateint, last_dateint):
    """Returns all dateints in the given dateint range.

    Arguments
    ---------
    first_dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.
    last_dateint : int
        An integer object decipting a specific calendaric day; e.g. 20170108.

    Returns
    -------
    iterable
        An iterable of ints representing all days in the given dateint range.

    Example
    -------
    >>> dateint_range(20170228, 20170301)
    [20170228, 20170301]
    >>> dateint_range(20170225, 20170301)
    [20170225, 20170226, 20170227, 20170228, 20170301]
    """
    first_datetime = dateint_to_datetime(first_dateint)
    last_datetime = dateint_to_datetime(last_dateint)
    delta = last_datetime - first_datetime
    delta_in_hours = math.ceil(delta.total_seconds() / 3600)
    delta_in_days = math.ceil(delta_in_hours / 24) + 1
    dateint_set = set()
    for delta_i in range(0, delta_in_days * 24, 24):
        datetime_i = first_datetime + timedelta(hours=delta_i)
        dateint_i = datetime_to_dateint(datetime_i)
        if dateint_i <= last_dateint:
            dateint_set.add(dateint_i)
    return sorted(dateint_set)


def today_int():
    """Returns the dateint for today."""
    return datetime_to_dateint(utc_time())


def dateint_week_by_dateint(dateint, first_day='Monday'):
    """Return a dateint range of the week the given dateint belongs to.

    Arguments
    ---------
    dateint : int
        An integer object decipting a specific calendaric day; e.g. 20161225.
    first_day : str, default 'Monday'
        The first day of the week.

    Returns
    -------
    iterable
        An iterable of dateint representing all days of the week the given
        dateint belongs to.
    """
    weekday_ix = dateint_to_weekday(dateint, first_day)
    first_day_dateint = shift_dateint(dateint, -weekday_ix)
    last_day_dateint = shift_dateint(first_day_dateint, 6)
    return dateint_range(first_day_dateint, last_day_dateint)


def dateint_difference(dateint1, dateint2):
    """Return the difference between two dateints in days.

    Arguments
    ---------
    dateint1 : int
        An integer object decipting a specific calendaric day; e.g. 20161225.
    dateint2 : int
        An integer object decipting a specific calendaric day; e.g. 20161225.

    Returns
    -------
    int
        The difference between the two given dateints in days.
    """
    dt1 = dateint_to_datetime(dateint1)
    dt2 = dateint_to_datetime(dateint2)
    delta = dt1 - dt2
    return abs(delta.days)
