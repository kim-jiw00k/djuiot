from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
print(digits)
print(digits.data.shape) # digits.shape 과 동일 학습을 할려면 이것
print(digits.images.shape)  # 그림을 볼려면 이것
# plt.imshow(digits.images[1], cmap=plt.cm.gray_r)
# plt.show()
n_samples = len(digits.images)
old_data = digits.images.reshape(n_samples, -1)
print(old_data)
print(old_data.shape)
data = digits.data
from sklearn.model_selection import train_test_split
(X_train, X_test, y_train, y_test) = train_test_split(data, digits.target, test_size=0.3, random_state=42)
from sklearn.neighbors import KNeighborsClassifier
k = 1
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X=X_train,y=y_train)
print(f"학습 정확도 : {knn.score(X=X_train,y=y_train)}")
predictions = knn.predict(X=X_test)
from sklearn.metrics import accuracy_score
print(f"예측 정확도 : {accuracy_score(y_pred=predictions, y_true=y_test)}")
from sklearn.metrics import classification_report
print("Evaluation on Testting Data")
print(classification_report(y_true=y_test,y_pred=predictions))

y_predict = knn.predict(X=[X_test[5]])
print(y_predict)
plt.imshow(X_test[5].reshape(8,8), cmap='gray', interpolation='nearest')
plt.show()