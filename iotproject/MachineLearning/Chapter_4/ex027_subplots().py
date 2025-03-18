import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(2, 2)             # 2행 2열의 그림을 그리는 공간을 만듦

X = np.random.randn(100)                            # 정규 분포를 가지는 데이터
Y = np.random.randn(100)                            # 정규 분포를 가지는 데이터
ax[0, 0].scatter(X, Y, c='r',marker='o')                              # 산점도 그림
X = np.arange(10)                                   # 0 에서 9 사이의 연속 값
Y = np.random.uniform(1, 10, 10)      # 균일 분포 값 생성
ax[0, 1].bar(X, Y)                                  # 막대 차트 그림
X = np.linspace(0, np.pi, 100)
Y = np.cos(X)
ax[1, 0].plot(X, Y, 'g')                                 # 실선으로 함수를 그림
Z = np.random.uniform(0, 1, (5, 5))
ax[1, 1].imshow(Z)                                  # 분포를 2D 이미지로 그림

plt.show()

#ax 는 위치를 나타낸다.