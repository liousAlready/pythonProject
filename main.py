import os
import unittest
from test_deom.test_login import TestLogin

# 1. 实例化测试套件 TestSuite
# s = unittest.TestSuite()

# # 添加一个用例
# s.addTest(TestLogin("test_login_ok"))
# # 添加一群用例
# s.addTests([TestLogin("test_login_ok"),TestLogin("test_login_wrong_passwd",)])

# 从start_directory这个目录下开始，搜索所有的测试用例，并加载到测试套件当中
# 1.制定搜索目录
# 2.有子包，需要指定文件过滤规则：文件名匹配 test*.py
# 3.在文件当做过滤用例：集成了unittest.TestCase类的测试类，类当中以test_开头的测试函数


s=unittest.TestLoader().discover("/Users/lishouwu/PycharmProjects/pythonProject/test_deom")
print(type(s))
print(s)

# # 运行测试用例并生成结果
# runner = unittest.TextTestRunner()
# runner.run(s)



