# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/13 22:10
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm19_使用继承开发动物和狗.py
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
# 子类拥有父类的所有的属性和方法
Tom = Dog()
Tom.eat()
Tom.run()
Tom.drink()
Tom.sleep()
Tom.bark()