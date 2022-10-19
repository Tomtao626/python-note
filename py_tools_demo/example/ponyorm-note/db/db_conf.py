#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: db_conf.py 
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.gggg.net
@software: PyCharm 
"""

from pony import orm

# 创建数据库对象
pony_db = orm.Database()
# 建立数据库连接
pony_db.bind(provider='mysql', host='localhost', user='user', passwd='password', db='pony_db')


# 官方文档地址
# https://docs.ponyorm.org/