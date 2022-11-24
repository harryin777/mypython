matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 我的理解，首先列表推导式的主题是内层的中括号内的部分，也就是[row[i] for row in matrix]，这是迭代 matrix 的行，后面的 for i in range(4) 是从 1 迭代到 4
# 那么也就是对于外层的每一个迭代，都会遍历一次 matrix 的行，同时取出该行中索引为 i 的值
print([[row[i] for row in matrix] for i in range(4)])
# 那为什么不能遍历 col，当然不是变量名的原因。因为 matrix 本身是一个元素为数组的数组，那么 matrix 的每一个元素都是一行，所以遍历 matrix 实际上是在遍历行，而不能遍历列
print([[col[i] for col in matrix] for i in range(4)])