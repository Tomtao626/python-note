# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: main
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-06-15 16:32
    Project: tools
    IDE: PyCharm
"""
import json

import pandas as pd


file_list = ["codestr_0k_1k.json"]

csv_path = "json/codestr_22k_23k.json"

def fix_data(csv_path):
	"""
	解析数据
	@return:
	"""
	with open(csv_path, "r", encoding="utf-8") as fr:
		sread = json.load(fr)
	return sread, csv_path.replace(".json", "")

data_list, save_path = fix_data(csv_path)
res = []
for k, v in enumerate(data_list):
	if v["brand"]:
		print(k)
		# if v.get('name') == "电视":
		print(v.get('brand'))
		if v.get('model'):
			print(v.get('model'))
		cur_dict = {
			"brand": v.get('brand'),
			"model": v.get('model') if v.get('model') else v.get('elecModel'),
			"type": '电视',
		}
		res.append(cur_dict)
		# elif v.get('brand') == '空调':
		# 	print(v.get('brand'))
		# 	if v.get('model'):
		# 		print(v.get('model'))
		# 	cur_dict = {
		# 		"brand": v.get('brand'),
		# 		"model": v.get('model') if v.get('model') else v.get('elecModel'),
		# 		"type": '空调',
		# 	}
		# 	res.append(cur_dict)
		# else:
		# 	continue
	else:
		continue

print(res)
# 重命名字段
_rename_dict = {
	'brand': '品牌',
	'model': '型号',
	'type': '品类'
}
res_df = pd.DataFrame(res)
res_df = res_df.rename(columns=_rename_dict)
res_df.index += 1
# 文件保存
save_path = f"E:\program\workspaces\pywork\\tools\ircode_brand_model\excel\\{save_path}.xlsx"
res_df.to_excel(save_path, index=False, encoding="utf-8", sheet_name='sheet1')
