from sklearn.linear_model import Perceptron

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]
percept = Perceptron(tol=0.001, random_state=0)
percept.fit(X=X, y=y)
print(percept.score(X=X, y=y))
y_predict = percept.predict([[0, 0], [1, 0], [1, 1]])
print(y_predict)