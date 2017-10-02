"""Datetime-related utility functions."""


class TimeInterval:
    """A class that represents a time interval, based on a start and end point.
    """
    def __init__(self, start, end):
        """Create a new TimeInterval object from a start and end point.

        Parameters
        ----------
        start, end : datetime.datetime
        """
        assert start <= end
        self.start = start
        self.end = end

    @classmethod
    def from_timedelta(cls, datetime_obj, duration):
        """Create a new TimeInterval object from a start point and a duration.

        If duration is positive, datetime_obj is the start of the interval;
        if duration is negative, datetime_obj is the end of the interval.

        Parameters
        ----------
        datetime_obj : datetime.datetime
        duration : datetime.timedelta

        Returns
        -------
        neutils.time.TimeInterval
        """
        if duration.total_seconds() > 0:
            return TimeInterval(datetime_obj, datetime_obj + duration)
        else:
            return TimeInterval(datetime_obj + duration, datetime_obj)

    def __repr__(self):
        return "{}({!r}, {!r})".format(
            type(self).__name__, self.start, self.end)

    def __str__(self):
        return "{} -> {}".format(self.start, self.end)

    def __contains__(self, datetime_obj):
        """Check if a certain datetime objects is in the interval, requiring
        that it is between the start and end points (inclusive).

        Parameters
        ----------
        datetime_obj: datetime.datetime

        Returns
        -------
        bool
        """
        return self.start <= datetime_obj <= self.end
