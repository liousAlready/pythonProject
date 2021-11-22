# -*- coding: utf-8 -*-
# @Time : 2021/11/19 16:27
# @Author : Limusen
# @File : handle_config

import os
from configparser import ConfigParser


class HandleConfig(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Conf/config.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    print(conf.get("log", "name"))
