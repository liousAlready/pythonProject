# -*- coding: utf-8 -*-
# @Time : 2021/11/18 17:25
# @Author : Limusen
# @File : handle-excel

"""


excel类，需求的实现时什么

1.读取表头
2.读取数据 --读取表头意外的所有数据 --返回值：列表，成员是每一行数据


初始话工作？

加载一个excel，打开已表单。

"""
import os
from openpyxl import load_workbook

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login_cases.xlsx')


class HandleExcel:

    def __init__(self,file_path, sheet_name):
        # 　1.加载excel数据文件
        self.wb = load_workbook(file_path)
        # 　2.根据表单名称选择表单
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:  # 遍历第一行的每一列
            titles.append(item.value)
        return titles

    def read_all_data(self):
        all_datas = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]:  # 遍历数据行
            values = []
            for val in item:  # 获取每一行的值
                values.append(val.value)
            res = dict(zip(titles, values))  # title和每一行数据,打包成字典
            # res['check'] = eval(res['check'])  # 将check的字符串,转换成字典对象
            all_datas.append(res)
        return all_datas

    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    fix = HandleExcel(file_path,"login")
    cases = fix.read_all_data()
    fix.close_file()
    for case in cases:
        print(case)
