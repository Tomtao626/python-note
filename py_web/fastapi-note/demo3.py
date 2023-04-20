#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 12:56 下午
# @Author : admin
# @Software: PyCharm
# @File: demo3.py

from fastapi import FastAPI, Form
import uvicorn
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.post("/users/")
async def from_text(request: Request, username: str = Form(...), password: str = Form(...)):
    print("username", username)
    print("password", password)
    return templates.TemplateResponse('index2.html', {'request': request, 'username': username, 'password': password})


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse('post.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)
