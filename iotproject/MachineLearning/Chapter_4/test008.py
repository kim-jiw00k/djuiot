# pdf 4장 36 page 해보기
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
x1 = np.arange(3)
years = ['2010','2011','2012']
domestic = [6801,7695,8010]
foreign = [777,1046,1681]

plt.barh(x, domestic, height=0.25)
plt.barh(x - 0.3, foreign, height=0.25)
plt.yticks(x, years)
plt.show()