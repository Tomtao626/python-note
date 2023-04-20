#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/28 5:03 下午
# @Author : admin
# @Software: PyCharm
# @File: aio_http_demo2.py

import ujson
import asyncio
from aiohttp import ClientSession


# 异步获取响应  异步读取内容
async def hello():
    async with ClientSession() as session:
        # 访问结束 关闭请求
        async with session.get("http://httpbin.org/headers") as response:
            response = await response.read()
            print(ujson.loads(response))


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
