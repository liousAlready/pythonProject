# -*- coding: utf-8 -*-
# @Time : 2021/11/19 14:18
# @Author : Limusen
# @File : my_logger

import time
import logging
import os
from day4.Common.handle_config import conf
from day4.Common.handle_path import logs_dir


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        # 设置日志级别/渠道/格式
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

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


if conf.getboolean("log", "file_ok"):
    file_name = os.path.join(logs_dir, 'Api_%s.log' % time.strftime('%Y_%m_%d'))
else:
    file_name = None

logger = MyLogger(file_name)
