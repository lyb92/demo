# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配。
import random

# 定义学校和办公室
school = [[], [], []]
from typing import List


def create_teachers():
    # 定义列表保存老师
    teacher_list = []

    index = 1
    while index <= 8:
        # 创建老师的名字
        teacher_name = "老师" + str(index)
        # 把老师装进笼子里
        teacher_list.append(teacher_name)
        index += 1
    return teacher_list


list1 = create_teachers()
print(list1)
# teacher_list2 = create_teachers()
# print(teacher_list2)

# 分配老师
for teacher in list1:
    # 产生一个办公室编号的随机数
    office_number = random.randint(0, 2)
    school[office_number].append(teacher)

for office in school:
    for person in office:
        print(person, end=" ")
    print()
