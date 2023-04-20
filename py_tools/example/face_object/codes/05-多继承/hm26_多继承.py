# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/19 22:19
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm26_多继承.py
'''

class A:

    def test(self):
        print("A")


class B:

    def demo(self):
        print("B")

class C(A,B):
    '''
    C继承于A和B两个父类，拥有A和B两个父类的所有属性和方法
    '''
    pass

c = C()

c.test()
c.demo()