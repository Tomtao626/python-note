#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/24 8:10 下午
# @Author : admin
# @Software: PyCharm
# @File: demo2.py


from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'hello': 'HI...'})


@app.get("/{item_id}/")
async def item_id(request: Request, item_id):
    return templates.TemplateResponse('index.html', {'request': request, "item_id": item_id})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
