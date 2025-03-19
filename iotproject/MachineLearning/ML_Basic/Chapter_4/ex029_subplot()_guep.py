import matplotlib.pyplot as plt
import numpy as np

grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
X = np.random.randn(100)
Y = np.random.randn(100)
plt.subplot(grid[0, 0]).scatter(X,Y)

X = np.arange(10)
Y = np.random.uniform(1, 10 ,10)
plt.subplot(grid[0,1:]).bar(X,Y)

X = np.linspace(0, 10, 100)
Y = np.cos(X)
plt.subplot(grid[1, :2]).plot(X,Y)

Z = np.random.uniform(0, 1, (5, 5))
plt.subplot(grid[1, 2]).imshow(Z)

plt.show()