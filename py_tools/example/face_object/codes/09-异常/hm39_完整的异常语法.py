# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 17:11
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm38_捕获未知错误.py
'''
try:
    num = int(input("please a inter num:"))
    result = 8/num
    print(result)
except Exception as result:
    print("ukonwn error %s " % result)
else:
    print("try success，只有try下面的程序执行通过，即没有出现异常，才会执行")
finally:
    print("无论是否出现异常都会执行finally下面的程序")