# -*- coding: utf-8 -*-
# @Time : 2021/11/22 13:10
# @Author : Limusen
# @File : request封装


"""

基于项目做的定制化封装
1.鉴权  token
2.项目通用的请求头
3.请求体格式

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Accept": "application/json, text/plain, */*"
    }

"""
import requests


def __handle_heard(token=None):
    """
    处理请求头,加上项目中必带的其你去,如果有token,则加上token
    :param token: token值
    :return: 处理之后的headers值
    """
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Accept": "application/json, text/plain, */*"
    }
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def send_requests(method, url, data=None, token=None):
    """
    处理请求信息
    :param method: get或者post方法
    :param url:
    :param data: 字典
    :param token:
    :return: 查询结果
    """
    # 得到请求头
    headers = __handle_heard(token)
    # 根据请求类型,调用请求方法
    if method.upper() == "GET":
        response = requests.get(url, params=data, headers=headers)
    elif method.upper() == "POST":
        response = requests.post(url, json=data, headers=headers)

    return response


if __name__ == '__main__':
    url = "http://userback.yaoweilai.cn:88/api/gateway/system/v2/login"
    params = {
        "loginInfoDto":
            {"phone": "13252254992", "pass": "254992", "type": "BackGroundUser", "loginType": "LoginPass"}
    }
    # 获取token
    resp = send_requests('post', url, params)
    token = resp.json()["data"]["token"]

    # 查询列表
    data = {"userPhone": "", "userName": "", "pageIndex": 1, "pageSize": 10, "identity": "BackGroundUser"}
    get_list_url = "http://userback.yaoweilai.cn:88/api/gateway/system/backGroundUser/pageList"
    query_list = send_requests("post", get_list_url, data=data, token=token)
    print(query_list.json())
