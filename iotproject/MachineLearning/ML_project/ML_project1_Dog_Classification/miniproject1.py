import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 닥스훈트의 길이와 높이 특성 데이터
dachhund_length = [77, 78, 85, 83, 73, 77, 73, 80]  # 준비된 데이터
dachhund_height = [25, 28, 29, 30, 21, 22, 17, 35]  # 준비된 데이터
# 사모예드의 길이와 높이 특성 데이터
samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]  # 준비된 데이터
samoyed_height = [56, 57, 50, 53, 60, 53, 49, 61]  # 준비된 데이터
dachhund_length_mean = np.mean(dachhund_length)  # 더욱 많은 데이터 값을 위해 평균을 구함
dachhund_height_mean = np.mean(dachhund_height) 

samoyed_length_mean = np.mean(samoyed_length)  # 더욱 많은 데이터 값을 위해 평균을 구함
samoyed_height_mean = np.mean(samoyed_height)

new_dachhund_length = np.random.normal(dachhund_length_mean,10.0,200)  # 새로운 200마리의 닥스훈트 길이 값 구함 랜덤하게 구하지만 평균 값을 통해 +-10 정도
new_dachhund_height = np.random.normal(dachhund_height_mean,10.0,200)  # 새로운 200마리의 닥스훈트 높이 값 구함 랜덤하게 구하지만 평균 값을 통해 +-10 정도

new_samoyed_length = np.random.normal(samoyed_length_mean,10.0,200)  # 새로운 200마리의 사모예드 길이 값 구함 랜덤하게 구하지만 평균 값을 통해 +-10 정도
new_samoyed_height = np.random.normal(samoyed_height_mean,10.0,200)  # 새로운 200마리의 사모예드 높이 값 구함 랜덤하게 구하지만 평균 값을 통해 +-10 정도

new_found_dog_length = np.random.normal((dachhund_length_mean + samoyed_length_mean) / 2, 10.0, size=5)      # 새로운 강아지 랜덤하게 5마리 길이
new_found_dog_height = np.random.normal((dachhund_height_mean + samoyed_height_mean) / 2, 10.0, size=5)      # 새로운 강아지 랜덤하게 5마리 높이

# KNN 알고리즘 으로 분류
# 닥스훈트의 target 을 0으로 만듦
dachhund_data = np.column_stack((new_dachhund_length,new_dachhund_height))
dachhund_label = np.zeros(len(dachhund_data))
# 사모예드의 target 을 1로 만듦
samoyed_data = np.column_stack((new_samoyed_length,new_samoyed_height))
samoyed_label = np.ones(len(samoyed_data))
# 새로운 강아지

unknown_dog = np.column_stack((new_found_dog_length,new_found_dog_height))
print(unknown_dog)

dogs = np.concat((dachhund_data, samoyed_data), axis=0) # 데이터 결합
labels = np.concat((dachhund_label, samoyed_label), axis=0)

dog_classes = {0 : "닥스훈트",
               1 : "사모예드"}  # 안써도 되는데 써주면 알아보기 쉽다


k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X=dogs,y=labels)
print(knn.classes_)
y_predict = knn.predict(unknown_dog)
print(y_predict)
print(f"훈련 정확도 : {knn.score(X=dogs, y=labels)}") # 학습할 때 정확도
print(f"이 강아지는 : {dog_classes[y_predict[0]]},{dog_classes[y_predict[1]]},{dog_classes[y_predict[2]]},{dog_classes[y_predict[3]]},{dog_classes[y_predict[4]]}")


import matplotlib.pyplot as plt

plt.scatter(new_dachhund_length, new_dachhund_height, c= 'c', marker='o')
plt.scatter(new_samoyed_length, new_samoyed_height, c= 'b', marker='*')
plt.scatter(new_found_dog_length,new_found_dog_height, c= 'r', marker='p')
plt.xlabel("Height")
plt.ylabel("Length")
plt.legend(["Dachhund","Samoyed","New Dog"],loc="upper right")
plt.show()            # 드래그 한 후 Ctrl+/
