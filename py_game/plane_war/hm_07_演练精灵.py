# -*- coding: utf-8 -*-
"""
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/25 23:16
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm_07_演练精灵.py
"""
import pygame
from plane_sprites import *

# 游戏的初始化
pygame.init()

# 游戏的窗口创建 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以在所有绘制工作完成之后，同意调用update()方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏训话 意味着游戏正式开始
while True:
	# 指定循环体内代码执行的频率
	clock.tick(60)

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
	if hero_rect.y <= 0:
		hero_rect.y = 700

	# 绘制背景图片
	screen.blit(bg, (0, 0))

	# 绘制英雄图像
	screen.blit(hero, hero_rect)

	# 让精灵组调用两个方法
	# update 让组中的所有精灵更新位置
	enemy_group.update()

	# draw 在screen上绘制所有的精灵
	enemy_group.draw(screen)

	# 更新显示
	pygame.display.update()

pygame.quit()
