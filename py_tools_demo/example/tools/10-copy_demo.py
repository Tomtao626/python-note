#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/13 20:08
# @Author : Tom_tao
# @Site : 
# @File : 拷贝.py
# @Software: PyCharm

# a = [1,[2,3],4]
# b = a[::]
#
# a[0] = 5
# print("----1----")
# print(id(a))
# print(id(b))
#
# a[1][1] = 10
# print("----2----")
# print(id(a))
# print(id(b))

# import copy
#
# a = [1,2,3,[99,88]]
#
# b = a.copy()
# a.append(77)
#
# print(a,id(a))
#
# print(b,id(b))
#
# print("-----")
#
# b = copy.deepcopy(a)
# print(a,id(a))
# print(b,id(b))


print(sum(range(1, 101)))
print(int((1+100)*100/2))
print(sum([i for i in range(101)]))
print(sum([i for i in range(1, 101)]))
n = 100
print(int(((1+n)*n/2)))