# 字符串提供了一种语法，用来获取字符串中的一个子串

user_email = "simagousheng@itcast.cn"
print(user_email[0])

# 切片语法 左闭右开
print(user_email[0:3])
print(user_email[0:12])
# 获得容器元素的个数
string_length = len(user_email)
print(user_email[12:string_length])

# 起始值不写表示从0开始
print(user_email[:12])
# 结束值不写表示到最后
print(user_email[13:])
print(user_email[:])

#步长
print("*"*20)
print(user_email[0:12])
print(user_email[0:12:2])
# simagousheng@itcast.cn
# 了解 起始 结束 步长都可以为负数
print("&"*20)
print(user_email[-5:-1])
print(user_email[6:1:-1])
print(user_email[::-1])