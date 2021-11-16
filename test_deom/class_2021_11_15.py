# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/15 9:24 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : pythonProject
# File      : class_2021_11_15.py
# explain   : 文件说明


def login_check(username=None, password=None):
    if username != None and password != None:
        if username == "test" and password == "123456":
            return {"code": 0, 'msg': "登录成功"}
        else:
            return {"code": 1, 'msg': "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有数据不能为空"}

# s = login_check("test","123456")
#
# if s == {"code":0, 'msg':"登录成功"}:
#     print("用例通过")
# else:
#     print("用例失败")
