from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1_000,random_state=0,solver='lbfgs')
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]
mlp.fit(X=X, y=y)
print(f"훈련 정확도 : {mlp.score(X=X, y=y)}")

from sklearn.metrics import accuracy_score
y_predict = mlp.predict(X=X)
print(f"예측 정확도 : {accuracy_score(y_true=y, y_pred=y_predict)}")