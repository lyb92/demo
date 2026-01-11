# 导包
from time import sleep

import time
from selenium import webdriver

# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 最大化浏览器
driver.maximize_window()

# 隐式等待
driver.implicitly_wait(30)

# 打开url

# 打开百度
driver.get("https://www.baidu.com")

# 设置cookie
driver.add_cookie({"name":"BDUSS","value":"FxTmxNLXhreX5zbEI0SkhWZW40akhKNE1mTUhNZTd3SkRuVVNYcTdEdHFQbnRrRVFBQUFBJCQAAAAAAAAAAAEAAADHTCDzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqxU2RqsVNkRl"})



# 暂停5秒
sleep(5)

# 刷新 必须进行刷新才能看到效果
driver.refresh()



# 暂停2秒
sleep(2)
# 关闭驱动对象
driver.quit()
