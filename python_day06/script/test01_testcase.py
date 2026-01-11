"""
     目标：unittest框架--Testcase使用
     步骤：
         1.导包improt unitest
         2.新建类 并继承 unittest.Testcase
         3.测试方法必须以test字母开头

    案例：
         编写求和测试函数
"""
# 导包
import unittest


# 编写求和函数
def add(x, y):
    return x + y


# 定义测试类并继承
class Test01(unittest.TestCase):
    #     定义测试方法 注意：以test字母开头
    def test_add(self):
        #         调用要是的函数
        result = add(1, 2)
        print("结果为：", result)

    def test_add02(self):
        result = add(1, 3)

        print("结果为：", result)

    def test_add03(self):
        result = add(1, 6)

        print("结果为：", result)


# 可以这么使用
# unittest.main("test01_testcase")

if __name__ == '__main__':
    unittest.main()
