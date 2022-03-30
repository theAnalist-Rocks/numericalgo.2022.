from order import RK
from Euler.euler import getValues, raffiner, Euler


Euler()
print("-------------------RK-------------------")
f, y_0, *arr = getValues()
RK(f, y_0, *sorted(arr), order=4, precision=-3)
