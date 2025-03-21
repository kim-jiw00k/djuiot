from sklearn.datasets import load_iris

from ML_2.ex004_diabetes import y_test

iris_data = load_iris() #dataset loading
#print(iris_data)
print(iris_data['target_names'])
print(iris_data['data'].shape)
print(iris_data['target'].shape)
print(iris_data['data'][0:5])

from sklearn.model_selection import train_test_split    #train_test_split 이 7.5:2.5 정도
(X_train, X_test, Y_train, Y_test) = train_test_split(iris_data['data'], iris_data['target'], random_state=0)
print(X_train)
print(X_train.shape)
print()
print(X_test)
print(X_test.shape)

#import pandas as pd
#import matplotlib.pyplot as plt
#iris_dataFrame = pd.DataFrame(data = X_train, columns=iris_data.feature_names) #columns=iris_data["feature_names"] 이것도 가능
#pd.plotting.scatter_matrix(frame=iris_dataFrame,c=Y_train, figsize=(20, 20),
#                           marker='o', hist_kwds={'bins':20}, s=60, alpha= 0.8)
#plt.show()

# KNN 알고리즘 사용
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X=X_train, y=Y_train)    # 학습하기
y_predict = knn.predict(X=X_test)
print(y_predict)    # 추론한것
print(Y_test)       # 정답
import numpy as np
# print(np.mean(y_predict == Y_test).round(2))
from sklearn.metrics import accuracy_score
print(f"예측 정확도 : {accuracy_score(y_true=Y_test,y_pred=y_predict)}")   # 정확도를 보는 것
print(f"훈련 정확도 : {knn.score(X=X_train, y=Y_train)}") # 학습할 때 정확도
x = np.array([[5.0, 3.0, 5.2, 2.3]])
flower = knn.predict(x)
print(flower)