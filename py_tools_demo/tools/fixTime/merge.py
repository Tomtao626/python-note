# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: merge
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-03-18 09:15
    Project: tools
    IDE: PyCharm
"""
import random
import time
import json
import ujson


def fix_data_chn():
	"""
	解析数据
	"""
	with open("chinese.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


def fix_data_eng():
	"""
	解析数据
	"""
	with open("english.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


chn_list = fix_data_chn()
eng_list = fix_data_eng()
merge_list = []
for chn_k, chn_v in enumerate(chn_list):
	print(f"{chn_k}-----{chn_v['country']}")
	for chn_k2, chn_v2 in enumerate(chn_v['children']):
		print(f"{chn_k2}-----{chn_v2['province']}")
		for eng_k, eng_v in enumerate(eng_list):
			if chn_v['code'] == eng_v['code']:
				print(f"{eng_k}-----{eng_v['country']}")
				for eng_k2, eng_v2 in enumerate(eng_v['children']):
					if chn_v2['code'] == eng_v2['code']:
						if "subchildren" not in chn_v2.keys():
							continue
						eng_v2['subchildren'] = chn_v2['subchildren']
				eng_v['children'] = chn_v['children']
			merge_list.append(eng_v)
# print(merge_list)
# dic = ujson.dumps(tmp1, ensure_ascii=False).replace('\/', "/")
with open(f'city-timezone-english.json', 'a', encoding='utf-8') as fw:
	json.dump(merge_list, fw, ensure_ascii=False)
