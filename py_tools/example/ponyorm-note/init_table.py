#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: init_table.py 
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""
from pony.orm import set_sql_debug

from db.db_conf import pony_db
# 生成mapping并建表
pony_db.generate_mapping(create_tables=True)
# create_tables=True代表 如果Post和Category,Comment没有对应的表，Pony会帮你在数据库建表，在generate_mapping之前必须要有实体，否则会报错。
# 设置debug模式，看pony帮我们生成的sql语句
set_sql_debug(True)
