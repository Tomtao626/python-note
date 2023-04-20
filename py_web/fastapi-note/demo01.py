#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/18 3:00
# @Author : Tom_tao
# @Site : 
# @File : demo01.py
# @Software: PyCharm

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return {"msg": "HelloWorld,FastAPI"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)
