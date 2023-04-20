# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/13 22:44
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm21_继承的注意事项.py
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

class Cat(Animal):

    def catch(self):
        print("catch")
#
tom = Cat()
tom.eat()
tom.run()
tom.drink()
tom.sleep()
tom.catch()
# cat类和xiaoqianquan类之间没有继承关系
tom.fly()
