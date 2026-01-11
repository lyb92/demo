from time import sleep
# 导包 webdriver
from selenium import webdriver

# 获取 谷歌浏览器对象
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
# 打开百度
driver.get("https://www.baidu.com")
# 暂停3秒
# driver.find_element_by_css_selector("#kw").send_keys("python的环境变量")
# driver.refresh()

# 实例化并获取ActionChains类
action = ActionChains(driver)
# 获取用户名元素
username = driver.find_element_by_css_selector("#kw")
# #调用右击方法
# action.context_click(username).perform()
# 发送用户名admin并进行双击 预期：选中admin
username.send_keys("admin")
action.double_click(username).perform()

#

# driver.find_element_by_css_selector("#su").click()

"""
# 获取title
title = driver.title
print("当前页面title为：", title)

#获取当前URL
current_url = driver.current_url
print("当前页面current_url为：", current_url)
"""

sleep(10)
# 退出驱动
# driver.quit()
