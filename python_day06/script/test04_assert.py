"""
目标：unittest常用断言
     1.assertTure : 如果结果为Ture通过，否则失败

"""
import unittest


class Test02(unittest.TestCase):
    def test001(self):
        flag = False
#         断言是否为Ture
#         self.assertTrue(flag)
        self.assertFalse(flag)



