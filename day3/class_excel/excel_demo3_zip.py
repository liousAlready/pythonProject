# -*- coding: utf-8 -*-
# @Time : 2021/11/18 16:43
# @Author : Limusen
# @File : workbook

import os
from openpyxl import load_workbook

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login_cases.xlsx')
# print(file_path)

all_data = []

# 　1.加载excel数据文件
wb = load_workbook(file_path)
# 　2.根据表单名称选择表单
sh = wb['login']

# 1.拿到字典的key值: 第一行
titles = []
for item in list(sh.rows)[0]:  # 遍历第一行的每一列
    titles.append(item.value)
# print(titles)

for item in list(sh.rows)[1:]:  # 遍历数据行
    values = []
    for val in item:  # 获取每一行的值
        values.append(val.value)
    res = dict(zip(titles, values))  # title和每一行数据,打包成字典
    all_data.append(res)

print(all_data)

wb.close()  # 关闭工作簿

# @ddt
# class TestLogin(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print("======单个用例执行=======")
#
#     def tearDown(self) -> None:
#         print("======单个用例结束=======")
#
#     @data(*all_data)
#     def test_login(self, case):
#         # 1.测试数据 　2.测试步骤
#         res = login_check(case['user'], case['password'])
#         # 3.断言
#         self.assertEqual(res, case['check'], "test_login_ok,测试失败")
#
#
# if __name__ == '__main__':
#     unittest.main()
