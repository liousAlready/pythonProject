# -*- coding: utf-8 -*-
# @Time : 2021/11/24 17:15
# @Author : Limusen
# @File : handel_data

"""

1.一条用例涉及到的数据当中,有url/request_data/check_sql

2.多条用例涉及到的数据


"""
from day4.Common.handle_excel import HandleExcel


def replace_mark_with_data(case, mark, real_data):
    """
    遍历一个http请求用户涉及到的所有数据,如果说每一个数据有需要替换的,都会替换
    :param case: excel当中读取出来一条,是一个字典
    :param mark: 数据当中的占位符,替换参数 需要是字符串 #xxx#  #值#
    :param real_data: 实际替换的值  需要是字符串
    :return:
    """
    for key, value in case.items():
        if value is not None and isinstance(value,str):
            if value.find(mark) !=-1:
                case[key] = value.replace(mark,real_data)

    return case


if __name__ == '__main__':
    case = {
        "request_data": '{"loginInfoDto": {"phone": "#phone#", "pass": "#phone#"}'
    }
    phone = replace_mark_with_data(case,"#phone#","1557455")
    print(phone)
