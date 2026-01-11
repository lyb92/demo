def test01():
    """1.字典定义"""

    my_dict = {"name": "Obama", "age": "18", "gender": "男", 101: 100}
    print(my_dict["name"])
    print(my_dict[101])  # key 关键字 value 值
    my_dict["gender"] = "女"
    print(my_dict)


# def test02():
#     """2.字典不支持索引，也不支持切片"""
# my_dict = {"name": "Obama", "age": 18, "gender": "男", 101: 100}
# print(my_dict[0])
# print(my_dict[1:])


def test03():
    """3.获得字典的值"""

    my_dict = {"name": "Obama", "age": 18, "gender": "男", 101: 100}
    # 使用中括号这种访问字典中元素的方式，如果键不存在则会报错，程序终止
    # print(my_dict["age1"])
    # 使用get方法，如果 key 不存在默认返回 None， 也可以指定默认返回值
    print(my_dict.get("age","我是默认值"))

def test04():
    """4.添加和修改元素"""

    my_dict = {"name": "Obama", "age": 18, "gender": "男", 101: 100}
    # 如果 key 不存在则是新增元素
    my_dict["score"] = 90
    print(my_dict)
    # 如果 key 存在的话就是修改元素
    my_dict["name"] = "trump"
    print(my_dict)
# test02()
# test03()
test04()
