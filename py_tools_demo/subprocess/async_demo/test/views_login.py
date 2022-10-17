# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/12 0:23
User   : Administrator
Product  : PyCharm
Project  : chatroom_project
File   : views_login.py
'''
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="登录"
        )
        self.render("login.html", data=data)