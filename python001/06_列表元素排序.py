# 创建一个包含十个随机数的列表
import random

my_list = []
i = 0
while i < 10:
    random_num = random.randint(1, 100)
    my_list.append(random_num)
    i += 1

print(my_list)

# 对列表中的元素进行排序,sort排序的意思
# 默认排序是从小到大，升序排序
my_list.sort()
print(my_list)

# 需要降序排列，就需要将 sort()函数的 reverse的默认值改为Ture

my_list.sort(reverse=True)
print(my_list)

# 逆序
my_list.reverse()
print(my_list)
