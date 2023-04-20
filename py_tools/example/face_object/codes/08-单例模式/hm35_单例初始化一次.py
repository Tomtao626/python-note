# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/18 22:32
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm35_单例初始化一次.py
'''
class MusicPlayer(object):

    # 定义一个类属性
    instance = None

    # 定义一个类属性 标记初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance ==None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 如果没有执行过，在执行初始化动作
        print("播放器初始化")
        # 修改初始化状态的标记
        MusicPlayer.init_flag = True

musicplayer1 = MusicPlayer()
print(musicplayer1)

musicplayer2 = MusicPlayer()
print(musicplayer2)
