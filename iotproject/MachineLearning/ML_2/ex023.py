from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import keras
import tensorflow as tf

(X, y) = load_iris(return_X_y=True)
#print(X)
#print(X.shape)
#print(y)
#print(y.shape)

(X_train, X_test, y_train, y_test) = train_test_split(X, y, stratify=y, train_size=0.8, random_state=2025)

# scaling
scaler = MinMaxScaler()
scaler.fit(X_train)
scaler.transform(X_train) # 값이 바뀐다
# print(X_train)
# scaler.fit(X_test)
# scaler.transform(X_test)

y_train_label = keras.utils.to_categorical(x=y_train)   # OneHotEncoding
y_test_label = keras.utils.to_categorical(x=y_test)     # MultiHotEncoding

# print(y_train_label)
# print(y_test_label)

model = keras.Sequential(name='IrisModel')
input_layer = keras.Input(shape=(4,), name='Input_Layer')
model.add(layer=input_layer)
model.add(keras.layers.Dense(units=32, activation='relu', name='layer1'))
model.add(keras.layers.Dense(units=16, activation='relu', name='layer2'))
model.add(keras.layers.Dense(units=8, activation='relu', name='layer3'))
output_layer = keras.layers.Dense(units=3, activation='softmax', name='Output_Layer')
model.add(layer=output_layer)
model.summary()
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['categorical_accuracy'])
history = model.fit(x=X_train, y=y_train_label, epochs=500, verbose='auto')
# history = model.fit(x=X_train, y=y_train, epochs=500, verbose='auto')
print(f'예측 정확도 : {model.evaluate(x=X_test, y=y_test_label)}')
# print(f'예측 정확도 : {model.evaluate(x=X_test, y=y_test)}')

"""
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 131ms/step - accuracy: 1.0000 - loss: 0.0029
예측 정확도 : [0.002918579149991274, 1.0]

"""
