# import random
import random

lst = [item*item for item in range(1,11)]
print(lst)

lst1 = [random.randint(1,100) for _ in range(10)]
print(lst1)

lst2 = [i for i in range(10) if i % 2 == 0]
print(lst2)

lst3 = [[random.randint(1,100) for _ in range(5)]for _ in range(4)]
print(lst3)