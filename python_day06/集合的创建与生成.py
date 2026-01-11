import random

s = set("helloword")
print(s)
s = set([10, 20, 30, 40, 50])
print(s)

s = set(range(3, 10, 1))
print(s)

s = {i for i in range(5, 10)}
print(s)

s = {i for i in range(5, 10) if i % 2 == 1}
print(s)

s = {random.randint(1, 100) for i in range(10)}
print(s)
