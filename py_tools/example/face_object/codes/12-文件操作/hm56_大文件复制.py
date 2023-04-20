# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 20:51
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm56_大文件复制.py
'''
# open
file_read = open("README")
file_write = open("README[复件]","w")

# read and write
while True:
    # 按行读取
    text = file_read.readline()
    # 判断是否读取到内容
    if not text:
        break
    file_write.write(text)

# close
file_read.close()
file_write.close()