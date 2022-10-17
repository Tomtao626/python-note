# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com
Datetime : 2019/10/18 22:10
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm33_new方法.py
'''
class MusicPlayer(object):
    # 创建对象，new方法会被自动调用
    def __new__(cls, *args, **kwargs):
        print("分配空间，对象初始化")

        # 为对象分配空间
        instance = super().__new__(cls)

        #返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")

musicplayer = MusicPlayer()
print(musicplayer)