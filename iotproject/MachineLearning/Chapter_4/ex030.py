import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2010','2011','2012']
domestic = [6801,7695,8010]
foreign = [777,1046,1681]

plt.bar(x, domestic)
plt.bar(x,foreign)
plt.xticks(x, years)

plt.show()