# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 17:43
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm40_异常的传递.py
'''

def demo1():
    return int(input("请输入一个整数"))

def demo2():
    return demo1()
try:
    print(demo2())
except Exception as result:
    print("unkonwn error %s "% result)