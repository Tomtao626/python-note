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
        print("test-A")

    def demo(self):
        print("demo-A")


class B:

    def demo(self):
        print("demo-B")

    def test(self):
        print("test-B")

class C(A,B):
    '''
    C继承于A和B两个父类，拥有A和B两个父类的所有属性和方法
    '''
    pass

c = C()

c.test()
c.demo()
'''
MRO-方法搜索顺序，主要用于在多继承时判断方法、属性的调用路径
在搜索方法时，是按照__mro__的输出结果从左至右的顺序查找的
如果在当前类中找到方法，就直接执行，不再搜索
如果没有找到，就查找下一个类中是否有对应的方法，如果找到，就直接执行
如果找到最后一个类，还没有找到方法，程序报错
'''
print(C.__mro__)