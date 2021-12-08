# -*- coding: utf-8 -*-
# @Time : 2021/11/23 15:42
# @Author : Limusen
# @File : handle_db


import pymysql
from day4.Common.handle_config import conf

"""

数据库操作步骤:
1.连接数据库
2.执行sql语句
3.获取执行的结果
4.关闭数据库连接

"""


class HandleDb:

    def __init__(self):
        # 连接数据库,创建游标
        self.conn = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=3306,
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),  # 库名
            charset="utf8",  # 字符集
            cursorclass=pymysql.cursors.DictCursor  # 结果切换为字典输出
        )

        # 2.创建游标
        self.cur = self.conn.cursor()

    def select_one_data(self, sql):
        self.conn.commit()  # 同步处理
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_count(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self, sql):
        """
        :param sql: 增删改的操作
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    # sql = "select * from `user` ;"
    # ss = HandleDb().get_one_data(sql)
    # print(ss)

    from day4.Common.handle_requests import send_requests

    db = HandleDb()
    sql = "select id from back_ground_user where user_phone = 15574866554;"
    token_case = {
        "method": "POST",
        "url": "/api/gateway/system/v2/login",
        "request_data": {"loginInfoDto": {"phone": "13252254992", "pass": "254992", "type": "BackGroundUser",
                                          "loginType": "LoginPass"}}
    }

    token = send_requests(token_case['method'], token_case['url'], token_case['request_data'])  # 接口
    result_dict = token.json()
    login_token = result_dict["data"]["token"]

    case = {
        "method": "POST",
        "url": "/api/gateway/system/backGroundUser/addBackGroundUser",
        "request_data": {"userName": "123", "userPhone": "15574866554", "userPass": "", "identity": "BackGroundUser",
                         "roleId": 1, "userGenerateCode": ""}
    }
    # 　发起创建用户的请求
    response = send_requests(case['method'], case['url'], case['request_data'], login_token)
    print("响应结果：", response.json())

    # 查询创建的用户
    count = db.select_count(sql)
    print("获取到的结果：", count)
