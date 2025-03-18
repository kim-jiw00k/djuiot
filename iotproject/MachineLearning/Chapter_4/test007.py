import numpy as np
import matplotlib.pyplot as plt

grid = plt.GridSpec(3,3)
X = np.random.randn(100)
Y = np.random.randn(100)
plt.subplot(grid[0, 0:]).scatter(X,Y)

X = np.linspace(0,4,100)
Y = np.linspace(0,4,100)
plt.subplot(grid[1, :2]).plot(X,Y,'r--')

X = np.linspace(0,10,100)
Y = np.cos(X)
plt.subplot(grid[2, 0]).plot(X,Y,'g-')

X = np.arange(10)
Y = np.random.uniform(0,10,10)
plt.subplot(grid[2, 1]).bar(X,Y)

Z = np.random.uniform(0, 1, (10, 5))
plt.subplot(grid[1:3, 2]).imshow(Z)

plt.show()