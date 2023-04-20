import requests

url = "http://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/index.html"
resp = requests.get(url)
print(resp.text)
