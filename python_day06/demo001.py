str2 = """
张灵
李四


王五

张无忌
黄哟哟

雷大
"""
str1 = """
张三
李四


王五

张无忌
黄药师

雷锋
"""

# 先进行切片
str1_list = str1.split("\n")
# print(str1_list)
# 用来保存去掉空元素个空格后的数据
new_str1_list = []
# 循环处理列表中的每个元素
for s1 in str1_list:
    new_s1 = s1.replace(" ", "")
    #     如果是空元素，则跳过
    if new_s1 == "":
        continue
    else:
        # 去掉空格不为空的内容，添加到新列表中
        new_str1_list.append(new_s1)

str2_list = str2.split("\n")
# 用来保存去掉空元素个空格后的数据
new_str2_list = []
# 循环处理列表中的每个元素
for s2 in str2_list:
    new_s2 = s2.replace(" ", "")
    #     如果是空元素，则跳过
    if new_s2 == "":
        continue
    else:
        # 去掉空格不为空的内容，添加到新列表中
        new_str2_list.append(new_s2)

#     通过集合的形式求差集
a = set(new_str1_list) - set(new_str2_list)
print(f"str1中存在，str2中不存在的人为：{a}")

b = set(new_str2_list) - set(new_str1_list)
print(f"str2中存在，str1中不存在的人为：{b}")

# print(new_str1_list)
# print(new_str2_list)