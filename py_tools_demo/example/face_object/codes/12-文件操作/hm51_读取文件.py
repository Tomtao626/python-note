# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 20:16
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm51_读取文件.py
'''
# 打开文件
file = open("README",encoding='utf-8')
# 读取
text = file.read()
print(text)
# 关闭
file.close()