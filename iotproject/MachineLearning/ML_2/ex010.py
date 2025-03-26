from sklearn.datasets import make_blobs

(X, y) = make_blobs(centers=4, n_samples=200, random_state=42)
print(X)
print(y)

from matplotlib import pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, marker='*')
plt.axis('equal')
plt.show()

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression(solver='liblinear')

from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(X, y, stratify=y, train_size=0.8, random_state=0)
print(X_train.shape)
print(X_test.shape)
logistic.fit(X=X_train, y=y_train)
print(f'훈련 정확도 : {logistic.score(X=X_train, y=y_train)}')
y_predict = logistic.predict(X=X_test)
from sklearn.metrics import accuracy_score
print(f'예측 정확도 : {accuracy_score(y_true=y_test, y_pred=y_predict)}')