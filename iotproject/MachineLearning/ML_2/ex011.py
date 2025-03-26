import numpy as np

epsilon = 0.0000001     # 부동소수점 오차 방지 0으로 나누어지는 문제 해결을 위해서

def step_func(t):       # 퍼셉트론의 활성화 함수
    if t > epsilon:
        return 1
    else:
        return 0

X = np.array([          # 훈련 데이터 세트
    [0, 0, 1],          # 맨 끝의 1은 바이어스를 위한 입력 신호 1이다.
    [0, 1, 1],          # 맨 끝의 1은 바이어스를 위한 입력 신호 1이다.
    [1, 0, 1],          # 맨 끝의 1은 바이어스를 위한 입력 신호 1이다.
    [1, 1, 1]])         # 맨 끝의 1은 바이어스를 위한 입력 신호 1이다.

y = np.array([0, 1, 1, 0])      # 정답을 저장하는 넘파이 행렬
W = np.array([0, 0, 0])         # 가중치를 저장하는 넘파이 행렬

def perceptron_fit(X, Y, epoches=10):       # 퍼셉트론 학습 알고리즘 구현
    global W
    lr = 0.2                               # 학습률

    for t in range(epoches):
        print("epoches = ", t + 1, "="*500)
        for i in range(len(X)):
            y_hat = step_func(np.dot(X[i], W))
            error = y[i] - y_hat
            W = W + lr * error * X[i]
            print("현재 처리 입력 = ",X[i],"정답 = ",Y[i],"y_hat = ",y_hat,"변경된 가중치 = ",W)
        print("-"*100)

perceptron_fit(X, y, 10)

def perceptron_predict(X):
    global W
    for x in X:
        print(x[0], x[1], " => " ,step_func(np.dot(x, W)))

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression(solver='liblinear')
logistic.fit(X=X, y=y)
print(f'훈련 정확도 : {logistic.score(X=X, y=y)}')
y_predict = logistic.predict(X=X)


perceptron_predict(X)