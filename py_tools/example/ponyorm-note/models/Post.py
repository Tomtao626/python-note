#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: Post.py 
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.gggg.net
@software: PyCharm 
"""

from datetime import datetime
from pony.orm import PrimaryKey, Required, Optional, LongStr, Set
from db.db_conf import pony_db


class Post(pony_db.Entity):
    """post"""
    post_pk = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Optional(LongStr)
    published_at = Required(datetime, default=datetime.now())
    categories = Set("Category")
    comments = Set("Comment")
