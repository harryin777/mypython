# 1、一定要指明 lambda
# 2、lambda后面指明变量名
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
