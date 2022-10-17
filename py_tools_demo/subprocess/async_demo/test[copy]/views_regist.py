# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/9/12 0:15
User   : Administrator
Product  : PyCharm
Project  : chatroom_project
File   : views_regist.py
'''

import tornado.web

# 注册视图
class RegistHandler(tornado.web.RequestHandler):
    # 定义GET请求方法
    def get(self,*args,**kwargs):
        data = dict(
            title = "注册"
        )
        self.render("regist.html", data=data)