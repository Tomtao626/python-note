import time

import ujson
import requests


def download_data():
	"""
	download pushfront data from faq
	"""
	ls = [[0, 100], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900],
	      [900, 1000]]
	s = 1
	for i in ls:
		url = "https://faqsupport-deu.ibroadlink.com/dataquery/cybereye/queryissue"
		req_body = {"servicename": "serv_pushfront_v1", "start": "2021-10-20_00:00:00", "end": "2021-11-18_00:00:00",
		            "queryCondition": [{"key": "tagcode", "value": "亚马逊短信", "type": "input"}], "offset": i[0],
		            "step": i[1]}
		headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36"}
		resp = requests.request('POST', url, data=ujson.dumps(req_body), headers=headers).json()
		s += 1
		with open(f"/broadlink-s/data/{s}.json", 'a',
		          encoding='utf-8') as fw:
			ujson.dump(resp, fw, ensure_ascii=False)
		time.sleep(5)


def fix_data(num):
	"""
	解析数据
	"""
	with open(f"./data/{num}.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


for i in range(2, 3):
	sDict = fix_data(i)
	print(f"-------{i}-------"*10)
	print(sDict)
	for k, v in enumerate(sDict['results']):
		print(k, v)
