# -*- coding: utf-8 -*-
# @Time : 2021/11/18 17:25
# @Author : Limusen
# @File : handle-excel

import os
import json
from openpyxl import load_workbook

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../TestDatas/api_cases.xlsx')


class HandleExcel:

    def __init__(self, file_path, sheet_name):
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
            # # 将请求数据从json转换成字典对象
            # res['request_data'] = json.loads(res['request_data'])
            # res['expected'] = json.loads(res['expected'])

            all_datas.append(res)
        return all_datas

    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    fix = HandleExcel(file_path, "create")
    cases = fix.read_all_data()
    fix.close_file()

    # case = cases[0]
    # print(case)
    #
    # print(case['expected'])
    for i in cases:
        print(i)
