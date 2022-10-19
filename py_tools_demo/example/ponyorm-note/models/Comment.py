#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: Comment.py 
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.gggg.net
@software: PyCharm 
"""
from datetime import datetime
from pony.orm import Required, Optional
from db.db_conf import pony_db
from models.Post import Post


class Comment(pony_db.Entity):
    """comment"""
    post = Optional(Post)
    content = Required(str)
    published_at = Required(datetime, default=datetime.now())