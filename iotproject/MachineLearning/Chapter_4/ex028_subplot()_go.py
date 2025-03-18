import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import scatter

fig, ax = plt.subplots(2, 3)

for i in range(2):      # 2 행
    for j in range(3):  # 3 열
        ax[i,j].text(0.3, 0.5, str((i,j)),fontsize=11)  # 텍스트 만 표시

plt.show()

