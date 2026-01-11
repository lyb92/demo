# 元组可以从语法的层面来限制数据的意外修改
# 元组使用小括号来定义

my_tuple = (10, 20, 30)
print(my_tuple[0])
# 注意： 元组中如果只有1个元素的话，需要在元素后添加逗号
my_tuple = (10,)
# 元组可以嵌套元组
my_tuple = ((1, 2), (10, 20))
print(my_tuple)
# 元组中的元素不能够修改
my_tuple = (1, 2, 3)
# my_tuple[0] = 100

for v in my_tuple:
    print(v)

# 查询
pos = my_tuple.index(3)
print(pos)

# 注意：如果定义的元素中只有一个元素，需要额外添加一个逗号在元素后面。
my_tuple = ((10,),)
print(my_tuple)
# 元组支持切片操作
my_tuple = (1,2,3,4)
print(my_tuple[1:])