# -*- coding: utf-8 -*-
"""
encoding: utf-8
Author  : tom_tao626@163.com
Datetime : 2019/10/18 22:24
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm34_单例.py
"""
class MusicPlayer(object):
    # 定义一个类属性
    instance = None

    def __new__(cls, *args, **kwargs):

        # 判断类属性是否是空对象
        if cls.instance == None:
            # 为类属性分配空间
            cls.instance = super().__new__(cls)
        # 返回对象的引用
        return cls.instance

m1 = MusicPlayer()
print(m1)

m2 = MusicPlayer()
print(m2)