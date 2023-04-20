# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao
#局部变量

names = ['A','B','C']
def change_name():
    names[0] = '你是傻逼！'
    print('inside func',names)

change_name()
print(names)




'''
def change_name():
    global name
    name = 'Tom_Tao'

change_name()
print(name)
'''
# school = 'Oldboy.edu'
# def change_name(name):
#     global school
#     school = 'HBMY'
#     print("before change",name,school)
#     name = "Tom_Tao"  #局部变量，change_name函数是局部变量name的作用域
#     print("after change",name,school)
#
# print("school:",school)
# name  = 'tom_tao'
# change_name(name)
# print(name)
# print(school)
