# -*- coding: utf-8 -*-
# @Time : 2021/11/22 14:40
# @Author : Limusen
# @File : test_login

import os
import unittest
from ddt import ddt, data
from day4.Common.handle_excel import HandleExcel
from day4.Common.handle_requests import send_requests
from day4.Common.handle_path import datas_dir
from day4.Common.my_logger import logger
from day4.Common.handle_db import HandleDb

# he = HandleExcel(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../TestDatas/api_cases.xlsx'), "login")
he = HandleExcel(os.path.join(datas_dir, "api_cases.xlsx"), "login")
cases = he.read_all_data()
he.close_file()

db = HandleDb()


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("====== 登录模块用例 开始执行 ======")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("====== 登录模块用例 执行结束 ======")

    @data(*cases)
    def test_login_success(self, case):
        logger.info("执行用例编号：{} : {}".format(case["id"], case['title']))
        # # 步骤 测试数据 - 发起请求
        response = send_requests(case['method'], case['url'], case['request_data'])
        # print(response.json())
        # # 　断言　--　code ==0 msg == ok
        logger.info("用例的期望结果是：{}".format(case['expected']))
        try:
            self.assertEqual(response.json()['code'], case["expected"]['code'])
            self.assertEqual(response.json()['desc'], case["expected"]['desc'])
            # 如果check_sql有值，说明数据库校验
            if case['check_sql']:
                result = db.select_one_data(case['check_sql'])
                self.assertIsNotNone(result)
        except AssertionError as e:
            logger.error("用例执行失败，原因：{}".format(e.__str__()))
            raise


if __name__ == '__main__':
    unittest.main()
