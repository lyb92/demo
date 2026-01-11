# 导包
from time import sleep

from selenium import webdriver
# from time import sleep
from selenium.webdriver import ActionChains

sleep()
# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url

url = ""
driver.get(url)

# 实例化并获取ActionChains类
action = ActionChains(driver)
# 获取用户名元素
username = driver.find_element_by_css_selector("#userA")
#调用右击方法
action.context_click(username).perform()


# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
