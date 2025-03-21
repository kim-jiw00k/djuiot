import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 닥스훈트의 길이와 높이 특성 데이터
dachhund_length = [77, 78, 85, 83, 73, 77, 73, 80]
dachhund_height = [25, 28, 29, 30, 21, 22, 17, 35]
# 사모예드의 길이와 높이 특성 데이터
samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]
samoyed_height = [56, 57, 50, 53, 60, 53, 49, 61]

dachhund_length_mean = np.mean(dachhund_length)
dachhund_height_mean = np.mean(dachhund_height)

samoyed_length_mean = np.mean(samoyed_length)
samoyed_height_mean = np.mean(samoyed_height)

new_dachhund_length = np.random.normal(dachhund_length_mean,10.0,200)
new_dachhund_height = np.random.normal(dachhund_height_mean,10.0,200)

new_samoyed_length = np.random.normal(samoyed_length_mean,10.0,200)
new_samoyed_height = np.random.normal(samoyed_height_mean,10.0,200)

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

dogs = np.concat((dachhund_data, samoyed_data), axis=0) # 데이터 결합
labels = np.concat((dachhund_label, samoyed_label), axis=0)

dog_classes = {0 : "닥스훈트",
               1 : "사모예드"}  # 써주면 좋음 안써도 되는데

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X=dogs,y=labels)
print(knn.classes_)
y_predict = knn.predict(unknown_dog)
print(y_predict)
print(f"이 강아지는 : {dog_classes[y_predict[0]]},{dog_classes[y_predict[1]]},{dog_classes[y_predict[2]]},{dog_classes[y_predict[3]]},{dog_classes[y_predict[4]]}")