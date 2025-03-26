import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.core import arange

epsilon = 0.000001

x = np.arange(-10.0, 10.0, 0.1)
def step(x:np.ndarray) -> list:
    y = list()
    for element in x:
        if element > epsilon: y.append(1)
        else: y.append(0)
    return y
y = step(x)
plt.plot(x, y)
#plt.axis('equal')
plt.show()