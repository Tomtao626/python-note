# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/19 23:47
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm27_多态案例.py
'''
class Dog:

    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s"%self.name)

class Xiaotianquan(Dog):

    def game(self):
        print("%s"%self.name)

class Person(object):

    def __init__(self,name):
        self.name=name

    def game_with_dog(self,dog):
        print("%s and %s"%(self.name,dog.name))
        dog.game()


# tom = Dog("tom")
tom = Xiaotianquan("fly_dog")

liming = Person("liming")

liming.game_with_dog(tom)