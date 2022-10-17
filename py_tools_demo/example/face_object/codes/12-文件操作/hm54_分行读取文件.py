# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 20:44
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm54_分行读取文件.py
'''
file= open("README")

while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)

file.close()