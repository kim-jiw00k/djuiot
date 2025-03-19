import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-20, 20)  # -20에서 20 사이의 수를 1의 간격으로 생성
y1 = 2 * x              # 2 * x 를 원소로 가지는 y1 함수
y2 = (1/3) * x ** 2 +5  # (1/3) * x ** 2 +5 를 원소로 가지는 y2 함수
y3 = -x ** 2 - 5        # -x ** 2 - 5 를 원소로 가지는 y3 함수
# 빨간색 점선, 녹색 실선과 세모기호, 파랑색 별표와 점선으로 함수를 표현
plt.plot(x,y1,'g--',x,y2,'ro-',x,y3,'b*:')
plt.axis([-30, 30, -30, 30])
plt.show()