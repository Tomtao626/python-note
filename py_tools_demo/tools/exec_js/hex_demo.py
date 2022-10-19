# coding:utf-8

import binascii

a = b'worker'
# 先把worker转换成二进制数据然后在用十六进制表示
b = binascii.b2a_hex(a)
print(b)
# 与b2a_hex相反
print(binascii.a2b_hex(b))
# 这个功能和b2a_hex()一样
c = binascii.hexlify(a)
print(c)
# 这个功能和a2b_hex()一样
print(binascii.unhexlify(c))
