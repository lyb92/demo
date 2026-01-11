# 字符串的格式化输出
name = input("请输入姓名:")
age = input("请输入年龄:")
# str_name = "%s的年龄是%s岁"%(name,age)

# 方式二：format的方式如果不指定参数传递的顺序，则是按照位置顺序传入
str_name = "{}的年龄是{}岁".format(name,age)
print(str_name)
