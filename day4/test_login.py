# -*- coding: utf-8 -*-
# @Time : 2021/11/22 14:40
# @Author : Limusen
# @File : test_login

import os
import json
import unittest
from ddt import ddt, data
from day4.handle_excel import HandleExcel
from day4.handle_requests import send_requests

he = HandleExcel(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api_cases.xlsx'), "login")
cases = he.read_all_data()
he.close_file()


@ddt
class TestLogin(unittest.TestCase):

    @data(*cases)
    def test_login_success(self, case):
        # # 步骤 测试数据 - 发起请求
        response = send_requests(case['method'], case['url'], case['request_data'])
        print(response.json())
        # # 　断言　--　code ==0 msg == ok
        self.assertEqual(response.json()['code'], case["expected"]['code'])
        self.assertEqual(response.json()['desc'], case["expected"]['desc'])


if __name__ == '__main__':
    unittest.main()
