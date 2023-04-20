# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/12 0:30
User   : Administrator
Product  : PyCharm
Project  : chatroom_project
File   : views_userprofile.py
'''

import tornado.web

class UserProfileHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = dict(
            title="个人资料"
        )
        self.render("userprofile.html", data=data)