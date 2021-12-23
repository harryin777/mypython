# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("hello world yky")
print('o----')
print(' ||||')
print('*' * 10)
print(6 % 5)
print(12 / 5)
# // 返回的是整数部分，%返回的是余数部分
print('11//5 =' + str(11 // 5))
print('10 ** 3 =' + str(10 ** 3))
x = 10
x += 2
# 同java一样的增广运算
print('x+=2 ' + str(x))

# 输入函数
# name = input('what is your name ')
# print('hi '+ name)


# 类型转换
name = '198'
age = 1999 - int(name)
print(age)

# 变量的类型
print('变量的类型:' + str(type(name)))

# 转义字符，或者用双引号
print('today\'s weather')
print("today's weather")

# 多行字符串
msg = '''
啦啦啦
这就是多文本，比java少了很多的加号
'''
print(msg)

# 字符串中字符的选取，类似java数组的形式但是其实是一个字符串
# 字串的选取 很奇妙
msg = 'abcde'
print(msg[0])
print(msg[0:3])
print(msg[0:])
print(msg[:])
# 注意这种写法，右边的负数相当于排除了从右起1位
print(msg[1:-1])

# str的特殊用法1
value = 'name'
value2 = 'age'
# 前面的f是作为类似一个关键字一样的东西
msg = f'{value}+{value}' + '    ' + f'{value2}'
print(msg)

# len函数 和 .length()方法一样，replace函数的最后一个数字是替换几次的意思
msg = 'abbbbbbc'
print('字符串的长度: ' + str(len(msg)))
print(msg.upper())
print(msg.replace('b', 'eee', 1))

# 在str中找到子字符的索引
print(msg.find('c'))

# title函数的作用，好像就是把第一个字符变成大写
msg = 'qwe'
print(msg)
print(msg.title())

#  (str)target in (str)msg 会返回一个boolean类型
print('q' in msg)

# 处理数字的函数 round，第二个参数是保留几位小数
print(round(2.965478, 5))

# abs() 绝对值函数
print(abs(-10))

# 导入其他模块，类似导入包 现在导入了数学包
import math

print('ceil(2.8)' + str(math.ceil(2.8)))

# if判断语句
# python 中比较引用和变量的方式和java刚好相反 , is 代替equals比较的是内存地址而不是内容
# 而且使用 is 后面加 字符串，前面是变量
# elif 替代了else if
# param = 8
# if param is 8:
#     print('是8')
#     print("确实是8")
# elif param is '7':
#     print('是7')
#     print("确实是7")
# else:
#     print('不是8')


# 逻辑运算符  & 用 and 代替
# | 用 or 代替
# ！ 用 not 代替
# 比较运算符 ！= 和java一样


# 循环逻辑 break continue的用法同java
# 但是居然又一个else 你敢信 而且else是while执行完以后必会执行的类似finally，前提是while没有主动跳出
i = 0
while i <= 5:
    i += 1
    print(i)
    # break
else:
    print('你敢信居然还有个else在while外面！！！')

# for循环
item = [1, 2, 3]
for i in item:
    print(i)
# range 的使用 如果只有一个参数，那就是从0到这个数字，左闭右开。如果两个参数，左边是起点，左闭右开
# 如果有第三个参数，第三个参数是步长
for i in range(5, 8):
    print(i)

# 列表，python可以直接打印出数组，而不是他们的内存地址
# 而且 array[-1] 是这个数组的最后一个元素
array = ['a', 'b', 'c', 'd', 'e', 'f']
print(array[-2])
print(array[2:])
print(array[2:4])
print(array[:4])

# add 方法被 append代替
# copy()方法的使用 完全复制，不影响之前的内容
array2 = array.copy()

array2.pop()
print(array)
print(array2)

# python的数组不可以删除和增加，只有count 和 index 两个方法
num = (1, 5, 22, 46)
print(num.count(5))
print(num.index(22))

# unpacking 特殊用法2 这个用法数组和列表都可以用，下面的例子是一个数组
num = (11, 22, 33)
# 相当于把11赋值给了x， 22给了y， 33给了z
x, y, z = num

# 键值对
person = {
    'name': 'harry',
    'age': '9',
    'country': 'China'
}
# 注意获取属性的方法，如果是中括号，那么没有这个属性时，会报错
# 但是用get方法，没有这个属性，会返回none，再加一个参数，就会在这个属性为none时，默认一个值
print(person['name'])
print(person.get('gendor', 'male'))


# 练习 输入数字返回对应的汉字
# phoneNo = str(input('your phone num'))
# nums = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five'
# }
# for i in phoneNo:
#     print(nums.get(i))

# 函数的使用
def say_hello(name, name2):
    print('hello!' + name)
    print('there!')


# 位置参数是第一种，关键字参数是第二种，如果两者要混用，需要位置参数在前，关键字参数在后
print('start')
say_hello('yky', 'ky')
say_hello(name='yky', name2='ky')
print('finish')


def square(num):
    return num * num


print(square(3))


# 异常
# 下面这个例子的错误一般是因为输入了字符串
# try:
#     age = int(input('Age: '))
#     print(age)
# except ZeroDivisionError:
#     print('0不能做被除数')
# except Exception:
#     print('出现了错误')

# ------------------------------------------------
# 类
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
# 注意python的类，是可以新建出来以后再新建属性的
point1.x = 1
print(point1.x)


# 构造器  注意构造器之前不需要新建任何 属性值
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point2 = Point2(1, 2)
print(point2.y)


# -------------------------------------------------------------
# 继承


class Mammal:
    def walk(self):
        print("walking")


class Dog(Mammal):
    # python 不能有空的的类，所有用pass来表示不是空但是也没东西
    pass


dog = Dog()
dog.walk()

# ---------------------------------------------------------------
# 模块 引入另一个模块


import converters

print(converters.minus(1, 2))

# python 传递数组参数的时候，不需要特殊指明是数组
print(converters.find_max([1, 2, 55]))

# 再python的文件下新建一个_init_.py的文件，这个文件夹会变成一个python的package，但是如果只是新建一个
# 目录的话，就是一个普通的目录，如果直接新建一个package的话，里面自带一个_init_.py的文件
# 有两种导入的方法
import t1.testModule

# 比较麻烦，每次使用方法都需要用这个前缀
t1.testModule.test1()

from t1 import testModule

testModule.test1()

from t1.testModule import test1

test1()

# ---------------------------------------------------------------
# 随机数

import random

# 随机从10和20选数字
for i in range(3):
    print(random.randint(10, 20))

# 随机选取数组中的数字
members = ['John', 'Harry', 'Tom']
print(random.choice(members))

# -------------------------------------------------------------
# 文件类
from pathlib import Path

absolutely = 'F:\yky'
# path = Path(absolutely)
path = Path()
for file in path.glob("*.*"):
    print(file)
