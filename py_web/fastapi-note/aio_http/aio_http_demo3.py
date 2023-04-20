#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/28 5:16 下午
# @Author : admin
# @Software: PyCharm
# @File: aio_http_demo3.py

# 异步请求花瓣网
import ujson
import asyncio
from aiohttp import ClientSession


async def fetch(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            # return response.read()  # 打印  [<coroutine object ClientResponse.read at 0x10e29bcc8>] [<coroutine object ClientResponse.read at 0x10e29bcc8>, <coroutine object ClientResponse.read at 0x10e29bdc8>]
            return await response.read()


'''
    response.read()是一个异步操作，这意味着它不会立即返回结果，仅仅返回生成器。
    这些生成器需要被调用跟运行，但是这并不是默认行为。在Python34中加入的yield from以及Python35中加入的await便是为此而生。
    它们将迭代这些生成器。以上代码只需要在response.read()前加上await关键字即可修复。
'''


async def run(loop, r):
    url = 'https://huaban.com/favorite/beauty/?k7162g1h&max=%' + str({}) + '&limit=20&wfl=1'
    tasks = []
    for i in range(r):
        task = asyncio.ensure_future(fetch(url.format(i)))
        tasks.append(task)
        # responses = asyncio.gather(*tasks)
        responses = await asyncio.gather(*tasks)
        print(
            responses)  # 打印 <_GatheringFuture pending> <_GatheringFuture pending> <_GatheringFuture pending> <_GatheringFuture pending>


'''
    response.read()是一个异步操作，这意味着它不会立即返回结果，仅仅返回生成器。
    这些生成器需要被调用跟运行，但是这并不是默认行为。在Python34中加入的yield from以及Python35中加入的await便是为此而生。
    它们将迭代这些生成器。以上代码只需要在response.read()前加上await关键字即可修复。
'''


def print_responses(result):
    print(result)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(loop, 4))
loop.run_until_complete(future)
