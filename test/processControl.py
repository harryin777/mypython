print("test")
#注意是中括号
arr = ["t1", "t2", "t3"]
# 变成了大括号
arr2 = {"t1":"ac", "t2":"ac", "t3":"in"}

for t, status in arr2:
    print(t)
    print(status)

# 注意 循环的是 arr2.items()
for t, status in arr2.items():
    print(t)
    print(status)


list(range(5, 10))