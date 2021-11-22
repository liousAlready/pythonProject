# -*- coding: utf-8 -*-
# @Time : 2021/11/19 17:40
# @Author : Limusen
# @File : resquest_cookies_jianquan


"""

Session类:创建一个会话对象

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

result = requests.post(url, json=params, headers=headers)
result_dict = result.json()
print(result.text)
token = result_dict["data"]["token"]
print(token)

# 将token添加到请求头当中
headers["Authorization"] = "Bearer {}".format(token)
params = {"userPhone": "", "userName": "", "pageIndex": 1, "pageSize": 10, "identity": "BackGroundUser"}
get_list_url = "http://userback.yaoweilai.cn:88/api/gateway/system/backGroundUser/pageList"
# 获取内部人员列表接口的值
resp = requests.post(get_list_url, json=params, headers=headers)
print(resp.json())
