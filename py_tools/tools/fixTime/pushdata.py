# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: pushdata
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-03-16 14:14
    Project: tools
    IDE: PyCharm
"""
import ujson


def fix_data():
	"""
	解析数据
	"""
	with open("english.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


TotalList = fix_data()
print(len(TotalList))
for tmp1 in TotalList:
	print(11)
	print(f"-----------{tmp1['country']}----------")
	if tmp1['country'] == "China mainland":
		for tmp2 in tmp1['children']:
			print(22)
			print(f"-----------{tmp2['province']}----------")
			# if tmp2['province'] == "Wyoming":
			for tmp3 in tmp2['subchildren']:
				tmp3.update({"timezone": "Asia/Shanghai"})
		print(ujson.dumps(tmp1['children'], ensure_ascii=False).replace('\/', "/"))

