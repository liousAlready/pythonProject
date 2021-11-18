# -*- coding: utf-8 -*-
# @Time : 2021/11/18 15:55
# @Author : Limusen
# @File : excel_demo2

import os
from openpyxl import load_workbook

"""
datas = [
    {"user": "test", "password": "123456", "check": {"code": 0, 'msg': "登录成功"}},
    {"user": "test", "password": "1234561212", "check": {'code': 1, 'msg': '账号或密码不正确'}},
    {"user": "test12212", "password": "123456", "check": {'code': 1, 'msg': '账号或密码不正确'}}
    {"user": "", "password": "123456", "check": {"code": 1, "msg": "所有数据不能为空"}},
    {"user": "", "password": "", "check": {"code": 1, "msg": "所有数据不能为空"}},
]


按行读取数据:
    sh.rows = 所有的行
    sh.column = 所有的列


"""

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login_cases.xlsx')
# print(file_path)

# 　1.加载excel数据文件
wb = load_workbook(file_path)
# 　2.根据表单名称选择表单
sh = wb['login']

# 1.拿到字典的key值: 第一行
titles = []
for item in list(sh.rows)[0]:  # 遍历第一行的每一列
    titles.append(item.value)
# print(titles)

data_list = []
# 2.把key跟value组合到一起,形成一个字典,再放到字典当中
for item in list(sh.rows)[1:]:
    value_dict = {}  # 每一行是一个字典
    # print(item)
    for index in range(len(item)):  # 获取每一行的数据
        # print(index, item[index], item[index].value)
        value_dict[titles[index]] = item[index].value
    # print(value_dict)
    data_list.append(value_dict)
print(data_list)

# # print(list(sh.rows)) #　每一行是个元祖，元祖里面放的是每一行的单元格
#
# for item in list(sh.rows)[1:]:
#     # (<Cell 'login'.A1>, <Cell 'login'.B1>, <Cell 'login'.C1>)
#     # print(item)
#     for cel in item:  # 获取每一行的单元格数据
#         print(cel.value)
