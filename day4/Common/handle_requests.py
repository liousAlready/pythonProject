# -*- coding: utf-8 -*-
# @Time : 2021/11/22 14:44
# @Author : Limusen
# @File : handle_requets

import json
import requests
from day4.Common.my_logger import logger
from day4.Common.handle_excel import HandleExcel
from day4.Common.handle_config import conf


def send_requests(method, url, data=None, token=None):
    # # 得到请求头
    logger.info('发起一次HTTP请求')
    headers = __handle_heard(token)
    # 得到完整的url
    url = __pre_url(url)
    # 　如果是字符串，则转换成字典对象
    data = __pre_data(data)
    # 将请求数据转换成字典对象
    logger.info('请求头为:{}'.format(headers))
    logger.info('请求方法为:{}'.format(method))
    logger.info('请求url为:{}'.format(url))
    logger.info('请求数据为:{}'.format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理

    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    else:
        resp = requests.post(url, json=data, headers=headers)
    logger.info('响应状态码为:{}'.format(resp.status_code))
    logger.info('响应数据为:{}'.format(resp.json()))
    return resp


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


def __pre_url(url):
    """
    处理拼接接口的url地址
    :param url: url
    :return:
    """
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + '/' + url


def __pre_data(data):
    """
    如果data是字符串，则转换为字典对象
    :param data:
    :return:
    """
    if data is not None and isinstance(data, str):
        return json.loads(data)
    return data
