# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 18:40
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm46_from_import导入.py
'''
from hm42_测试模块1 import Dog
from hm42_测试模块1 import say_hello
# 打入模块中某一个工具，函数，类，局部导入

say_hello()
dog = Dog()
print(dog)