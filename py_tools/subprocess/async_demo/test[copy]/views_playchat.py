# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/12 0:03
User   : Administrator
Product  : PyCharm
Project  : chatroom_project
File   : views_playchat.py
'''
import tornado.web

class PlayChatHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="弹幕列表"
        )
        self.render("playchat.html",data=data)