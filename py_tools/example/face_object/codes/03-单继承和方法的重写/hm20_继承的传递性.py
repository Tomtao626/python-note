# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/13 22:33
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm20_继承的传递性.py
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

# 子类拥有父类以及父类的父类中封装的所有属性和方法

tom = Xiaotianquan()
tom.bark()
tom.sleep()
tom.fly()
tom.drink()
tom.run()
tom.eat()