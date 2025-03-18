import numpy as np
import matplotlib.pyplot as plt

height = np.array([175,165,164,164,171,165,160,169,164,159,
                   163,167,163,172,159,160,156,162,166,162,
                   158,167,160,161,156,172,168,165,165,177])
#plt.hist(height, bins=6)
#plt.xlabel("height")
#plt.ylabel("frequency")

plt.hist(height, bins=6, label='cumulative=True', cumulative=True)      # 누적합 계산 함
plt.hist(height, bins=6, label='cumulative=False', cumulative=False)    # 누적합 계산 안함
plt.legend(loc='upper left')

plt.show()