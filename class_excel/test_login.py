# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/15 9:35 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : pythonProject
# File      : test_login.py
# explain   : 文件说明

import unittest
import os
from ddt import ddt, data
from test_demo.class_2021_11_15 import login_check
from class_excel.handle_excel import HandleExcel

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login_cases.xlsx')
exc = HandleExcel(file_path, "login")
cases = exc.read_all_data()
exc.close_file()

# print(cases)

@ddt
class TestLogin(unittest.TestCase):

    @data(*cases)
    def test_login(self, case):
        # 1.测试数据 　2.测试步骤
        res = login_check(case['user'], case['password'])
        # 3.断言
        self.assertEqual(res, eval(case['check']))


if __name__ == '__main__':
    unittest.main()
