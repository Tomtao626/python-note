# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao

import time

def logger():
    time_format = '%Y-%m-%d-%X'
    time_current = time.strftime(time_format)#引用time_format的时间格式
    with open('shabi.txt','a+') as f:
        f.write('%s end action\n'%time_current)

def test1():
    print("in the text1")
    logger()

def test2():
    print("in the text2")
    logger()
def test3():
    print("in the text3")
    logger()

test1()
test2()
test3()