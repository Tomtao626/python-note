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

    def __init__(self,name):
        self.name = name
        # 针对类属性做一个数量+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("desk")
tool2 = Tool("table")
tool3 = Tool("ruler")


print(tool1.count)