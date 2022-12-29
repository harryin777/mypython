import matplotlib.pyplot as plt
import numpy as np
# 创建一维数组
nd1 = np.array([1, 2, 3, 3, 3, 4, 5, 6])
# 创建二维数组
nd2 = np.array([[1, 2, 3], [4, 5, 6]])

plt.hist(nd1, density=True, align='mid')
plt.show()