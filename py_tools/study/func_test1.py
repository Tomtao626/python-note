# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao
#函数式编程
def test1():
    print("haha")
    return 0

#面向过程编程
def test2():
    print("aaaa")

x = test1()#x接受test1的返回值 0
y = test2()#y没有返回值，所以为none
#1.面向过程是没有返回值的函数式编程

print('from test1 return is %s'%x)
print('from test2 return is %s'%y)