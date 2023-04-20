# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 18:36
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm45_import导入时指定别名.py
'''
import hm42_测试模块1 as DogMoudle
import hm43_测试模块2 as CatMoudle

DogMoudle.say_hello()
CatMoudle.say_hello()

dog = DogMoudle.Dog()
print(dog)

cat = CatMoudle.Cat()
print(cat)