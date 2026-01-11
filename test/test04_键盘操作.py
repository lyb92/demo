from time import sleep
# 导包 webdriver
from selenium import webdriver

# 获取 谷歌浏览器对象
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# 打开百度
driver.get("https://www.baidu.com")
# 暂停3秒
# driver.find_element_by_css_selector("#kw").send_keys("python的环境变量")
# driver.refresh()

# 定位用户名
username = driver.find_element_by_css_selector("#kw")
# 输入admin1
username.send_keys("admin1")
sleep(2)
# 删除1
username.send_keys(Keys.BACK_SPACE)
sleep(2)
# 全选admin CTRL+A
username.send_keys(Keys.CONTROL,"a")
sleep(2)
# 复制 CTRL+C
username.send_keys(Keys.CONTROL,"x")
sleep(2)

# 定位密码框 并执行CTRL + V
username.send_keys(Keys.CONTROL,"v")


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
