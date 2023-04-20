# !/usr/bin/env python
# -*- coding:utf-8 -*-

# def logging(func):
#     logging.warn("%s is running" % func.__name__)
#     func()
#
# def foo():
#     print('I am foo')
#
# logging(foo)

# def my_sum(x,y):   #函数名   x,y是参数
#     res = x + y  #函数体
#     return res   #返回值  无参数时，默认返回None
#
# # 调用函数
# print(my_sum(2,3))

import time
# 测试函数运行时间
# def log(func):
#     def warpper(*args,**kwargs):
#         # print("begin call %s" % func.__name__)
#         print('log')
#         temp = func(*args,**kwargs)
#         # print("after call %s" % func.__name__)
#         return temp
#     return warpper

def log(text):
    def decortator(func):
        def warpper(*args, **kwargs):
            # print("begin call %s" % func.__name__)
            print(text)
            temp = func(*args, **kwargs)
            # print("after call %s" % func.__name__)
            return temp
        return warpper
    return decortator
# 运行时间
# 有返回值
# def my_time(func):
#     def warpper(*args,**kwargs):
#         # s_time = time.time()
#         print('time')
#         temp = func(*args,**kwargs)
#         # e_time = time.time()
#         # print("%耗时s%s秒" % (func.__name__ ,(e_time-s_time)))
#         return temp
#     return warpper

@log('taopeng')  # ---->@decortator
# @my_time # => f = my_time(f)
def f(x,y):  # 函数也是一个变量
    # print('I am f')
    # time.sleep(2)
    return x

n = f('i am hah',1)
print('n =', n)
# n = my_time(f)
# f = n
#f()

# n = f
#
# n()


# def new_f():
#     s_time = time.time()
#     f()
#     e_time = time.time()
#     print('耗时%s' % (e_time-s_time))

# #f()
# new_f()