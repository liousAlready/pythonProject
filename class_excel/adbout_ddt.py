# -*- coding: utf-8 -*-
# @Time : 2021/11/18 14:43
# @Author : Limusen
# @File : adbout_ddt


from ddt import ddt, data
import unittest


@ddt
class TestAbd(unittest.TestCase):

    @data([[1, 2, 3], [4, 5, 6]])
    def test_add(self, case):
        print("测试")
        print(case)

    my_dict = {"name": "xj", "age": 18}.items()

    @data(*my_dict)
    def test_add(self, case):
        print("测试")
        print(case)


if __name__ == '__main__':
    unittest.main()
