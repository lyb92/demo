# 导包
import unittest
import time

from parameterized import parameterized

from day06_2.V4_2.base.get_driver import GetDriver
from day06_2.V4_2.base.get_logger import GetLogger
from day06_2.V4_2.page.page_login import PageLogin
from day06_2.V4_2.tool.HTMLTestRunner import HTMLTestRunner
from day06_2.V4_2.tool.read_json import read_json

# 使用单例
log = GetLogger().get_logger()


def get_data():
    datas = read_json("calc.json")
    #   新建空列表
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"),
                     data.get("pwd"),
                     data.get("expect")))
    return arrs
    # return [("13822223333", "123456", "账号不存在"),
    #         ("13800003333", "123123", "密码错误")]


# 新建测试类 并继承
class TestLogin(unittest.TestCase):
    login = None

    # setup
    @classmethod
    def setUpClass(cls):
        #   实例化 获取页面对象 PageLogin
        # 获取driver
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)
        # 点击登录链接
        cls.login.page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):
        # 关闭driver驱动对象
        cls.login.driver.quit()

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, expect_result):
        # 调用登录方法
        self.login.page_login(username, pwd)

        # self.assertEqual("账号名或密码不正确", expect_result)
        # self.login.page_get_img()
        # 获取登录提示信息
        msg = self.login.page_get_error_info()
        try:
            # 断言
            self.assertEqual("msg", expect_result)
        except AssertionError as e:
            # 截图
            self.login.page_get_img()
            log.error(e)

        suite = unittest.defaultTestLoader.discover('\\PycharmProjects123\\day06_2\\V4_2', pattern='test*.py')

        report_dir = "\\PycharmProjects123\\day06_2\\V4_2\\report\\{}.html".format(time.strftime('%Y_%m_%d_%H_%M_%S'))

        with open(report_dir, 'wb') as f:
            HTMLTestRunner(stream=f, verbosity=2, title="某某项目自动化测试报告", description="操作系统 windows11").run(
                suite)
