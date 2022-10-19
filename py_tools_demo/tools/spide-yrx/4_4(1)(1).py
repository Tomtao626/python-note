import random
import requests
import time

url = "http://http.tiqu.letecs.com/getip3?num=400&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
target_url = 'https://www.python-spider.com/api/challenge4'
headers = {
    'User-Agent':'yuanrenxue.project'
}
proxies_list = []
result = requests.get(url=url).json()['data']
print(result)
for item in result:
    ips = item['ip']
    port = item['port']
    ipss = ips + ":" + str(port)
    # print(ipss)
    ip_proxies = {
        "http": f"http://{ipss}",
        "https": f"https://{ipss}"
    }
    proxies_list.append(ip_proxies)
print(proxies_list)

page = 1
value_list = []
while(page<101):
    proxies = random.choice(proxies_list)
    data = {
        'page': page
    }
    try:
        time.sleep(2)
        print(proxies)
        resp = requests.post(url=target_url,headers=headers,data=data,proxies=proxies,timeout=5,verify=False).json()
        print(resp)
        data_list = resp['data']
        for item in data_list:
            item_data = int(item['value'].strip())
            value_list.append(item_data)
        page += 1
    except:
        print('error')

    print(sum(value_list))

