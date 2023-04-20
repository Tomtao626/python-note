# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 18:21
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm44_import导入模块.py
'''
import hm42_测试模块1
import hm43_测试模块2

hm42_测试模块1.say_hello()
hm43_测试模块2.say_hello()

dog = hm42_测试模块1.Dog()
print(dog)

cat = hm43_测试模块2.Cat()
print(cat)