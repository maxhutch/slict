Slict
=====
|Build Status| |Version Status| |Downloads|

Dictionary that supports slices.

Slict implements Mapping and accepts the `[start]:[stop]` index to slice tuple-keys along one or more of their dimensions.

Slict can wrap any other Python Mapping and is lightweight (O(1) in space).  Try it with a chest_, for example.

Example
-------

.. code:: python

    >>> from slict import Slict
   
    >>> weather = Slict({("12pm", "Temperature"): 15.,  ("12pm", "Wind Speed"): 12.5,
    ...                  ("1pm",  "Temperature"): 15.5, ("1pm", "Wind Speed"):   9.2})
   
    >>> temps = weather[:,"Temperature"]
    >>> for k in temps:
    ...   print("The temperature at {:4s} is {:f}".format(k, temps[k]))
    The temperature at 12pm is 15.000000
    The temperature at 1pm  is 15.500000
   
    >>> noon_weather = weather["12pm",:]
    >>> for k in noon_weather:
    ...   print("The {:s} is {:f}".format(k, noon_weather[k]))
    The Temperature is 15.000000
    The Wind Speed is 12.500000

Install
-------

``slict`` is on the Python Package Index (PyPI):

::

    pip install slict

.. |Build Status| image:: https://travis-ci.org/maxhutch/slict.png
   :target: https://travis-ci.org/maxhutch/slict
.. |Version Status| image:: https://pypip.in/v/slict/badge.png
   :target: https://pypi.python.org/pypi/slict/
.. |Downloads| image:: https://pypip.in/d/slict/badge.png
   :target: https://pypi.python.org/pypi/slict/
.. _chest : https://github.com/ContinuumIO/chest
