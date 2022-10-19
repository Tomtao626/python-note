import json


def read_json(filepath):
	with open(filepath, 'r', encoding='utf-8') as fr:
		codejson = json.load(fr)
	return codejson


result = list()
for i in read_json("demo.json"):
	print(i['name'])
	result.append(i['name'])
sorted(result)
