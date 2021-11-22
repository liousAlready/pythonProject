# -*- coding: utf-8 -*-
# @Time : 2021/11/19 14:18
# @Author : Limusen
# @File : my_logger

import logging
from day4.Common.handle_config import conf

class MyLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        # 设置日志级别/渠道/格式
        super(MyLogger, self).__init__(name, level)

        # 日志格式
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s -%(lineno)d行: %(message)s"
        formatter = logging.Formatter(fmt)

        # 　控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            # 设置格式
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if conf.getboolean("log", "file_ok"):
    file_name = conf.get("log", "file_name")
else:
    file_name = None

# logger = MyLogger(conf.get("log", "name"), level=conf.get("log", "level"), file="123.log")
#
# if __name__ == '__main__':
#     logger.info("测试....")
