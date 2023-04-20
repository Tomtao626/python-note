# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: main
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-10 11:34
    Project: tools
    IDE: PyCharm
"""


class People(object):
	"""
	people class
	"""

	def __init__(self, height):
		self.height = height

	def get_height(self):
		return self.height

print(People.get_height)

