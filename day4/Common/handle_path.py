# -*- coding: utf-8 -*-
# @Time : 2021/11/22 17:53
# @Author : Limusen
# @File : handle_path

import os

current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(current)

# 　测试用例目录
case_dir = os.path.join(current, 'TestCases')

# 测试数据路径
datas_dir = os.path.join(current, 'TestDatas')

# 测试报告
reports_dir = os.path.join(current, 'Outputs\\reports')

# 日志的路径
logs_dir = os.path.join(current, 'Outputs\\logs')

# 配置文件的路径
conf_dir = os.path.join(current, 'Conf')

print(case_dir)
print(datas_dir)
print(reports_dir)
