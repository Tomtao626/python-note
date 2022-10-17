# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 19:25
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm50_导入包.py
'''

import hm_message

hm_message.send_message.send_msg("hello")
txt = hm_message.receive_message.receive_msg()
print(txt)