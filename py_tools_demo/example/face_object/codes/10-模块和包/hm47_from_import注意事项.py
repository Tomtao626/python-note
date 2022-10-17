# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 18:44
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm47_from_import注意事项.py
'''
# 同名导入。后导入会覆盖先导入的工具

from hm42_测试模块1 import say_hello as say1
from hm43_测试模块2 import say_hello

# 会调用模块2中的say_hello()函数。如果想调用第一个say_hello()函数，
# 可使用 from hm42_测试模块1 import say_hello as say_hell01
say1()
say_hello()

# from_import 导入所有工具
from hm42_测试模块1 import *
from hm43_测试模块2 import *
# 但是这种导入方式，函数重名并没有任何提示，出现问题不方便排查