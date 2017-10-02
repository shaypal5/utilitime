"""Utility pure-Python 3 decorators."""

import utilitime.dateint
import utilitime.datetime
import utilitime.time
import utilitime.timestamp
import utilitime.weekday

from .time_interval import TimeInterval
try:
    del utilitime
    del time_interval
except NameError: # pragma: no cover
    pass

# pylint: disable=C0413
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
