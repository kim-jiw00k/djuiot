import tensorflow as tf
import keras
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist.load_data()
print(fashion_mnist)
(train_images, train_labels), (test_images, test_labels) = fashion_mnist
print(train_images.shape)
print(test_images.shape)

# plt.imshow(train_images[0],cmap='gray')
# print(train_labels[0])
# plt.show()

# scaling
# minmax() -> 0~255 : / 255.0
train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential(name='Fashion')

input_layer = keras.Input(shape=(28, 28), name="Input_Layer")
model.add(input_layer)
flatten = keras.layers.Flatten(name='FlattenLayer')
model.add(flatten)
model.add(keras.layers.Dense(units=128, activation='relu', name='Layer1'))
model.add(keras.layers.Dense(units=64, activation='relu', name='Layer2'))
model.add(keras.layers.Dense(units=32, activation='relu', name='Layer3'))
model.add(keras.layers.Dense(units=10, activation='softmax', name='OUTPUT'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
model.fit(x=train_images,y=train_labels, epochs=50, verbose='auto')
print(f'예측 정확도 : {model.evaluate(x=test_images, y=test_labels)}')

"""
은닉층이 1개 일 때
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 815us/step - accuracy: 0.8889 - loss: 0.4650
예측 정확도 : [0.48694825172424316, 0.8880000114440918]

은닉층이 3개 일 때
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 866us/step - accuracy: 0.8865 - loss: 0.5203
예측 정확도 : [0.5032250881195068, 0.8876000046730042]
"""