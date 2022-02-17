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
# 推出栈顶元素, 那么排序结束以后相当于是最后面的元素在栈顶，可选参数是以参数为索引的推出元素
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
print("-"*40)

# 实现队列，列表实现队列效率很低，用 collections.deque
print("队列")
from collections import deque

# 这里不知道为什么不能用
queue1 = deque(["aa", "bb", "cc"])
queue1.append("dd")
# 只可以 pop 最左边
queue1.popleft()
print(queue1)
print("-"*40)

# 创建平方的列表
print("创建平方的列表")
squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares2 = [x**2 for x in range(10)]
print("-"*40)

# 列表推导式
# 列表推导式的方括号内包含以下内容：
# 一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或 if 子句。结果是由表达式依据 for 和 if 子句求值计算而得出一个新列表。
# 举例来说，以下列表推导式将两个列表中不相等的元素组合起来：
print("列表推导式")
# 注意 for 的先后顺序，第一个 for 就是最外层的 for 循环
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
# 列表推导式中的初始表达式可以是任何表达式，甚至可以是另一个列表推导式。
#  TODO 没看懂这个转置怎么做的
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
print("-" * 40)


# del 语句，按索引，而不是值从列表中移除元素
print("del")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)
print("-" * 40)
# del 也可以用来删除整个变量：
del a


# 元组
# 空元组用一对小括号
print("元组")
empty = ()
# 一个元素的元组直接赋值，最后加一个逗号，多个元素的元组之间用逗号隔开
oneElement = 1,
t = (1, 2)
u = (t, "a")
print(u)
print(len(oneElement))
# 序列解包，就是怎么打进一个包里或者叫怎么打进一个元组里，就怎么解出来
x, y = u
print(x)
print(y)
print("-" * 40)


# 集合 set 集合是由不重复元素组成的无序容器
print("set")
# 创建集合用花括号或 set() 函数，创建空集合只能用 set()，不能用 {}，{} 创建的是空字典
basket = {"a", "b", "p"}
a = set('absdfjosdif')
b = set('sdf')
# 支持这种运算，NB，也支持逻辑运算
print(a - b)
print(a | b)
print(a & b)
# ^ letters in b or in a ,but not both
print(a ^ b)
# 集合也支持推导式：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print("-" * 40)

# 字典
print("字典")
# 花括号 {} 用于创建空字典。另一种初始化字典的方式是，在花括号里输入逗号分隔的键值对
print({})
ddd = {"a": 1, "c": 5, "b": 2}
# 这个只会拿到 key 值
ddd = sorted(ddd)
print(ddd)
aaa = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(aaa)
# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷
ccc = dict(sape=4139, guido=4127, jack=4098)
print("-" * 40)

# 循环技巧
print("循环技巧")
# 在字典中循环时，用 items() 方法可同时取出键和对应的值
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 只是输出 key 值的索引和 key 值
for k, v in enumerate(knights):
    print(k, v)

# 在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值，注意这是序列，而不单指字典
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    # 注意这里的占位符的使用
    print('What is your {0}?  It is {1}.'.format(q, a))


# 反转顺序
for i in reversed(questions):
    print(i)
# 排序
aaa = [1, 6, 5, 4]
for i in sorted(aaa):
    print(i)
# 去重
bbb = [9, 9, 99, 999, 999]
for i in set(bbb):
    print(i)

print(__name__)