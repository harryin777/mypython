# coding=utf-8
# official chapter 5


# 列表
print("列表")
numList = ['a', 'b', 'c', 'd', 'e', 'f', 'a']
# 计算个数
print(numList.count('a'))
# 返回索引 索引是从 0 开始的, 后面有一个可选参数，如果可选参数大于了整个数组的长度，报错，0 代表出现的第一次，1 代表出现的第二次，如果只出现了两次
# 那么大于等于 1 < list.len 的数值，都返回的是第二次出现的索引
print(numList.index('a', 6))
# 反转列表 注意这个函数并不返回一个值，应该是直接改了指针
numList.reverse()
print(numList)
# 排序
numList.sort()
print(numList)
# 推出栈顶元素, 那么排序结束以后相当于是最后面的元素在栈顶，可选参数是以参数为索引的退出元素
print(numList.pop(1))
# 追加
numList.append('z')
print(numList)
# 插入 在指定位置插入元素
numList.insert(5, 'y')
print(numList)
# 删除 第一个出现的该元素，未找到指定元素时，触发 ValueError 异常
numList.remove('b')
print(numList)
print("-----------------------------------------")

# 实现队列，列表实现队列效率很低，用 collections.deque
print("队列")
from collections import deque

# 这里不知道为什么不能用 TODO 康康
queue1 = deque["aa", "bb", "cc"]
print("-----------------------------------------")

# 列表推导式
# 列表推导式的方括号内包含以下内容：
# 一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或 if 子句。结果是由表达式依据 for 和 if 子句求值计算而得出一个新列表。
# 举例来说，以下列表推导式将两个列表中不相等的元素组合起来：
print("列表推导式")
seq = list([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
print(seq)
# 等价于
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))


def absF(n):
    if n < 0:
        return -n
    else:
        return n


arr = [-1, 5, -6, -3, -10]

absList = list(absF(x) for x in arr)
print(absList)
#  TODO 没看懂这个转置怎么做的
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
print("-----------------------------------------")

# 元组
# 空元组用一对小括号
print("元组")
empty = ()
# 一个元素的元组直接赋值，最后加一个逗号
oneElement = 1,
t = (1, 2)
u = (t, "a")
print(u)
print(len(oneElement))
# 序列解包
x, y = u
print(x)
print(y)
print("-----------------------------------------")

# 集合 set 集合是由不重复元素组成的无序容器
