import keras
import tensorflow as tf
import numpy as np

X = tf.constant([[-1.23, -1.0, -1.34],
                 [-0.49, 1.0, 0.45],
                 [1.48, -1.0, -0.45],
                 [0.25, 1.0, 1.34]], name="CarInformation")

y = tf.constant([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, 1.0]], name='Target')

model = keras.Sequential(name='Car')
input_layer = keras.Input(shape=(3,), name='Input_Layer')
model.add(input_layer)
model.add(keras.layers.Dense(units=10, activation='relu', name='layer1'))
model.add(keras.layers.Dense(units=10, activation='relu', name='layer2'))
# model.add(keras.layers.Dropout(rate=0.5))  몇 갸의 노드들을 학습 과정에서 랜덤하게 제외
model.add(keras.layers.Dense(units=5, activation='relu', name='layer3'))
output_layer = keras.layers.Dense(units=2, activation='softmax', name='Output_Layer')
model.add(output_layer)
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['categorical_accuracy'])
history = model.fit(x=X, y=y, epochs=500, verbose='auto')


# data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
#
# scaler = MinMaxScaler()
# scaler.fit(data)
# print(scaler.transform(data))