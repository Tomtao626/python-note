# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: async_switch_dmeo
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-06 14:59
    Project: tools
    IDE: PyCharm
"""

import asyncio

balance = 0


async def change_it_without_lock(n):
	global balance
	balance = balance + n
	await asyncio.sleep(1)
	balance = balance - n
	print(balance)

loop = asyncio.get_event_loop()

res = loop.run_until_complete(
	asyncio.gather(change_it_without_lock(10), change_it_without_lock(2), change_it_without_lock(9),
	               change_it_without_lock(4)))

print(balance)

"""
	当我对全局变量balance进行加法运算后，主动释放使用权，让别的协程运行，随后立刻切换回来，再进行减法运算，如此往复，同时开启四个协程任务
	协程运行过程中，并没有保证“状态一致”，也就是一旦通过await关键字切换协程，变量的状态并不会进行同步，从而导致执行过程中变量状态的“混乱状态”，
	但是所有协程执行完毕后，变量balance的最终结果是0，意味着协程操作变量的最终一致性是可以保证的。
"""