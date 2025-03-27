import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras.src.datasets.mnist import load_data
#
# (X_train, y_train), (X_test, y_test) = load_data()
# print(X_train.shape)
# print(X_test.shape)
# X_train = X_train.reshape((-1, 28, 28, 1))
# X_test = X_test.reshape((-1, 28, 28, 1))
# print(X_train.shape)
# print(X_test.shape)
#
# X_train = X_train / 255.0
# X_test = X_test / 255.0
# print(X_test[0])
#
# model = keras.Sequential([], name="CNN")
# input_layer = keras.Input(shape=(28, 28, 1), name='Input_Layer')
# model.add(input_layer)
# model.add(keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', name='Conv2D_1'))
# model.add(keras.layers.MaxPooling2D(pool_size=2, name='MaxPool2D_1'))
# model.add(keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', name='Conv2D_2'))
# model.add(keras.layers.MaxPooling2D(pool_size=2, name='MaxPool2D_2'))
# model.add(keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', name='Conv2D_3'))
# model.add(keras.layers.MaxPooling2D(pool_size=2, name='MaxPool2D_3'))
#
# model.add(keras.layers.Flatten())  # 여기서 부터 DNN
# model.add(keras.layers.Dense(units=64, activation='relu', name='HiddenLayer1'))
# model.add(keras.layers.Dense(units=10, activation='softmax', name='Output_Layer'))
# model.summary()
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# model.fit(x=X_train, y=y_train, epochs=10, verbose='auto')
# print(f'예측 정확도 : {model.evaluate(x=X_test, y=y_test)}')
#
# model.save("2025-03-27_CNN.keras")
test_model = keras.models.load_model("2025-03-27_CNN.keras")

import cv2 as cv
Original = cv.imread('test3.png', cv.IMREAD_GRAYSCALE)
# Original = 255 - Original
image = cv.resize(Original, (28,28))
image = 255 - image
image = image.astype('float32')
image = image.reshape(-1, 28, 28, 1)  # 평탄화
image = image / 255.0   # 예측할 이미지

predict_image = test_model.predict(image)
print(f'그림 이미지 값은 : {predict_image} ')
print(f"추정된 숫자 : {predict_image.argmax()}") # 숫자가 복잡해서 가장 큰 값만 뽑아옴
