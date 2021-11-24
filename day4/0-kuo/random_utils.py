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
        # 2.校验
        count = db.select_count("select id from back_ground_user where user_phone = '{}'};".format(phone))
        if count == 0:  # 如果手机号码没有在数据库查到.表示是未注册的号码
            db.close()
            return phone



def __generator_phone():
    index = random.randint(0, len(prefix) - 1)
    phone = str(prefix[index])

    for i in range(0, 8):
        phone += str(random.randint(0, 9))

    return phone

# print(__generator_phone())


# def check_phone_in_db(phone):
# # 如果手机号码存在,ok,如果不存在,则重新生成
#     pass

print(get_new_phone())