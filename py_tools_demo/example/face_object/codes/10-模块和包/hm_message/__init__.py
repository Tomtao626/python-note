# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 19:22
User   : Administrator
Product  : PyCharm
Project  : codes
File   : __init__.py.py
'''
from . import receive_message
from . import send_message

# 要在外界使用包中的模块，需要在__init__.py中指定对外界提供的模块列表

# 从当前目录导入模块列表
# from . import receive_message
# from . import send_message