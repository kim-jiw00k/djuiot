from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
(X, y) = load_breast_cancer(return_X_y=True)
print(X)
print(X.shape)
print()
print(y)
print(y.shape)
cancer = load_breast_cancer()   # 정석
print(cancer)
X = cancer.data
print(X)
y = cancer.target
print(y)
for (i, feature) in enumerate(cancer.feature_names):
    print(f'feature {i+1} : ',feature)
    pass

# feature가 많아서 오버피팅 발생할 수 있다.
(X_train, X_test, y_train, y_test) = train_test_split(X,y,test_size=0.2,stratify=y, random_state= 42)
print(X_train.shape)
print(X_test.shape)
from sklearn.linear_model import LogisticRegression # 이진 분류
logistic = LogisticRegression(solver='liblinear')
# 학습시키기
logistic.fit(X=X_train, y=y_train)
print(f'훈련 정확도 : {logistic.score(X=X_train,y=y_train)}')

from sklearn.metrics import accuracy_score
y_predict = logistic.predict(X=X_test)
print(f'예측 정확도 : {accuracy_score(y_true=y_test, y_pred=y_predict)}')