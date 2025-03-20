import matplotlib.pyplot as plt
x = [i for i in range(10) ]
y = map(lambda x:x**2,x)
Y = [i for i in y]
print(Y)
plt.plot(x,Y)
plt.show()

import numpy as np

b = np.arange(10)
plt.plot(b**2)
plt.show()