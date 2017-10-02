"""dateime.time-related utility functions."""

from datetime import time

from ..constants import (
    SECONDS_IN_DAY,
)


def decompose_seconds_in_day(seconds):
    """Decomposes seconds in day into hour, minute and second components.

    Arguments
    ---------
    seconds : int
        A time of day by the number of seconds passed since midnight.

    Returns
    -------
    hour : int
        The hour component of the given time of day.
    minut : int
        The minute component of the given time of day.
    second : int
        The second component of the given time of day.
    """
    if seconds > SECONDS_IN_DAY:
        seconds = seconds - SECONDS_IN_DAY
    if seconds < 0:
        raise ValueError("seconds param must be non-negative!")
    hour = int(seconds / 3600)
    leftover = seconds - hour * 3600
    minute = int(leftover / 60)
    second = leftover - minute * 60
    return hour, minute, second


def seconds_in_day_to_time(seconds):
    """Decomposes atime of day into hour, minute and seconds components.

    Arguments
    ---------
    seconds : int
        A time of day by the number of seconds passed since midnight.

    Returns
    -------
    datetime.time
        The corresponding time of day as a datetime.time object.

    Example
    -------
    >>> seconds_in_day_to_time(23430)
    datetime.time(6, 30, 30)
    """
    try:
        return time(*decompose_seconds_in_day(seconds))
    except ValueError:
        print("Seconds = {}".format(seconds))
        print("H = {}, M={}, S={}".format(*decompose_seconds_in_day(seconds)))
        raise


def minutes_in_day_to_time(minutes):
    """Decomposes atime of day into hour, minute and seconds components.

    Arguments
    ---------
    minutes : int
        A time of day by the number of minutes passed since midnight.

    Returns
    -------
    datetime.time
        The corresponding time of day as a datetime.time object.

    Example
    -------
    >>> minutes_in_day_to_time(390)
    datetime.time(6, 30, 00)
    """
    return seconds_in_day_to_time(minutes*60)
