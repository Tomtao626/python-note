import json
import time
import datetime
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# mysql pymysql.connect('localhost',user='',passwd='',db='')
dblist = myclient.list_database_names()  # 返回所有数据库的名称以列表的形式
print(dblist)  # ['admin', 'config', 'lianjia', 'local', 'scrapy']
# dblist = myclient.database_names()
if "storage" in dblist:
    print("数据库已存在！")
# 创建数据库，直接在连接mongodb的对象采用列表赋值
mydb = myclient["storage"]
collist = mydb.list_collection_names()
print('打印出数据库中的所有集合', collist)  # 打印出数据库中的所有集合 []
# collist = mydb.collection_names()
if "serv_pushfront_v1_2022_04_24" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")
mycol = mydb["serv_pushfront_v1_2022_04_24"]
clusterList = mycol.find().distinct("clustername")
# areaCodeList = mycol.find({"data.ReqBody.touser": {"$regex": "^((?!11111111111).)*$"}, "data.ReqBody.tagcode": "亚马逊短信",
#                            "data.Response.data.template.servertype": "awssms"}).distinct("data.ReqBody.touser")
areaCodeList = ["30", "56", "84", "852", "886", "218", "66", "90", "357", "40", "62", "973", "992", "55", "61", "92",
                "972", "998"]

l = []
for k1, v1 in enumerate(clusterList):
    v1_dict = dict()
    v1_list = list()
    v1_count = 0
    print(v1)
    dic = {}
    for k2, v2 in enumerate(areaCodeList):
        v2_count = 0
        v2_dict ={}
        lis_count = mycol.count_documents(
            {"data.ReqBody.touser": {"$regex": f"(?=^00{v2})(?=^((?!11111111111).)*$)"}, "clustername": v1, "data.ReqBody.tagcode": "亚马逊短信",
             "data.Response.data.template.servertype": "awssms"})
        if lis_count == 0:
            continue
        v2_dict.update({"countrycode": f"+{v2}", "count": lis_count})
        v1_list.append(v2_dict)
        v1_count += lis_count
    v1_dict.update({"clustername": v1, "list": v1_list, "totalcount": v1_count})
    dic.update({"reporttype": "month", "time": "2022-04", "savetimeunixnano": int(time.mktime(datetime.datetime.now().timetuple())), "name": "clustername_counter_country", "data": v1_dict})
    # l.append(dic)
    current_col = mydb["aws_cluster_counter_country"]
    current_col.insert_one(dic)

# print(json.dumps(l, ensure_ascii=False, indent=4))
# clustrejson = json.dumps(dic, ensure_ascii=False, indent=4)




