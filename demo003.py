print("******模块开始******")


# 定义一个函数
def add(a, b):
    c = a * b
    if c % 2 == 0:
        print("这是一个偶数")
    else:
        print("这是一个奇数")
    print(f"c的值为：{c}")


# 函数调用
add(3, 5)
print("******模块结束******")
