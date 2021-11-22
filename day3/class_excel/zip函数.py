# -*- coding: utf-8 -*-
# @Time : 2021/11/18 16:39
# @Author : Limusen
# @File : zip函数


li1 = ['user', 'passwrod', 'check']
li2 = ['test', '123456', '{"code": 0, \'msg\': "登录成功"}']

res = zip(li1, li2)
print(dict(res))
