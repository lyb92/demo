# 定义一个函数
def add(a, b, c=2, *args, **kwargs):
    print(f"a的值为：{a}")
    print(f"b的值为：{b}")
    print(f"c的值为：{c}")
    print(f"args的值为：{args}")
    print(*args)
    print(f"kwargs的值为：{kwargs}")


# 函数调用
add(3, 5, 9, "张珊", 23, 56, "Tom", name="李四", age=23)
