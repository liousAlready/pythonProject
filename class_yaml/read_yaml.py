# -*- coding: utf-8 -*-
# @Time : 2021/11/19 16:46
# @Author : Limusen
# @File : read_yaml


import yaml

with open("nmb.yaml",encoding="utf-8") as fs:
    data = yaml.load(fs,yaml.FullLoader)
    print(data)
    for key,value in data.items():
        print(key)
        print(value)