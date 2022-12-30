import matplotlib.pyplot as plt
import numpy as np

# 创建一维数组
nd1 = np.array([1, 2, 3, 3, 3, 4, 5, 6])
# 创建二维数组
nd2 = np.array([[1, 2, 3], [4, 5, 6]])

# plt.hist(nd1, density=True, align='mid')
# plt.show()

a1 = [1, 2]
b1 = [1, 2]
c1 = [[1], [2]]
d1 = [[3], [4]]
e1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
v2 = np.stack((e1), axis=1)
print(v2.shape)
print(v2)
print("-" * 20)
v4 = np.stack((e1), axis=0)
print(v4.shape)
print(v4)
print("-" * 20)
v3 = np.stack((e1))
print(v3.shape)
print(v3)
print("-" * 20)
v1 = np.stack((c1, d1))[0]
# print(np.stack((c1, d1)))
# print("-" * 20)
# print(np.hstack((a1, b1)))
# print("-" * 20)
# print(np.hstack((c1, d1)))

# a = [[1], [2], [3]]
# b = [[1], [2], [3]]
# c = [[1], [2], [3]]
# d = [[1], [2], [3]]
# print(np.hstack((a, b, c, d)))
