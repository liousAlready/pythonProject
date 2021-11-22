# -*- coding: utf-8 -*-
# @Time : 2021/11/22 17:03
# @Author : Limusen
# @File : main

import os
import unittest
from HTMLTestReportCN import HTMLTestRunner

case_dir = os.path.dirname(os.path.abspath(__file__))
# print(case_dir)

s = unittest.TestLoader().discover(case_dir)

# 创建一个html文件，以写的模式打开，支持中文
with open("运营后台登录用例.html", "wb") as fs:
    # 运行测试用例，将结果写入html中
    runner = HTMLTestRunner(fs, title="单元测试报告", tester="li")
    runner.run(s)
