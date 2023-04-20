# -*- coding: utf-8 -*-
"""
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/22 23:37
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm_04_绘制图像.py
"""
import pygame

pygame.init()

sceen = pygame.display.set_mode((480,700))

# 绘制背景图像
#     1 加载数据
bg = pygame.image.load("./images/background.png")
#     2 blit绘制图像
sceen.blit(bg,(100,100))
#     3 update更新屏幕提示
pygame.display.update()

while True:
    pass

pygame.quit()
