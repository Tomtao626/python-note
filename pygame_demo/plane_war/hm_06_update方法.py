# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/22 23:52
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm_06_update方法.py
'''
import pygame

pygame.init()

screen = pygame.display.set_mode((480,700))

# 绘制背景图像
#     1 加载数据
bg = pygame.image.load("./images/background.png")
#     2 blit绘制图像
screen.blit(bg,(0,0))
#     3 update更新屏幕提示
# pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))


clock = pygame.time.Clock()
# 定义英雄的初始位置
hero_rect = pygame.Rect(150,500,102,126)
i = 0

# 可以在所有绘制工作完成以后，统一更新
# pygame.display.update()

while True:

    # 指定循环体内的代码执行的频率
    clock.tick(60)

    # # 捕获事件
    # event_list = pygame.event.get()
    # if len(event_list):
    #     print(event_list)

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否为退出事件
        if event.type == pygame.QUIT:
            print("游戏退出！")
            # pygame卸载所有模块
            pygame.quit()

            exit()

    # 更新英雄的位置
    hero_rect.y -= 1

    # 如果移出屏幕，则将英雄的顶部移动到屏幕顶部
    if hero_rect.y <=0:
        hero_rect.y = 700

    # 绘制背景图片
    screen.blit(bg,(0,0))

    # 绘制英雄图像
    screen.blit(hero,hero_rect)

    # 更新显示
    pygame.display.update()

pygame.quit()