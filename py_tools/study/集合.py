# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao

#集合
list_1 = [1,3,4,2,6,8]
list_1 = set(list_1)

list_2 = set([5,4,7,89,6,67])
print(list_1,list_2)
'''
#交集
print(list_1.intersection(list_2))

#并集
print(list_1.union(list_2))

#差集 in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_2.difference(list_1))

#子集
list_3 = set([1,3,8])
print(list_3.issubset(list_1))#z子集 --list_3是list_1的子集
print(list_1.issuperset(list_3))#父集 --list_1是list_3的父集

#对称差集
print(list_1.symmetric_difference(list_2))#去掉二者交集，留下剩余的

print('-----------------------------------')

list_4 = set([5,6,7,8])
#print(list_3.isdisjoint(list_4))#isdisjoint--脸啊这之间没有交集返回为真，反之为假
'''
print(list_1 & list_2)#交集

print(list_2 | list_1)#并集

print(list_1 - list_2)#差集

print(list_1 ^ list_2)#对称差集

list_1.add(999)
list_1.update([88,99,66])
print(list_1)

print(list_1.pop())#任意删除
print(list_1.pop())

print(list_1.remove(88))
print(len(list_1))#求集合的长度、
