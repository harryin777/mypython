# 方法里定义函数

print("方法里定义函数")


class a:
    """lalala"""
    i = 12345

    def f(self):
        print("hello world")


b = a()
print(b.i)
b.f()
# 这里可以把方法保存起来，不是必须立即调用
tmp = b.f
i = 1
while i != 5:
    i += 1
    tmp()
print("-" * 40)
# 构造方法
print("构造方法")


class A:
    """lalala"""
    i = 123

    def __init__(self):
        self.i = 456


c = A()
print(c.i)
print("-" * 40)

# 构造方法指定未定义的属性
print("构造方法指定未定义的属性")


class Add:
    """貌似不可以单纯声明而不赋值"""

    def __init__(self, a1, a2):
        self.ans = a1 + a2


d = Add(1, 2)
print(d.ans)
print("-" * 40)

# 占位符的使用
str = '123 %s' % 'a'
print(str)
