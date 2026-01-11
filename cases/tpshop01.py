import unittest


class TestTpshop(unittest.TestCase):
    def test001(self):
        print("输入正确用户名")

    def test002(self):
        print("输入正确密码")

    def test003(self):
        print("点击登录")

    def test004(self):
        print("登录成功")


if __name__ == '__main__':
    print("__name__的值：", __name__)
"""
    __name__:为python的内置变量
    值： 
          1.如果当前运行的模块为当前模块,那么__name__的值为：__main__
          2.如果当前运行的模块不是主模块，那么__name__的值为：模块名称
"""
