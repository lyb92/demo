from day06_2.V5.base.base import Base
from day06_2.V5 import page

class PageLogin(Base):
    # 点击 登录链接地址 封装
    def page_lick_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名封装
    def page_input_username(self):
        pass

    # 输入密码封装
    def page_input_pwd(self):
        pass

    # 输入验证码封装
    def page_input_code(self):
        pass

    # 点击登录 封装
    def page_click_login_btn(self):
        pass

    # 组装 封装
    def page_login(self):
        pass
