# -*- coding: utf-8 -*-
# @Time : 2021/11/19 14:57
# @Author : Limusen
# @File : config

from configparser import ConfigParser

# 1. 实例化
conf = ConfigParser()

# 2. 读取文件
conf.read("D:\pythonProject\class_config\demo.ini", encoding="utf-8")
value = conf.get("log", "name")
print(value)

# # 3.读取出来为布尔值
# val = conf.getboolean("log", "f_fail")
# print(val)

# 　获取当前的section
# conf.sections()
# s = conf.options("log")
# print(s)


# # 写入：set 改变内存中的值
# conf.set("log", "file_name", "oytes.log")
# # 写入文件
# conf.write(open("demo.ini", "w", encoding="utf-8"))
