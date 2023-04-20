import json
import requests

dir_list = ["awsprice.json", "twilioprice.json", "tencent.json"]


def read_json(filepath):
	with open(filepath, 'r', encoding='utf-8') as fr:
		codejson = json.load(fr)
	for i in codejson:
		i['price'] = float(i['price'])
	return codejson


def write_json(filepath):
	with open(filepath, 'a') as fw:
		json.dump(swb_codejson, fw, ensure_ascii=False)
		fw.write('\n')


json_list_one = read_json(dir_list[0])
json_list_two = read_json(dir_list[1])
json_list_thr = read_json(dir_list[1])



#
dic = {}
for i in json_list_one:
	for j in json_list_two:
		for k in json_list_thr:
			sub_dic = {}
			if i['areacode'] == j['areacode'] == k['areacode']:
				info_dic = {}
				current_score = 6.4015
				info_dic['aws'] = round(i['price']*current_score, 4)
				info_dic['tw'] = round(j['price']*current_score, 4)
				info_dic['tencent'] = float(k['price'])
				sub_dic['price_info'] = info_dic
				min_key = min(info_dic, key=lambda x: info_dic[x])
				sub_dic['price_min'] = min_key
				dic[f"{i['areacode']}"] = sub_dic
# tencent数据 price字段类型转换 string -> float
# for i in json_list_two:
# 	i['price'] = float(i['price'])
with open('result.json', 'a', encoding='utf-8') as fw:
	json.dump(dic, fw, ensure_ascii=False)



import re
import json
import urllib.request

url = "https://api.it120.cc/gooking/forex/rate?fromCode=CNY&toCode=USD"
resp = requests.get(url)
print(resp.json())

