#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: Category.py 
@time: 2020/12/11
@contact: tp320670258@gmail.com
@site: xxxx.gggg.net
@software: PyCharm 
"""

from pony.orm import PrimaryKey, Set
from db.db_conf import pony_db


class Category(pony_db.Entity):
    """category"""
    name = PrimaryKey(str)
    comments = Set("Post")
