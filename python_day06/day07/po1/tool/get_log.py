# 导包
import logging


# 定义获取logging函数
def get_logging():
    # 设置修改默认的输入日志格式
    fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)]-%(message)s"
    logging.basicConfig(level=logging.DEBUG, format=fm, filename="../log/log01.log")
    return logging
