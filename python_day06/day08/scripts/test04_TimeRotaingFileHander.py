"""
 目标：学习Logging底层 模块实现
      1.Logger
"""
# 注意以后导logging包，不在使用此方法
# import logging
# 导包时，import logging.handlers ，推荐使用，logging是包名，导入包时会自动执行包下面的__ini__
# handler 为模块名称
import logging.handlers

# 获取Logger
from time import sleep

logger = logging.getLogger("admin")
# 设置级别
logger.setLevel(logging.INFO)

# 获取控制台 处理器
sh = logging.StreamHandler()

# 到文件，根据文件分割
th = logging.handlers.TimedRotatingFileHandler(filename="../log/logtime.log",
                                               when="S",
                                               interval=1,
                                               backupCount=3)

# 设置处理器级别扩展 设置未error级别，那么只有error解蔽
th.setLevel(logging.ERROR)

# 添加格式器
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)]-%(message)s"
fm = logging.Formatter(fmt)

# 将格式器 添加到处理器中

sh.setFormatter(fm)
th.setFormatter(fm)

# 将处理器添加到Logger
logger.addHandler(sh)
logger.addHandler(th)

# 输入信息

logger.info("info")
logger.debug("debug")
logger.error("error")
logger.warning("warning")
