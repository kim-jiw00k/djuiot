from sklearn.svm import SVC

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]
svc = SVC(C=1e5, kernel='rbf', gamma = 0.1)     # C 는 클수록 좋고 gamma는 작을 수록 좋다.
svc.fit(X=X, y=y)
print(f"훈련 정확도 : {svc.score(X=X,y=y)}")