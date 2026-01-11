# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url

# url = r"G:\PycharmProjects\test\alert.html"
driver.get("https://www.baidu.com")

"""
填写主页面
"""
# 用户名
# driver.find_element_by_css_selector("#kw").send_keys("python")


# 获取当前窗口  -->目的：判断只要不是当前窗口句柄，就一定时新开的窗口句柄
current_handle = driver.current_window_handle

# 点击注册A网页
driver.find_element_by_partial_link_text("hao123").click()

# 获取所有窗口
handles = driver.window_handles
# 判断不是当前窗口句柄
for h in handles:
    if h != current_handle:
        #   切换
        driver.switch_to.window(h)

"""
填写 注册A
"""

# 用户名
driver.find_element_by_css_selector(".textInput.input-hook").send_keys("admin")

# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
