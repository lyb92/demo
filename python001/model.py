def login_auth(func):
    def inner(name, pwd):
        if name == "root" and pwd == "123456":
            print("登录成功")
        else:
            print("登录失败，请正确输入！")
        func(name, pwd)

    return inner


@login_auth
def login(username, password):
    print("username=", username, "password=", password)


username = input("请输入用户名")
password = input("请输入密码")
login(username, password)
