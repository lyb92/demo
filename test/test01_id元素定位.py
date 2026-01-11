# 导包
# from time import sleep
from time import sleep

from selenium import webdriver


# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开URL
url = "https://www.baidu.com"
driver.get(url)
# 查找用户名文本框userA
username = driver.find_element_by_id("chat-textarea").send_keys("admin")

# 查找密码框文本框
# password = driver.find_element_by_id("passwordA")
# 输入用户名
# username.send_keys("admin")
# 输入密码
# password.send_keys("123456")

# 暂停3秒

sleep()
# 关闭驱动
driver.quit()
