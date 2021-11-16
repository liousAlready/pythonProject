# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/15 8:38 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : pythonProject
# File      : demo2.py
# explain   : 文件说明


class People:

    def __init__(self, name):
        self.name = name


p = People("xa")
# print(p.name)
#
# p.name= "黄花菜"
# print(p.name)
#
# #  添加类属性
# p.sex = "女"
# print(p.sex)


# hasattr 判断是否有这个属性
res = hasattr(People, "name")
print(res)

res = hasattr(p, 'name')
print(res)
# getattr 获取类属性
res = getattr(p,'name')
print(res)

# setattr 设置属性值
setattr(People,'age',15)
print(People.age)

# # delattr 删除属性
# delattr(People,'age')
# print(People.age)