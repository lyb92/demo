# 导包
from time import sleep

import time
from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url

# 打开百度
driver.get("https://www.baidu.com")

#  输入admin
driver.find_element_by_css_selector("#kw").send_keys("admin")
#  调用截图方法
# driver.get_screenshot_as_file("./admin.png")
# driver.get_screenshot_as_file("../image/admin02.png")
driver.get_screenshot_as_file("../image/%s.png"%(time.strftime("%Y_%m_%d %H_%M_%S")))



# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
