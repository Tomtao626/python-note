# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao

def calc(n):
     print(n)
     if int(n/2) > 0:
         return calc(int(n/2))
     print('-->',n)

calc(100)