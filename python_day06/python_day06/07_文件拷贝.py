# 获得要拷贝的文件名
old_file_name = input("请输入一个文件名")
# 获得文件的名字和后缀
point_position = old_file_name.rfind(".")

if point_position > 0:
    suffix = old_file_name[point_position + 1:]
    # 拼接新的文件名
    new_file_name = old_file_name[:point_position] + "[附件]." + suffix
else:
    new_file_name = old_file_name + "[附件]"

# 以读的方式打开旧的文件
old_file = open(old_file_name, "rb")
# 以写的方式打开新文件
new_file = open(new_file_name, "wb")

new_file.writelines(old_file.readline())

