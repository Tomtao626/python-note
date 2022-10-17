# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/13 22:58
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm22_方法的重写_覆盖父类的方法.py
'''
class Animal:
    def run(self):
        print("run")

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def drink(self):
        print("drink")


class Dog(Animal):

    def bark(self):
        print("bark")


class Xiaotianquan(Dog):

    def fly(self):
        print("fly")

    def bark(self):
        print("bark 666")

tom = Xiaotianquan()
tom.bark()
'''
重写父类方法有两种情况：
1.覆盖父类的方法
2.对父类方法进行扩展

1）。覆盖父类的方法
    如果在开发中，父类的方法实现和子类的方法实现，完全不同
    就可以使用覆盖的方式，在子类中重新编写父类的方法实现
        具体的实现方式，就相当于在子类中定义了一个和父类同名的方法并实现
    重写之后，在运行时，只会调用子类中重写的方法，而不会调用父类封装的方法
'''

