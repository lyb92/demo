# 2.搭建业务框架

# 存储所有的员工信息
yuangongs = {}


def show_menu():
    """显示系统菜单"""
    print("*" * 20 + "员工管理系统菜单" + "*" * 20)
    print("1.添加员工信息")
    print("2.删除员工信息")
    print("3.修改员工信息")
    print("4.显示员工信息")
    print("5.退出管理系统")
    print("*" * 48)


def add_new_yuangong():
    """添加员工信息"""
    # 1. 员工编号、 员工姓名、 员工性别、 员工的薪资
    yuangong_id = input("请输入员工的编号")
    all_yuangong_id = list(yuangongs.keys())
    if yuangong_id in all_yuangong_id:
        print("员工编号重复，添加失败")
        return

# 1.2 如果不重复则进行下面的操作
yuangong_name = input("请输入员工姓名")
yuangong_gender = input("请输入员工性别")
yuangong_salary = input("请输入员工薪资")
# 2.将员工信息保存在字典中
# 2.1 编号作为键，剩下信息作为值
yuangong_info = {"name": yuangong_name, "gender": yuangong_gender, "salary": yuangong_salary}
# 2.2 1001：{"name":xxx,"age":xxx,"salary":xxx}
yuangongs[yuangong_id] = yuangong_info
print("员工编号为 %s 的员工信息添加成功" % yuangong_id)
while True:

    # 1. 显示系统菜单
    show_menu()
    # 2. 获得用户输入的菜单
    my_operate = input("请输入您的操作")
    # 3. 根据用户输入来判断做什么事情
    if my_operate == "1":
        add_new_yuangong()
        print(yuangongs)
    elif my_operate == "2":
        print("删除员工信息！")
    elif my_operate == "3":
        print("修改员工信息")
    elif my_operate == "4":
        print("显示所有员工信息")
    elif my_operate == "5":
        print("退出系统！")
    else:
        print("您的输入有误！")
