# -*- coding: utf-8 -*-
# @Time : 2021/11/22 11:05
# @Author : Limusen
# @File : request_zentoa_cookies


import requests

s = requests.Session()
print(s.cookies)

url = "http://192.168.31.200/zentao/user-login.html"

