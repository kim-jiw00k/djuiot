# 3장 pdf 56 page 문제
import numpy as np

def train_test_split():
    a = np.arange(1,51)
    np.random.shuffle(a)

    split_index = int(len(a) * 0.8)
    train_data = a[:split_index]
    test_data = a[split_index:]

    return train_data, test_data

train_data, test_data = train_test_split()
print("Train Data:", train_data)
print("Test Data:", test_data)
