# -*- coding: utf-8 -*-
# @Time : 2021/11/25 10:25
# @Author : Limusen
# @File : json_path


"""
$	根元素
@	当前元素
*	通配符，可以表示任何元素
..	递归搜索
.	子节点（元素）
['' (, '')]	一个或者多个子节点
[ (, )]	一个或者多个数组下标
[start:end]	数组片段，区间为[start,end)
[?()]	过滤器表达式，其中表达式结果必须是 boolean 类型，如可以是比较表达式或者逻辑表达式

链接：http://testingpai.com/article/1595507145193

安装: pip install jsonpath

使用方式:

jsonpath.jsonpath(字典对象,jsonpath表达式)


"""
import json
import jsonpath

res = {
    "code": "100001",
    "desc": "成功",
    "success": True,
    "data": {
        "token": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJpZFwiOjEsXCJ1c2VyTmFtZVwiOlwiYWRtaW5cIixcInVzZXJQaG9uZVwiOlwiMTMyNTIyNTQ5OTJcIixcInVzZXJHZW5lcmF0ZUNvZGVcIjo4MDU4NTM3MDcxMTc3NDA4NTExLFwicG9ydHJhaXRVcmxcIjpudWxsLFwiaWRlbnRpdHlcIjpudWxsLFwibGFzdExvZ2luVGltZVwiOlwiMjAyMS0xMS0yNSAxMDozMTowOFwiLFwicm9sZUlkXCI6NCxcImFjdGl2YXRpb25cIjpudWxsfSIsInJvbGVJZCI6NCwiaXNzIjoidmFsaWQiLCJleHAiOjE2Mzc4Mjk0NzYsInVzZXJJZCI6ODA1ODUzNzA3MTE3NzQwODUxMSwiaWF0IjoxNjM3ODA3ODc2LCJqdGkiOiI4MDU4NTM3MDcxMTc3NDA4NTExIn0.SEDJH1188s0YtF4fVd9HkTzKtfk6dni2UWUQD5IlLI8",
        "activation": "擦擦实打实大傻傻的"
    }
}

# $.data.token  一个.通配符  第一个字典对象,第二个jsonpath表达式
# 返回值,列表,存放匹配到的值
rrr = jsonpath.jsonpath(res,"$.data.token")
print(rrr)

# ..不分层级  $..token
rrs = jsonpath.jsonpath(res,"$..activation")
print(rrs)

