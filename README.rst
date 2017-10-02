utilitime
#########
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

A small pure-python package for utility decorators.

.. code-block:: python

  from utilitime.datetime import datetime_to_dateint
  from utilitime.dateint import shift_dateint, today_int, dateint_range

  start_dateint = datetime_to_dateint(some_dt_obj)
  day_after_tomorrow = shift_dateint(today_int, 2)
  dateints_to_check = dateint_range(start_dateint, day_after_tomorrow)

.. contents::

.. section-numbering::


Installation
============

Install ``utilitime`` with:

.. code-block:: bash

  pip install utilitime


Components
==========

The package is composed of several sub-components, each dedicated to functions dealing with mainly one type of time representation.

dateint
-------

The dateint format uses integer objects to decipt a specific calendaric day; e.g. ``20161225``. This components deals with converintg and transforming objects of this type.

datetime
--------

Utilitu methods for standard ``dateime.dateime`` objects.

time
----

Utilitu methods for standard ``dateime.time`` objects.

timestamp
---------

The timestamp format uses integer objects to decipt a specific moment in time by seconds (or sometimes milliseconds) since the epoc;h e.g. ``1506984924``. This components deals with converintg and transforming objects of this type.

weekday
-------

Utility methods for ordered lists of weekday names.

TimeInterval
------------

Defines a type corresponding to a time interval between two specific points in time (and not their difference, like ``datetime.timedelta``).


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
--------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/utilitime.git


Install in development mode with test dependencies:

.. code-block:: bash

  cd utilitime
  pip install -e ".[test]"


Running the tests
-----------------

To run the tests, use:

.. code-block:: bash

  python -m pytest --cov=utilitime


Adding documentation
--------------------

This project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings (in my personal opinion, of course). When documenting code you add to this project, please follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


Credits
=======
Created by Shay Palachy  (shay.palachy@gmail.com).

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/utilitime.svg
  :target: https://pypi.python.org/pypi/utilitime

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/utilitime.svg
   :target: https://pypi.python.org/pypi/utilitime

.. |Build-Status| image:: https://travis-ci.org/shaypal5/utilitime.svg?branch=master
  :target: https://travis-ci.org/shaypal5/utilitime

.. |LICENCE| image:: https://img.shields.io/pypi/l/utilitime.svg
  :target: https://pypi.python.org/pypi/utilitime

.. |Codecov| image:: https://codecov.io/github/shaypal5/utilitime/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/utilitime?branch=master
