# -*- coding: utf-8 -*-
# @Time : 2021/11/19 17:20
# @Author : Limusen
# @File : about_requests


"""

1.接口地址
2.请求方法
3.请求参数
4.请求头

get: param

没有请求体,param就是追加在url后面的参数


post: data,json
请求体
data: 字典.对应的默认body格式  application/x-www-form-unlencoded
json: 字典.对应的默认body格式 application/json

{
"loginInfoDto":
    {"phone":"13252254992","pass":"254992","type":"BackGroundUser","loginType":"LoginPass"}
}

"""

import requests

url = "http://userback.yaoweilai.cn:88/api/gateway/system/v2/login"

params = {
    "loginInfoDto":
        {"phone": "13252254992", "pass": "254992", "type": "BackGroundUser", "loginType": "LoginPass"}
}

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

result = requests.post(url=url, json=params, headers=headers)

# 　响应状态码
print(result.status_code)
#  响应头
print(result.headers)
# 响应体
print(result.text)
# # 　响应体转换成python的字典
# body_j = result.json()
# print("===================================")
# print(body_j)
# print(type(body_j))
