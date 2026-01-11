"""
页面对象层：
    页面对象编写技巧：
        类名：使用大驼峰将模块名称抄进来，有下划线去掉下划线
        方法：根据业务需求每个操作步骤单独封装一个方法

"""
from selenium import webdriver


class PageLogin:
    def _init_(self):
        # 获取driver对象
        driver = webdriver.Firefox()
        # 最大化浏览器
        driver.maximize_window()
        # 隐式等待
        driver.implicitly_wait(30)
        # 打开URL
        driver.get("http:/localhost")

        # 点击登录连接
        def page_click_login_link(self):
            self.driver.find_element_by_partial_link_text("登录").click()

        # 输入用户名
        def page_input_username(self, useranme):
            self.driver.find_element_by_css_selector("#username").send_keys(useranme)

        # 输入密码
        def page_input_pwd(self, pwd):
            self.driver.find_element_by_css_selector("#password").send_keys(pwd)

        # 输入验证码
        def page_input_verify_code(self, code):
            self.driver.find_element_by_css_selector("#verify_code").send_keys(code)

        # 点击登录按钮
        def page_click_login_btn(self):
            self.driver.find_element_by_css_selector(".J-login-submit").click()

        #  获取异常提示信息
        def page_get_text(self):
            return self.driver.find_element_by_css_selector(".layui_layer_content").text

        # 点击登录按钮
        def page_click_err_btn_ok(self):
            self.driver.find_element_by_css_selector(".layui_layer_btn0").click()

        # 组装登录业务方法 给业务层调用
        def page_login(self, usename, pwd, code):
            self.page_click_login_link()
            self.page_input_username(usename)
            self.page_input_pwd(pwd)
            self.page_input_verify_code(code)
            self.page_click_login_btn()
