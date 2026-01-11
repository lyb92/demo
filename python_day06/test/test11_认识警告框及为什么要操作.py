# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url

url = r"G:\PycharmProjects\test\alert.html"
driver.get(url)

# 定位alert按钮并点击
# driver.find_element_by_css_selector("[value='alert警告框']").click()

# driver.find_element_by_css_selector("[value='confirm确认框']").click()

driver.find_element_by_css_selector("[value='prompt提示框']").click()

# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
