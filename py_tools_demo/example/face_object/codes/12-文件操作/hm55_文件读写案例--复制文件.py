# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 20:47
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm55_文件读写案例--复制文件.py
'''

# 1.打开文件
file_read= open("README")
file_write = open("README[复件]","w")

# 2.读写文件
text = file_read.read()
file_write.write(text)

# 3.关闭文件
file_read.close()
file_write.close()