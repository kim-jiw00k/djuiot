import keras
import tensorflow as tf

x = tf.random.normal(shape=(4, 28, 28, 3), name="RandomImage4")
# from matplotlib import pyplot as plt
# plt.imshow(x[0])
# plt.show()
y = keras.layers.Conv2D(input_shape=(28, 28, 3), filters=2, kernel_size=3, activation='relu')(x)
print(y)
print(y.shape)

x = tf.constant([[1.,2., 3.], [4.,5., 6.], [7.,8., 9.]], name="입력 데이터")
print(x)
print(type(x))
x = tf.reshape(x, [1, 3, 3, 1])
print(x)
max_pool_2d = keras.layers.MaxPooling2D(pool_size=2, strides=1, padding='valid')(x)
print(max_pool_2d)