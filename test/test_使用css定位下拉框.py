# 导包
from time import sleep

from selenium import webdriver

from selenium.webdriver.support.select import Select

# 获取浏览器驱动对象


driver = webdriver.Firefox()

# 打开url

url = r"G:\PycharmProjects\test\select.html"
driver.get(url)


"""
# 使用css定位来操作A上海
driver.find_element_by_css_selector("[value='sh']").click()
sleep(5)
# 使用css定位来操作A广州
driver.find_element_by_css_selector("[value='gz']").click()
"""


el = driver.find_element_by_css_selector("#selectA")

# 通过下标形式访问
Select(el).select_by_index(2)

sleep(2)

Select(el).select_by_index(3)
driver.refresh()

"""


# 通过value形式访问
# 切换上海
Select(el).select_by_value("sh")
sleep(2)
# 切换广州
Select(el).select_by_value("gz")
"""
"""
#
# 通过显示文本切换
# 切换上海
Select(el).select_by_visible_text("A上海")
sleep(2)
# 切换广州
Select(el).select_by_visible_text("A广州")
"""
# sleep(2)
#


# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
