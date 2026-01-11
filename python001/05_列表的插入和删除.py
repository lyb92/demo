# 创建空列表
my_list = []

# append 追加 在尾部插入元素
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)

# insert 可以在指定位置插入
my_list.insert(0, 100)
print(my_list)
my_list.insert(2, 200)
print(my_list)

# 删除元素：值删除 位置删除
# pop 方法 用于位置删除，默认删除最后一个位置元素，如果指定
# 了位置，删除改位置元素

my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)
# remove 移除 根据值删除
my_list.remove(200)
print(my_list)
my_list.append(20)
print(my_list)
# remove 删除第一次出现的值
my_list.remove(20)
print(my_list)

print("列表长度：",len(my_list))

# 清空 清除
my_list.clear()
print("列表长度：",len(my_list))
