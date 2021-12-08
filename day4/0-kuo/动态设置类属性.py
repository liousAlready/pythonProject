# -*- coding: utf-8 -*-
# @Time : 2021/11/26 16:30
# @Author : Limusen
# @File : 动态设置类属性


class AABB:
    pass


# setattr,hasattr,getattr,delattr


setattr(AABB, "name", "hello")

print(AABB.name)

print(AABB.__dict__)

s = "111"
# 转成字典才能迭代
values = dict(AABB.__dict__.items())
print(values)
for key, value in values.items():
    if key.startswith("__"):
        pass
    else:
        delattr(AABB, key)

print(AABB.__dict__)
