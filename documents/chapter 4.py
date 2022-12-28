# coding=utf-8
# official chapter 4


print("documents")
# 注意是中括号
arr = ["t1", "t2", "t3"]
# 变成了大括号
arr2 = {"t1": "ac", "t2": "ac", "t3": "in"}

# 注意 循环的是 arr 本身
for t in arr:
    print(t)

# 注意 循环的是 arr2.items()
for t, status in arr2.items():
    print(t)
    print(status)

# 居然还可以这样输出 好吧 这应该是个 list
print(list(range(5, 10)))
print(type(list(range(5, 10))))

print("range begin -------")
# 只输出 range
print(range(5, 10))
print(type(range(5, 10)))
print("range end -------")


def askCheristmas(day, ok=True, saying="merry christmas"):
    """here what ???"""
    if ok:
        print("这就 ok 啦")
        print(day)
    else:
        print(saying)


askCheristmas(1)


# 接受一个字典作为参数
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# 第一个应该是位置参数，后面的元组或者序列构成第二个参数(666也可以被输出证明是一个元组就可以)，最后的字典是第三个参数
cheeseshop("Limburger", "It's very runny, sir.", 666,
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# 特殊参数 / *
def f1(la, /, lala, *, lalala):
    print(la)
    print(lala)
    print(lalala)


f1(1, 2, lalala=3)


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))


# 需要解包
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(*d)
print("-" * 40)


# lambda 表达式
def make_lambda(n):
    return lambda x: x + n


f = make_lambda(1)
print(f(100))

print('\'这是单引号里的单引号\'')
print('"这是单引号里的双引号"')

if 1 == 1:
    print("okokok")
