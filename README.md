# slict
![](https://travis-ci.org/maxhutch/slict.svg)

Dictionary that supports slices.
Slict implements Mappable and accepts the `:` to slice tuple-keys along one or more of their dimensions.

## Example
```python
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
```
