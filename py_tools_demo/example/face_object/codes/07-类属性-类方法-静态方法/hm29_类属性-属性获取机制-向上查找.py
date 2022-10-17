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


# 1.在python中属性的获取存在一个向上查找机制
# 2.首先在对象内部查找对象属性，没有找到就会向上查找类属性
# print(Tool.count)
# 因此，要访问类属性有两种方式：
# 1. 类名.类属性
# 2. 对象.类属性(不推荐)
# 如果使用对象.类属性赋值语句，只会给对象增加一个属性，而不会影响到类属性的值

tool1.count = 89

print(tool1.count) # 89 使用类名.类属性赋值语句，只会修改当前类对象的值，
print(Tool.count) # 3  修改对类本身的类属性并不起作用