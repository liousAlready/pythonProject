# -*- coding: utf-8 -*-
# @Time : 2021/11/24 15:48
# @Author : Limusen
# @File : random_utils

"""

1.随机生成11位升级好 前3位+8位
2.进行数据校验

"""

import os
import random
from day4.Common.handle_db import HandleDb
from day4.Common.handle_config import conf
from day4.Common.handle_requests import send_requests

prefix = [133, 149, 153, 173, 177, 180, 181, 189, 199,
          130, 131, 132, 145, 155, 156, 166, 171, 175,
          176, 185, 186, 166, 134, 135, 136, 137, 178,
          139, 147, 150, 151, 151, 152, 157, 158, 159,
          172, 178, 182]


def get_new_phone():
    db = HandleDb()

    while True:
        # 1.生成
        phone = __generator_phone()
        # nub = str(phone)
        # print(type(nub))
        # print(nub)
        # 2.校验
        count = db.select_count("select id from back_ground_user where user_phone = {};".format(phone))
        if count == 0:  # 如果手机号码没有在数据库查到.表示是未注册的号码
            db.close()
            return phone


def get_old_phone():
    """
    从配置文件中获取制定用户名和密码
    确认此账号,在系统当中是注册了的
    :return: 账号跟密码
    """
    user = conf.get("user", "user")
    password = conf.get("user", "password")
    # 如果数据库查找到user,就直接返回 ,如果没有则调用注册接口
    # 不管注册与否,直接调用注册接口
    send_requests("post","/ss",user)





def __generator_phone():
    index = random.randint(0, len(prefix) - 1)
    phone = str(prefix[index])

    for i in range(0, 8):
        phone += str(random.randint(0, 9))

    return str(phone)


# print(__generator_phone())


# def check_phone_in_db(phone):
# # 如果手机号码存在,ok,如果不存在,则重新生成
#     pass
#
# print(__generator_phone())

# print(get_new_phone())
