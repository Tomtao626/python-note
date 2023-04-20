# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 20:28
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm52_read方法和文件指针.py
'''
# open the file
file = open("README",encoding='utf-8')# 注意文件的unicode编码
# 当open文件出现 UnicodeDecodeError: 'gbk' codec can't decode byte 0x81 in position 59: incomplete multibyte sequence 时，
# 请在其后添加 encoding='utf-8'

# read the file of everything
text = file.read()

print(text) #打印输出所有文件内容
print(len(text)) # 打印输出文件的长度51

print("--"*20)
# 当文件被open时，文件指针会默认指向该文件的起始位置，执行read操作后，文件指针会从开头走向文件末尾，这时文件指针指向文件末尾
# 所以再次执行read操作，并没有输出任何内容

text = file.read()
print(text)# 没有文件内容输出
print(len(text)) # 输出 0，因为上次执行read操作后，文件指针已指向末尾，没有内容了


# close the file
file.close()