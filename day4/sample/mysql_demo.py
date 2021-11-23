# -*- coding: utf-8 -*-
# @Time : 2021/11/23 15:15
# @Author : Limusen
# @File : mysql_demo

"""

mysql数据库:pymysql
pip install pymysql

数据库操作步骤:
1.连接数据库
2.执行sql语句
3.获取执行的结果
4.关闭数据库连接

"""

import pymysql

# 1.建立连接

conn = pymysql.connect(
    host="mysql.yaoweilai.cn",
    port=3306,
    user="root",
    password="123456",
    database="yaoweilai_common",  # 库名
    charset="utf8",  # 字符集
    cursorclass=pymysql.cursors.DictCursor  # 结果切换为字典输出
)

# 2.创建游标
cur = conn.cursor()

# 3.执行sql语句
# sql = "select * from `user`"
sql = "select id from `user`  limit 5 ;  "
count = cur.execute(sql)  # 查询到结果的条数
# print(count)

# 4.获取sql语句执行之后的结果
one = cur.fetchone()  # 获取结果中的一条
print("第一条数据：", one)
two = cur.fetchone()
print("第二条数据：", two)
print("=======================")
# 获取所有的结果
all = cur.fetchall()
print("获取所有数据：", all)
