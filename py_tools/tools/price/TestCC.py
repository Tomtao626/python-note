import json
import requests
from pyquery import PyQuery as pq
import requests
from lxml import etree

url = "https://cloud.tencent.com/document/product/382/18051"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
resp = requests.get(url, headers=headers)
html = etree.HTML(resp.text)
tx_code_list = html.xpath('//table[2]/tbody/tr/td/text()')
tx_list = [tx_code_list[i: i+5] for i in range(0, len(tx_code_list), 5)]
print([{'code': i[2], 'areacode': f"+{i[3]}", 'price':float(i[4])} for i in tx_list])