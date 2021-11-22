# -*- coding: utf-8 -*-
# @Time : 2021/11/22 15:56
# @Author : Limusen
# @File : demo

'''
基于项目做定制化封装
1.鉴权
2.通用的请求头设置
3.请求体格式:application/json
'''
import requests


def __handle_header(token=None):
    '''
    处理请求头,加上项目当中必要的请求头,如果有token,加上token
    :param token:token值
    :return:处理之后的headers字典
    '''
    headers = {'X-Lemonban-Media-Type': 'lemonban.v2',
               'Content-Type': 'application/json'}
    # 判断是否传入token值,如果传了,将token值写入Authorization中
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def send_requests(method, url, data=None, token=None):
    # 得到请求头
    headers = __handle_header(token)
    # 根据请求类型,调用请求方法
    if method.upper() == 'GET':
        resp = requests.get(url, params=data, headers=headers)
    elif method.upper() == 'POST':
        resp = requests.post(url, json=data, headers=headers)
    return resp


if __name__ == '__main__':
    login_url = "http://api.lemonban.com/futureloan/member/login"
    login_datas = {"mobile_phone": "18600001112", "pwd": "123456789"}
    resp = send_requests('post', login_url, login_datas)
    token = resp.json()["data"]["token_info"]["token"]
    print(token)

    # recharge_url = 'http://api.lemonban.com/futureloan/member/recharge'
    # recharge_data = {'member_id': '1236900867', 'amount': 2000}
    # resp = send_requests('post',recharge_url,recharge_data,token)
    # print(resp.json())
