# 닥스훈트의 길이와 높이 특성 데이터
dachhund_length = [77, 78, 85, 83, 73, 77, 73, 80]
dachhund_height = [25, 28, 29, 30, 21, 22, 17, 35]
# 사모예드의 길이와 높이 특성 데이터
samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]
samoyed_height = [56, 57, 50, 53, 60, 53, 49, 61]

# 그림을 그려보자 (데이터들의 특징을 보기 위함)
from matplotlib import pyplot as plt
#plt.scatter(dachhund_length, dachhund_height, c= 'c', marker='.')
#plt.scatter(samoyed_length, samoyed_height, c= 'b', marker='*')
#plt.xlabel("Height")
#plt.ylabel("Length")
#plt.legend(["Dachhund","Samoyed"],loc="upper right")
#plt.show()

# 길가다 발견한 새로운 강아지의 데이터
new_found_dog_length = [79]
new_found_dog_height = [35]

# plt.scatter(dachhund_length, dachhund_height, c= 'c', marker='.')
# plt.scatter(samoyed_length, samoyed_height, c= 'b', marker='*')
# plt.scatter(new_found_dog_length,new_found_dog_height, c= 'r', marker='p')
# plt.xlabel("Height")
# plt.ylabel("Length")
# plt.legend(["Dachhund","Samoyed","New Dog"],loc="upper right")
# plt.show()            # 드래그 한 후 Ctrl+/

# KNN 알고리듬 (분류 : classfier)
import numpy as np
dachhund_data = np.column_stack((dachhund_length,dachhund_height))  # dachhund_data = [dachhund_length,dachhund_height]
# 이제 닥스훈트의 target 을 만듦 0으로
print(dachhund_data)
print(dachhund_data.shape)
dachhund_label = np.zeros(len(dachhund_data))
print(dachhund_label)
# 사모예드의 target을 만듦 1로
samoyed_data = np.column_stack((samoyed_length,samoyed_height))  # samoyed_data = [samoyed_length,samoyed_height]
print(samoyed_data)
print(samoyed_data.shape)
samoyed_label = np.ones(len(samoyed_data))
print(samoyed_label)

unknown_dog = [[79, 35]] # 새로운 강아지의 데이텀 타입

dogs = np.concat((dachhund_data, samoyed_data), axis=0) # 데이터 결합
labels = np.concat((dachhund_label, samoyed_label), axis=0)
print(dogs)
print(dogs.shape)
print(labels)
print(labels.shape)
dog_classes = {0 : "닥스훈트",
               1 : "사모예드"}  # 써주면 좋음 안써도 되는데
from sklearn.neighbors import KNeighborsClassifier
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X=dogs,y=labels)
print(knn.classes_)
y_predict = knn.predict(unknown_dog)
print(y_predict)
print(f"이 강아지는 : {dog_classes[y_predict[0]]}")
