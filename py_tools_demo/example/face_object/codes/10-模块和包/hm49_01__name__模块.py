# -*- coding: utf-8 -*-
'''
encoding: utf-8
Author  : tom_tao626@163.com >
Datetime : 2019/10/20 19:12
User   : Administrator
Product  : PyCharm
Project  : codes
File   : hm49_01__name__模块.py
'''
def say_hello():
    print("你好你好，我是say_hello()")

# 如果直接执行模块,输出 __main__
if __name__ == "__main__":
    print(__name__)

    #文件被导入时，能够直接执行的代码
    print("小明开发的模块")
    say_hello()

    # __name__属性可以做到，测试模块的代码旨在测试情况下执行，而在被导入时不会执行