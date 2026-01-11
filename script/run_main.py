"""
    目标：unitest框架  -testSuite使用
    操作：
        1.导包
        2.实例化获取TestSuite对象
        3.调用addTest方法添加用例  到指定套件
"""

# 导包
import unittest
from script.test01_testcase import Test01
from script.test02 import Test02

# 实例化suite
suite = unittest.TestSuite()

# 调用添加方法
suite.addTest(Test01("test_add()"))
# suite.addTest(Test01("test_add02()"))

# 扩展添加测试类中所有test开头的方法
suite.addTest(unittest.makeSuite(Test02))

# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
