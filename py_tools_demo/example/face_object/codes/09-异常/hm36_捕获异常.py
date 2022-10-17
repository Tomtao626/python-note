# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 16:44
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm36_捕获异常.py
'''


try:
    num = int(input("请输入一个整数:"))
except:
    print("请输入一个正常的整数!")

print("-"*40)