# -*- coding: utf-8 -*-
# @Time : 2021/11/19 13:26
# @Author : Limusen
# @File : demo_log

import logging

# logging.info("s11111111")
# logging.warning("sad")

"""

日志收集器 ==> 渠道(Handle) ==> 日志格式(Formatter) ==> 赋值给渠道() ==> 输出日志()
             日志级别



# 自定义日志

第一步: 创建日志收集器
logging.getLogger("收集器的名字")

第二步: 给日志收集器,设置日志级别 Level
logger.setLevel(logging.INFO)

第三步: 定义输出渠道 Handle   控制台(streamHandle)/文件(FileHandle)
handle1 = logging.StreamHandler()

第四步: 设置渠道的输出内容格式
fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s s(%(lineno)d)行: %(message)s"
formatter = logging.Formatter(fmt)

第五步: 将日志绑定到渠道
handle1.setFormatter(formatter)

第六步: 将设置好的渠道,添加到日志收集器上


"""

logger = logging.getLogger("接口测试日志")
# 设置日志输入级别
logger.setLevel(logging.INFO)

# 设置日志的输出渠道
handle1 = logging.StreamHandler()
handle1.setLevel(logging.DEBUG)

# 设置渠道输出的格式内容
fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s -%(lineno)d行: %(message)s"
formatter = logging.Formatter(fmt)

# 将日志格式绑定到渠道当中
handle1.setFormatter(formatter)

# 将设置好的日志渠道，添加到日志渠道上
logger.addHandler(handle1)

# 设置文件 fileHandle
handle2 = logging.FileHandler("my_logger.log", encoding="utf-8")
# 设置格式
handle2.setFormatter(formatter)
logger.addHandler(handle2)

logger.info("hello,第一个收集器")
logger.debug("debug")

print("=======================================")

from logging import handlers

