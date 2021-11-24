# -*- coding: utf-8 -*-
# @Time : 2021/11/24 16:57
# @Author : Limusen
# @File : test_creater_man


import os
import unittest
import json
from ddt import ddt, data
from day4.Common.handle_excel import HandleExcel
from day4.Common.handle_requests import send_requests
from day4.Common.handle_path import datas_dir
from day4.Common.my_logger import logger
from day4.Common.handle_db import HandleDb
from day4.Common.handle_phone import get_new_phone
from day4.Common.handel_data import replace_mark_with_data

# he = HandleExcel(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../TestDatas/api_cases.xlsx'), "login")
he = HandleExcel(os.path.join(datas_dir, "api_cases.xlsx"), "create")
cases = he.read_all_data()
he.close_file()

db = HandleDb()


@ddt
class TestCreate(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        token_case = {
            "method": "POST",
            "url": "api/gateway/system/v2/login",
            "request_data": {"loginInfoDto": {"phone": "13252254992", "pass": "254992", "type": "BackGroundUser",
                                              "loginType": "LoginPass"}}
        }

        token = send_requests(token_case['method'], token_case['url'], token_case['request_data'])  # 接口
        result_dict = token.json()
        cls.login_token = result_dict["data"]["token"]

    @data(*cases)
    def test_create_success(self, case):
        logger.info("执行用例编号：{} : {}".format(case["id"], case['title']))

        # 替换 --动态
        # 请求数据 #phone# 替换成 #new_phone#
        # 　check_sql 里面的 #phone# 替换成 #new_phone#
        if case['request_data'].find("#phone#") != -1:
            new_phone = get_new_phone()
            replace_mark_with_data(case, "#phone#", new_phone)

        # # 将请求数据从json转换成字典对象
        case['request_data'] = json.loads(case['request_data'])

        expected = eval(case['expected'])

        # # 步骤 测试数据 - 发起请求
        response = send_requests(case['method'], case['url'], case['request_data'], self.login_token)
        logger.info("用例的期望结果是：{}".format(case['expected']))
        try:
            self.assertEqual(response.json()['code'], expected['code'])
            self.assertEqual(response.json()['desc'], expected['desc'])
            # 如果check_sql有值，说明数据库校验
            if case['check_sql']:
                result = db.select_one_data(case['check_sql'])
                self.assertIsNotNone(result)
        except AssertionError as e:
            logger.error("用例执行失败，原因：{}".format(e.__str__()))
            raise


if __name__ == '__main__':
    unittest.main()
