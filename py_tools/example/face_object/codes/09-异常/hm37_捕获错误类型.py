# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 17:02
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm37_捕获错误类型.py
'''
try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数:"))
    result = 8/num
    print(result)
except ZeroDivisionError:
    print("除0错误!")
except ValueError:
    print("请输入一个整数!")