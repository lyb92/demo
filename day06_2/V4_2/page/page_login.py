from time import sleep

from selenium.webdriver import ActionChains

from day06_2.V4_2 import page
from day06_2.V4_2.base.base import Base


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self):
        self.base_click(page.login_verify_code)

    # 点击登录按钮

    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    def page_check_agreement(self):
        checkbox = self.base_find_element(page.login_verify_code)
        if not checkbox.is_selected():
            checkbox.click()

    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)

    # 滑块从左滑到右
    # 点击异常信息框 确定
    def page_click_err_btn_ok(self):
        slider = self.base_find_element(page.login_err_btn_ok)
        # 创建一个ActionChains对象
        actions = ActionChains(self.driver)

        # 移动到滑块上
        actions.click_and_hold(slider)

        # 移动滑块到右端（可能需要计算距离）
        # 比如，如果滑块的总宽度是100px，你想移动到50px的位置
        actions.move_by_offset(50, 0).perform()  # 这里50是x轴的偏移量

        # 释放滑块
        actions.release().perform()
        # self.base_click(page.login_err_btn_ok)

    # 截图
    def page_get_img(self):
        self.base_get_image()

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        sleep(2)
        self.page_input_password(pwd)
        sleep(2)
        # self.page_input_verify_code()
        self.page_check_agreement()
        sleep(2)
        self.page_click_login_btn()
        # sleep(2)
        # self.page_click_err_btn_ok()
