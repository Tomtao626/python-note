# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: async_lock_demo
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-06 14:41
    Project: tools
    IDE: PyCharm
"""

import asyncio
"""
    balance = 0
    
    
    async def change_it_without_lock(n):
        global balance
        balance = balance + n
        balance = balance - n
    
        print(balance)
    
    
    loop = asyncio.get_event_loop()
    
    res = loop.run_until_complete(
        asyncio.gather(change_it_without_lock(10), change_it_without_lock(5), change_it_without_lock(11),
                       change_it_without_lock(6)))
    print(res)
    print(balance)
"""


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
"""
	当我们执行第一句代码print("Hello world!")之后，使用await关键字让出使用权，也可以理解为把程序“暂时”挂起，
	此时使用权让出以后，别的协程就可以进行执行，随后当我们让出使用权1秒之后，当别的协程任务执行完毕，
	又或者别的协程任务也“主动”让出了使用权，协程又可以切回来，继续执行我们当前的任务，也就是第二行代码print("Hello again!")。
"""

