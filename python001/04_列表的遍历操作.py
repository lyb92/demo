my_list = [10,20,30,40]
# 列表是序列式容器，支持索引、切片
print(my_list[0],my_list[2])
print(my_list[:2])

# 1.列表的遍历
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

#2. for循环一般都用于容器中元素的遍历
for val in my_list:
    print(val)
#break continue用于循环中，问题：





