# 导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

# 获取浏览器驱动对象


driver = webdriver.Firefox()

# 打开URL
url = ""
driver.get("https://www.baidu.com")

# 实例化webDriverWait()并调用until方法
# 注意：调用until方法返回的一定是个元素


username = WebDriverWait(driver, timeout=10, poll_frequency=0.5).until(lambda x: x.find_element_by_id("#kw1"))
username.send_keys("admin")
# 暂停3秒
sleep(3)
# 关闭驱动
driver.quit()
