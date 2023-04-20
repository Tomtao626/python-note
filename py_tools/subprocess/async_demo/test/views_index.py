# -*- coding: utf-8 -*-
# Author  : tom_tao626@163.com >
# Datetime : 2019/9/8 19:45
# User   : Administrator
# Product  : PyCharm
# Project  : chatroom_project
# File   : views_index.py

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    # 定义一个get请求的方法
    def get(self, *args, **kwargs):
        # self.write("<h1>这是一个弹幕视频+在线聊天的项目!</h1>")
        data = dict(
            title="视频列表"
        )
        self.render("index.html", data=data)