import requests
import json

from unidecode import unidecode

URL = "https://irmanage.ibroadlink.com"
headers = {
    'requserid': '002439249f192996bb183cac9f6b313f',
    'loginsession': 'a30f3e15534aLRR50De6aiZIc96Kq24tQGJPTmhQtIUfpN2X4HbrpymKssS4IbLGdM9MXB4ULvcGxN'
}
channel_name = ""
# url = URL + "/irmanage/v1/manager/channel/list"
# get_brandid_url = URL + "/irmanage/v1/manager/brand/list"
# req = requests.post(get_brandid_url, data=json.dumps({"name": ""}), headers=headers, verify=False)
# get_brandid_rel = json.loads(req.text)
# if get_brandid_rel['total'] > 0:
#     print(get_brandid_rel['result'])


# data = {
#     "name": '',
# }
# req = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
# rel = json.loads(req.text)
# print(len(rel['result']))
    # if unidecode(i['name']).lower() == unidecode(channel_name).lower():
    # print({"status": 0, "error": 0, "msg": "ok", "channel_id": i["id"]})

# 获取键位映射关系
# get_function_map_url = URL + "/irmanage/v1/manager/funckeys/list"
# req = requests.get(get_function_map_url, headers=headers, verify=False)
# get_function_map_rel = json.loads(req.text)
# for i in get_function_map_rel['result']:
#     print(i)

# get country list
get_countrycode_url = URL + "/irmanage/v1/manager/area"
get_countrycode_data = {
    "type": "getcountry",
    "keyword": ''
}
req = requests.post(get_countrycode_url, headers=headers, data=json.dumps(get_countrycode_data),
                    verify=False)
get_countrycode_rel = json.loads(req.text)
for i in get_countrycode_rel['data']:
    print(i)

# group list
# groupid_channel_list_url = URL + "/irmanage/v1/manager/operator/channelgroup"
# req = requests.post(groupid_channel_list_url, data=json.dumps({"id": 2345}), headers=headers,
#                     verify=False)
# groupid_channel_list_rel = json.loads(req.text)
# for i in groupid_channel_list_rel['result']['channels']:
#     print(i)