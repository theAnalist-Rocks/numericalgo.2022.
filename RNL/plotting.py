import matplotlib.pyplot as plt
import numpy as np
from newton import newton
from gestion import get_function


def f(X, func):
    for i in X:
        yield func(i)


func, a, b, x, prec = get_function()
X = np.linspace(a, b, num=1000)
y = f(X, func)
Y = []
for i in y:
    Y.append(i)
Y = np.array(Y)

plt.plot(X, Y)
plt.show()
