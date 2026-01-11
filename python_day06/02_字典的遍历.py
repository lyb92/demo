my_dict = {"aaa": 10, "bbb": 20, "ccc": 30}
print(my_dict)
my_dict["ddd"] = "dog"
print(my_dict)
# 默认只能遍历出来键
for val in my_dict:
    print(val)

# keys 方法可以获得所有的键列表
key_list = my_dict.keys()
print(list(key_list))
value_list = my_dict.values()
print(list(value_list))

key_value_list = my_dict.items()
print(list(key_value_list))
