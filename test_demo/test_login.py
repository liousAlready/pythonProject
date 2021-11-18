# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/15 9:35 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : pythonProject
# File      : test_login.py
# explain   : 文件说明

import unittest
import ddt
from test_demo.class_2021_11_15 import login_check

"""

定义测试类，继承unittest.TestCase
在测试类当中，以test_开头，定义测试函数
每一个test_开头的函数，就是一个测试用例

编写用例：
    1.测试数据
    2.测试步骤
    3.断言：预期结果与实际结果的对比
        AssertionError: 断言失败 -- 用例失败
        assert  表达式（True表示通过，False表达失败）     期望等于实际结果
    
"""

datas = [
    {"user": "test", "password": "123456", "check": {"code": 0, 'msg': "登录成功"}},
    {"user": "test", "password": "1234561212", "check": {'code': 1, 'msg': '账号或密码不正确'}},
    {"user": "test12212", "password": "123456", "check": {'code': 1, 'msg': '账号或密码不正确'}}
    # {"user": "", "password": "123456", "check": {"code": 1, "msg": "所有数据不能为空"}},
    # {"user": "", "password": "", "check": {"code": 1, "msg": "所有数据不能为空"}},
]

'''
0.引入ddt
1.在测试类名上面,用@ddt

2.在测试函数上面,使用@ddt.data(*列表)
    在测试函数的参数中,定义一个参数用来接收每一组测试数据
'''
from ddt import ddt,data

@ddt
class TestLogin(unittest.TestCase):

    @data(*datas)
    def test_login(self, case):
        # 1.测试数据 　2.测试步骤
        res = login_check(case['user'], case['password'])
        # 3.断言
        self.assertEqual(res, case['check'], "test_login_ok,测试失败")

    @classmethod
    def setUpClass(cls) -> None:
        print("=====测试类开始执行=======")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=====测试类结束=======")

    def setUp(self) -> None:
        print("======单个用例执行=======")

    def tearDown(self) -> None:
        print("======单个用例结束=======")

    # def test_login_wrong_passwd(self):
    #     res = login_check("test", "1234561212")
    #     text = {"code": 1, 'msg': "账号或密码不正确"}
    #     self.assertEqual(res, text, "test_login_wrong_passwd,测试失败")
    #
    # def test_login_wrong_user(self):
    #     res = login_check("test12212", "123456")
    #     text = {"code": 1, 'msg': "账号或密码不正确"}
    #     self.assertEqual(res, text, "test_login_wrong_user,测试失败")
    # def test_login_no_passwd(self):
    #     res = login_check(username="test")
    #     text = {"code": 1, "msg": "所有数据不能为空"}
    #     self.assertEqual(res, text, "test_login_no_passwd,测试失败")
    #
    # def test_login_no_name(self):
    #     res = login_check(password="123456")
    #     text = {"code": 1, "msg": "所有数据不能为空"}
    #     self.assertEqual(res, text, "test_login_no_name,测试失败")
    #
    # def test_login_all_no(self):
    #     res = login_check()
    #     text = {"code": 1, "msg": "所有数据不能为空"}
    #     self.assertEqual(res, text, "test_login_no_name,测试失败")


if __name__ == '__main__':
    unittest.main()
