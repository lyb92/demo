# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url

url = ""
driver.get(url)

driver.find_element_by_css_selector("[name='upfile1']").send_keys("D:\hello123.txt")

# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
