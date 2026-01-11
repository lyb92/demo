"""
 目标：学习Logging底层 模块实现
      1.Logger
"""
import logging

# 获取Logger
logger = logging.getLogger()
# 设置级别
logger.setLevel(logging.INFO)

# 获取控制台 处理器
sh = logging.StreamHandler()
# 将处理器添加到Logger
logger.addHandler(sh)

# 输入信息
logger.info("info")
logger.debug("debug")






