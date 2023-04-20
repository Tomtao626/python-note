# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/16 22:31
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm28_类属性.py
'''

class Dog(object):

    # 使用@staticmethod来标识，告诉python解释器这是一个静态方法
    def run():
        print("the dog is running")
# 如果在类中封装一个方法，这个方法不需要访问实例属性或者调用实例方法，也不需要访问类属性或者调用类方法，
# 这个时候需要把这个方法封装成一个静态方法

# 通过类名. 调用静态方法
Dog.run()