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

class Tool(object):

    # 使用赋值语句创建类属性，记录工具类实例化对象的数量
    count = 0

    # 创建一个类方法
    @classmethod
    def show_tool_count(cls):
        # 在类方法内部，可直接使用cls访问类属性和调用类方法
        print("the tool's num is %s " % cls.count)
# 类方法需要使用@classmethod来标识，告诉解释器这是一个类方法
# 类方法的第一个参数应该是cls
# 由哪一个类调用的方法，方法内的cls就是哪一个类的引用
# 这个参数和实例方法的第一个参数self相似，当然用其他名称也可以
# 通过类名.调用类方法时，不需要传递cls参数
    def __init__(self,name):
        self.name = name
        # 针对类属性做一个数量+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("desk")
tool3 = Tool("ruler")
# 调用类方法
tool3.show_tool_count()



