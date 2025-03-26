from sklearn.datasets import make_moons
(X, y) = make_moons(n_samples=200, noise=0.25, shuffle=True, random_state=0)
print(X)
print(X.shape)
print(y)
print(y.shape)
from matplotlib import pyplot as plt
plt.scatter(X[:,0], X[:,1], c=y, marker='*', s=30, alpha=0.5)
plt.axis('equal')
plt.show()
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1_000, random_state=0, solver='lbfgs')
mlp.fit(X=X, y=y)
print(mlp.score(X=X,y=y))