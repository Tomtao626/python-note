# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: single_threading_demo
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-06 15:13
    Project: tools
    IDE: PyCharm
"""
import threading

balance = 0


def change_it_without_lock(n):
	global balance
	for i in range(1000000):
		balance = balance + n
		balance = balance - n
	print(balance)


threads = [
	threading.Thread(target=change_it_without_lock, args=(8,)),
	threading.Thread(target=change_it_without_lock, args=(10,)),
	threading.Thread(target=change_it_without_lock, args=(10,)),
	threading.Thread(target=change_it_without_lock, args=(4,))
]

[t.start() for t in threads]
[t.join() for t in threads]

print(balance)

"""
	多线程在未加锁的情况下，连最终一致性也无法保证，因为线程是系统态切换，
	虽然同时只能有一个线程执行，但切换过程是争抢的，也就会导致写操作被原子性覆盖，
	而协程虽然在手动切换过程中也无法保证状态一致，但是可以保证最终一致性呢？因为协程是用户态，
	切换过程是协作的，所以写操作不会被争抢覆盖，会被顺序执行，所以肯定可以保证最终一致性
"""