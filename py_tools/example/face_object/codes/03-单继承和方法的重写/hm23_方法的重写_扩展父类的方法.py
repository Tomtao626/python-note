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
        # 针对子类特有的需求，编写代码
        print("bark 666")
        #使用super(). 调用原本在父类中封装的方法
        # super().bark()

        # 父类名.方法(self)
        Dog.bark(self)
        # 注意：如果使用子类调用方法,会出现递归调用--死循环
        # Xiaotianquan.bark(self)

        #增加其他子类的代码
        print("wdnmd")

tom = Xiaotianquan()
tom.bark()
'''
重写父类方法有两种情况：
1.覆盖父类的方法
2.对父类方法进行扩展

2).对父类方法进行扩展

如果在开发中，子类的方法实现中包含父类的方法实现
    父类原本封装的方法实现是子类方法的一部分
    就可以使用扩展的方法
    
    1.在子类中重写父类的方法
    2.在需要的位置使用super().弗雷方法 来调用父类方法的执行
    3.代码的其他位置针对子类的需求，编写子类特有的代码实现
    
    关于super
        在python中super是一个特殊的类
        super()就是使用super类创建出来的对象
        最常使用的场景就是在重写父类方法时，调用在父类中封装的方法实现
'''


