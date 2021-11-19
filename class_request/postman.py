# -*- coding: utf-8 -*-
# @Time : 2021/11/19 17:16
# @Author : Limusen
# @File : postman


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

response = requests.post(url, params, headers)
