# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: main
    Github: https://github.com/Tomtao626/django-real-estate
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-05-26 23:44
    Project: django-real-estate
    IDE: PyCharm
"""
l = [-6, -6, 100, 64, -85, -107, -3, -74, 1, -82, -100, 72, 53, 103, 91, -113, -53, 50, -55, -123, 44, -54, 26, -59,
     -18, -24, 37, -7, -77, -61, 86, 44]

b = bytes(i % 256 for i in l)
c = bytearray(b)
print(list(c))