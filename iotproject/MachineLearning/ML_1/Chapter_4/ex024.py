import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = x**2
plt.plot(x,y)
plt.axis([0, 100, 0, 100])  # x 값이랑 y이 다를때 실제로 보이는 그래프를 만들기 위해 사용
plt.show()