# 导包
from time import sleep

from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 最大化浏览器
driver.maximize_window()

# 隐式等待
driver.implicitly_wait(30)

# 打开url

url = r"G:\PycharmProjects\test\alert.html"
driver.get(url)



# 定位alert按钮并点击
driver.find_element_by_css_selector("[value='alert警告框']").click()

# driver.find_element_by_css_selector("[value='confirm确认框']").click()

# driver.find_element_by_css_selector("[value='prompt提示框']").click()

# 定位alert并点击
driver.find_element_by_css_selector("#prompt").click()

# 切换到alert
# 默认返回的alert对话框对象
at = driver.switch_to.alert

# 处理对话框
# 同意
# at.accept()

# 取消
at.dismiss()

# 定位用户名输入admin
driver.find_element_by_css_selector("#TANGRAM__PSP_3__userName").send_keys("admin")


# 暂停2秒
sleep(5)
# 关闭驱动对象
driver.quit()
