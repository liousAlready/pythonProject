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
from class_logger.my_logger import logger

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login_cases.xlsx')
exc = HandleExcel(file_path, "login")
cases = exc.read_all_data()
exc.close_file()


# print(cases)

@ddt
class TestLogin(unittest.TestCase):

    @data(*cases)
    def test_login(self, case):
        logger.info("*********** 开始测试 ***********")
        logger.info("测试数据为：{}".format(case))
        # 1.测试数据 　2.测试步骤
        res = login_check(case['user'], case['password'])
        logger.info("实际运行结果为：{}".format(res))
        # 3.断言
        try:
            self.assertEqual(res, eval(case['check']))
        except AttributeError:
            logger.error("断言失败，用例不通过")
            raise
        else:
            logger.info("断言成功，用例通过！")
        logger.info("********** 测试用例执行结束 **********")


if __name__ == '__main__':
    unittest.main()
