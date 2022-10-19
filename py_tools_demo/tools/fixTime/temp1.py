# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: temp1
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-03-17 16:29
    Project: tools
    IDE: PyCharm
"""
import random
import time
import json
import ujson
from typing import AnyStr
from pyquery import PyQuery as Pq
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def fix_data1():
	"""
	解析数据
	"""
	with open("temp1.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


def fix_data2():
	"""
	解析数据
	"""
	with open("temp1.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


# TotalList = fix_data()
# print(f"total-{len(TotalList)}")
# for tmp1_k, tmp1_v in enumerate(TotalList):
# 	print(f"-----------{tmp1_k}-{tmp1_v['country']}----------")
# 	for tmp2_k, tmp2_v in enumerate(tmp1_v['children']):
# 		print(f"----------{tmp2_k}-{tmp2_v['province']}----------")
# 		# if tmp2['province'] == "Wales":
# 		if tmp2_v['province'] == "others":
# 			status, timezone = crawl_page(tmp2_v['subchildren'][0]['city'])
# 		else:
# 			status, timezone = crawl_page(tmp2_v['province'])
# 		if not status:
# 			continue
# 		for tmp3 in tmp2_v['subchildren']:
# 			tmp3.update({"timezone": f"{timezone}"})
# 	print(ujson.dumps(tmp1_v['children'], ensure_ascii=False).replace('\/', "/"))
# 	print(f"----------{tmp1_v['country']}-----------已完成")
# 	# dic = ujson.dumps(tmp1, ensure_ascii=False).replace('\/', "/")
# 	with open(f'temp/{tmp1_k}-{tmp1_v["country"]}.json', 'a', encoding='utf-8') as fw:
# 		json.dump(tmp1_v, fw, ensure_ascii=False)


# TotalList = fix_data()
# print(len(TotalList))
# for tmp1 in TotalList:
# 	print(11)
# 	# print(f"-----------{tmp1['country']}----------")
# 	if tmp1['country'] == "United Kingdom":
# 		for tmp2 in tmp1['children']:
# 			print(22)
# 			print(f"-----------{tmp2['province']}----------")
# 			# if tmp2['province'] == "台湾":
# 			for tmp3 in tmp2['subchildren']:
# 				tmp3.update({"timezone": "Europe/London"})
# 		print(ujson.dumps(tmp1['children'], ensure_ascii=False).replace('\/', "/"))

