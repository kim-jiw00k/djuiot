from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

(X, y) = load_breast_cancer(return_X_y=True)
print(X[0])

(X_train, X_test, y_train, y_test) = train_test_split(X, y, train_size=0.8, stratify=y, random_state=42)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train) # X_train 값이 안 바뀜
scaler.transform(X_train)   # 값이 바뀜.
scaler.fit(X_test)
scaler.transform(X_test)
print()
print(X_train[0])
print(X_train.shape)

# 신경망
import keras
import tensorflow as tf
model = keras.Sequential(name="Predict_Cancer")
input_layer = keras.Input(shape=(30,), name="Input_Layer")
model.add(input_layer)
model.add(keras.layers.Dense(units=64, activation='relu', name='Layer1'))
model.add(keras.layers.Dense(units=64, activation='relu', name='Layer2'))
model.add(keras.layers.Dense(units=32, activation='relu', name='Layer3'))
output_layer = keras.layers.Dense(units=1, activation='sigmoid', name="OutPut")
model.add(output_layer)
model.summary()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) # 분류에 맞는 loss 이다.
model.fit(x=X_train, y=y_train, epochs=1_000, verbose='auto')
print(f'예측 정확도 : {model.evaluate(x=X_test, y=y_test)}')