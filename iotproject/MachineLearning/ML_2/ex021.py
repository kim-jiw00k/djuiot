import matplotlib.pyplot as plt
import tensorflow as tf
import keras

mnist_data = keras.datasets.mnist.load_data()
print(mnist_data)       # 필기체 이미지 데이터
(X_train, y_train), (X_test, y_test) = mnist_data
print(X_train.shape)    #60000,28,28 이미지가 60000장 있다는 뜻
print(X_test.shape)

X_train = X_train.reshape((-1, 28*28))
X_test = X_test.reshape((-1, 28*28))

# 스케일링을 해줘야 함
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0
#
# print(X_train.shape)
# print(X_test.shape)
#
# # plt.imshow(X=X_train[0], cmap='Greys')
# # print(y_train[0])
# # plt.show()
#
# # 신경망 구현
# model = keras.models.Sequential(layers=[],name="MNIST_MODEL")
# input_layer = keras.Input(shape=(28*28,), name="Input_layer")
# model.add(layer=input_layer)
# layer1 = keras.layers.Dense(units=512, activation="relu")
# model.add(layer=layer1)
# output_layer = keras.layers.Dense(units=10, activation='softmax')   # 보통 1개 일때 sigmoid 여러개 일대 softmax 쓰인다.
# model.add(layer=output_layer)
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# #crossentropy를 쓰는건 분류 하겠다는 소리
# model.summary()
# history = model.fit(x=X_train, y=y_train, epochs=10, verbose='auto')
# print(f"예측 정확도 : {model.evaluate(x=X_test, y=y_test)}")
# print(history.history['accuracy'])
#
# model.save('2025-03-25_MNIST.keras')

good_model = keras.models.load_model('2025-03-25_MNIST.keras')
y_predict = good_model.predict(x=X_test)

"""
[0.0913565456867218, 0.9789000153541565]
[0.9410666823387146, 0.975516676902771, 0.9836000204086304, 0.9880666732788086, 0.9907000064849854, 0.993066668510437, 0.9945666790008545, 0.995283305644989, 0.9955499768257141, 0.9966333508491516]
"""