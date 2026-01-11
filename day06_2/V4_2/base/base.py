import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from day06_2.V4_2.base.get_logger import GetLogger

# 使用单例
log = GetLogger().get_logger()

class Base:
    # 初始化
    def __init__(self, driver):
        log.info("初始化driver{}".format(driver))
        self.driver = driver
        # 临时代替driver
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # self.driver.get("https://s.taobao.com/search?spm=a21bo.jianhua/a.201867-main.d2_first.5af92a89ts3w8C&q=%E7%94%B5%E8%84%91")

    # 查找元素方法(提供：点击,输入，获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        log.info("正在点击元素{}".format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        log.info("正在输入内容{}".format(value))
        el = self.base_find_element(loc)

        # 清空
        el.clear()
        sleep(2)
        #     输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        log.info("正在得到属性{}".format(loc))
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        # self.driver.get_screenshot_as_file("../image/fail.png")
        self.driver.get_screenshot_as_file("\\PycharmProjects12\\day06_2\\V4_2\\image\\{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
