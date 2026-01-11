# 定义一个列表
my_list = [10, 20, 30, 40, 50]
# pos = my_list.index(30)
old_value = 30
new_value = 110
if old_value in my_list:
    # 查找到值为old_value的位置
    pos = my_list.index(old_value)
    # 根据位置修改值
    my_list[pos] = new_value
print(my_list)

my_list2 = ["abc","def","gyh"]
# extend函数将一个列表的尾数追加到另一个列表
my_list.extend(my_list2)
print(my_list)
