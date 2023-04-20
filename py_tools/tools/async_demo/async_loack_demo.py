# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: async_loack_demo
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-06 15:33
    Project: tools
    IDE: PyCharm
"""

import asyncio

balance = 0


async def change_it_with_lock(n):
	async with lock:
		global balance

		balance = balance + n
		await asyncio.sleep(1)
		balance = balance - n

		print(balance)


lock = asyncio.Lock()

loop = asyncio.get_event_loop()

res = loop.run_until_complete(
	asyncio.gather(change_it_with_lock(10), change_it_with_lock(8),
	               change_it_with_lock(2), change_it_with_lock(7)))

print(balance)

"""
	  结论当然就是看使用场景，如果协程在操作共享变量的过程中，没有主动放弃执行权(await)，也就是没有切换挂起状态，那就不需要加锁，执行过程本身就是安全的；
	  可是如果在执行事务逻辑块中主动放弃执行权了，会分两种情况，如果在逻辑执行过程中我们需要判断变量状态，或者执行过程中要根据变量状态进行一些下游操作，则必须加锁，
	  如果我们不关注执行过程中的状态，只关注最终结果一致性，则不需要加锁。是的，抛开剂量谈毒性，是不客观的，给一个健康的人注射吗啡是犯罪，但是给一个垂死的人注射吗啡，那就是最大的道德，
	  所以说，道德不是空泛的，脱离对象孤立存在的，同理，抛开场景谈逻辑，也是不客观的，协程也不是虚空的，脱离具体场景孤立存在的，
	  我们应该养成具体问题具体分析的辩证唯物思想，只有掌握了辩证的矛盾思维才能更全面更灵活的看待问题，才能透过现象，把握本质。
"""