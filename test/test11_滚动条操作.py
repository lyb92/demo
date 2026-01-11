# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url

url = r"G:\PycharmProjects\test\alert.html"
driver.get(url)
sleep(3)
#  第一步 设置js控制滚动条语句
js = "window.scrollTo(0,10000)"
#  第二步 调用执行js语句方法
driver.execute_script(js)


# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
