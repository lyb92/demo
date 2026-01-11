from selenium.webdriver.common.by import By
url = "https://s.taobao.com/"
""""以下登录页面元素配置信息，临时存放地"""
# 登录链接
# login_link = By.PARTIAL_LINK_TEXT, "登录"
login_link = By.PARTIAL_LINK_TEXT, "亲，请登录"
# 用户名
# login_username = By.ID, "username"
login_username = By.ID, "fm-login-id"
# 密码
# login_pwd = By.ID, "password"
login_pwd = By.ID, "fm-login-password"
# 验证码
# login_verify_code = By.ID, "verify_code"
login_verify_code = By.CSS_SELECTOR, "#fm-agreement-checkbox"
# 登录按钮
# login_btn = By.ID, ".J-login-submit"
login_btn = By.CSS_SELECTOR, ".fm-button"
# 获取异常文本信息CSS_SELECTOR
# login_err_info = By.CSS_SELECTOR, ".layui_layer_content"
login_err_info = By.CSS_SELECTOR, ".login-error-msg"
# 点击异常提示框 按钮
# 滑块弹出
# login_err_btn_ok = By.CSS_SELECTOR, ".layui_layer_btn0"
login_err_btn_ok = By.CSS_SELECTOR, "#nc_1_n1z"
