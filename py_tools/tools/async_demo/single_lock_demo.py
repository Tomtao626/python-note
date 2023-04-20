# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: main
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-06 09:51
    Project: tools
    IDE: PyCharm
"""

import threading

balance = 0


def change_it_without_lock(n):
	global balance
	"""
	不加锁的话 最后的值不是0
    线程共享数据危险在于 多个线程同时改同一个变量
    如果每个线程按顺序执行，那么值会是0， 但是线程时系统调度，又不确定性，交替进行
    没锁的话，同时修改变量
    #所以加锁是为了同时只有一个线程再修改，别的线程表一定不能改
	"""
	for i in range(10000):
		balance = balance + n
		balance = balance - n


def change_it_with_lock(n):
	global balance
	"""
	lock
	"""
	if lock.acquire():
		try:
			for i in range(10000):
				balance = balance + n
				balance = balance - n
		finally:
			# 这里的finally 防止中途出错了，也能释放锁
			lock.release()


threads = [
	threading.Thread(target=change_it_with_lock, args=(8,)),
	threading.Thread(target=change_it_with_lock, args=(10,))
]

lock = threading.Lock()

if __name__ == '__main__':
	[t.start() for t in threads]
	[t.join() for t in threads]
	print(balance)
