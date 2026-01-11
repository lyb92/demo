"""




    操作：
        1.导包unittest
        2.调用Testloader类下的discover方法
        3.执行测试用例
"""
# 导包
import unittest

# 调用方法
# suite = unittest.TestLoader().discover("../cases")
suite = unittest.TestLoader().discover("../cases", pattern="tpshop*.py")
# 执行套件方法 TextTestRunner
unittest.TextTestRunner().run(suite)
