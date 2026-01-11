# def add_num(start, end):
#     i = start
#     my_sum = 0
#     while i <= end:
#         my_sum += i
#         i += 1
#         # print(i)
#     return my_sum
#
#
# # 定义一个新的变量用于保存函数的返回结果
# ret = add_num(1, 100)
# print("ret的结果", ret)

def my_caculator(left, right, operator):
    a = left
    b = right
    if operator == "+":
        ret = a + b
    elif operator == "-":
        ret = a - b
    elif operator == "*":
        ret = a * b
    elif operator == "/":
        ret = a / b
    else:
        print("您输入有误")
        ret = None  # 表示什么也没有，在python中表示无意义的值
    return ret


ret = my_caculator(10, 20, "+")
print("ret:", ret)
ret = my_caculator(10, 20, "-")
print("ret:", ret)
ret = my_caculator(10, 20, "*")
print("ret:", ret)
ret = my_caculator(10, 20, "/")
print("ret:", ret)
ret = my_caculator(10, 20, "$")
print("ret:", ret)