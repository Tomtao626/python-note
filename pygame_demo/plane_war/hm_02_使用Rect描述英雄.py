# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/22 23:23
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm_02_使用Rect描述英雄.py
'''
import pygame

hero_rect = pygame.Rect(100,500,120,125)

print("英雄的原点 %d %d"% (hero_rect.x,hero_rect.y))
print("英雄的尺寸 %d %d"% (hero_rect.width,hero_rect.height))
print("%d %d"% hero_rect.size)