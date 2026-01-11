import random

d = {item: random.randint(1, 100) for item in range(1, 6)}
print(d)

lis1 = [1001, 1002, 1003, 1004, 1005]
lis2 = ["张三", "李四", "王五", "刘六", "柳七"]
d = {key: value for key, value in zip(lis1, lis2)}
print(d)

lis1 = (1001, 1002, 1003, 1004, 1005)
lis2 = ("张三", "李四", "王五", "刘六", "柳七")
d = {key: value for key, value in zip(lis1, lis2)}
print(d)
