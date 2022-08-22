def example():
    x = 1
    y = 10
    while x < y:
        yield x
        x += 1


example = example()
print(example)
for i in example:
    print(i)

print('*' * 20)

# next 也是往下迭代，但一定要在迭代器还没有完成迭代之前才可以
print(next(example))
print(next(example))
print(next(example))