# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/16 23:30
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm32_方法综合案例.py
'''

class Game(object):

    # 历史最高分 是一个类属性 定义类属性，在class下方，使用赋值语句即可
    top_score = 0

    # 玩家姓名 是一个实例属性，实例属性应该在实例初始化方法内部定义
    def __init__(self,player_name): #player_name是一个形参
        self.player_name = player_name
    #静态方法
    @staticmethod
    def show_help():
        print("1.请查看游戏帮助信息:让僵尸进入大门！")
    #类方法
    @classmethod
    def show_top_score(cls):
        print("2.游戏最高分是%d分" % cls.top_score)
    # 实例方法
    def start_game(self):
        print("3.%s,游戏开始了"% self.player_name)

# 1.查看游戏帮助信息
Game.show_help()
# 2.查看游戏历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("Tom_tao")
game.start_game()

# 1.实例方法--方法内部需要访问实例属性
    # 实例方法内部可以使用类名.访问类属性
# 2.类方法--方法内部只需要访问类属性
# 3.静态方法--方法内部，不需要访问实例属性和类属性，应该定义实例方法
    # 因为类只有一个，在实例方法内部可以使用类名.访问类属性。

