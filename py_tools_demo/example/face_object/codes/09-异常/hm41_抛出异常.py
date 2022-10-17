# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 18:01
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm41_抛出异常.py
'''
def input_paswd():

    # 1.提示用户输入密码
    pwd = input("请输入密码：")

    # 2.判断密码长度》=8，返回用户输入的密码
    if len(pwd)>=8:
        return pwd

    # 3.如果密码长度<8，主动抛出一异常
    print("主动抛出异常")
    # 1> 创建异常对象 *args 多值的元组数据
    ex = Exception("密码长度不够")
    # 2> 主动抛出异常
    raise ex


try:
    print(input_paswd())
except Exception as result:
    print("未知错误%s" % result)
else:
    print("执行成功")
finally:
    print("无论是否出现异常都执行finally")