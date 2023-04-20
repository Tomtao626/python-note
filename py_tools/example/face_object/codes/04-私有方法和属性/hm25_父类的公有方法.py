# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/17 23:05
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm24_父类的私有属性和私有方法.py
'''
class A:
    def __init__(self):
        self.num1=100
        self.__num2=200
    def __test(self):
        print("私有方法 %d %d"%(self.num1, self.__num2))
    def test(self):
        print("父类的公有方法")
        print("父类的私有方法%d"%self.__num2)
        self.__test()

class B(A):

    def demo(self):

        # 1.在子类的对象方法中，不能访问父类的私有属性
        # print("访问傅雷的私有属性%d"% self.__num2)

        # 2.在子类的对象方法中，不能调用父类的私有方法
        # self.__test()

        print("子类方法 %d "% self.num1)

        self.test()
        pass
b = B()
b.test()
# b.num1
# 在外界不能直接访问对象的私有属性、调用私有方法
# b.__num2
# b.__test()