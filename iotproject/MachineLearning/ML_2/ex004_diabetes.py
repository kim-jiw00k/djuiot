from sklearn import datasets
import numpy as np
diabetes_data = datasets.load_diabetes()
print(diabetes_data)
(X, y) = diabetes_data.data, diabetes_data.target
#print(X)
#print(X.shape)          # (442,1)
#print(X[:,2])
#print(X[:,2].shape)     #scikit-learn은 tensor가 2개여야함
bmi = X[:, np.newaxis, 2] # 그래서 tensor를 하나 늘리는 방식으로 만듬
print(bmi.shape)  # BMI 데이터 추출 및 행렬화
from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(bmi, y, train_size=0.9, random_state=0)
# train_size 가 0.9 이면 test_size 가 0.1이 된다 9:1
print(X_train)
print(X_train.shape)     # (397,1)
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X=X_train, y=y_train)
y_predict = regression.predict(X=X_test)
import matplotlib.pyplot as plt
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_predict, color='blue', linewidth=3)
plt.show()