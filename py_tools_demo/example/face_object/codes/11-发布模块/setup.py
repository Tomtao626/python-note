# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 19:33
User   : Administrator
Product  : PyCharm
Project  : codes
File   : setup.py
'''
# 导入setup函数
from distutils.core import setup

setup(
    name="hm_message", # 包名
    version="1.0", # 版本
    description="hm发送和接收消息模块", # 完整描述信息
    author="tomtao", #作者
    author_email="tom_tao626@163.com", # 作者邮箱
    url="www.tomtao.top", #主页
    py_modules = ["hm_message.send_message",
                  "hm_message.receive_message"]
)