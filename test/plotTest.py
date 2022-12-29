import matplotlib.pyplot as plt
import numpy as np

# 创建一维数组
nd1 = np.array([1, 2, 3, 3, 3, 4, 5, 6])
# 创建二维数组
nd2 = np.array([[1, 2, 3], [4, 5, 6]])

# plt.hist(nd1, density=True, align='mid')
# plt.show()

a1 = [[[1], [2]]]
b1 = [[[1], [2]]]
print(np.hstack((a1, b1)))
a = [[1], [2], [3]]
b = [[1], [2], [3]]
c = [[1], [2], [3]]
d = [[1], [2], [3]]
print(np.hstack((a, b, c, d)))

