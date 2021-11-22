# -*- coding: utf-8 -*-
# @Time : 2021/11/19 17:40
# @Author : Limusen
# @File : resquest_cookies_jianquan


"""

Session类:创建一个会话对象

"""

import requests

# 第一步 创建对象
s = requests.Session()
print("登录之前的cookies:", s.cookies)
# 第二步 登录,得到cookies鉴权

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

result = s.post(url, json=params, headers=headers)

# print("登录响应的cookies:", result.cookies)
#
# print("登录之后的cookies:", s.cookies)  # 主动会将响应的set-cookies添加到s对象当中.

# 主动获取cookies
cookies = result.cookies
print(cookies)

# 　第二部：获取用户信息

get_list_url = "http://userback.yaoweilai.cn:88/api/gateway/system/backGroundUser/pageList"

resp = requests.post(get_list_url,cookies=cookies)
print(resp.json())