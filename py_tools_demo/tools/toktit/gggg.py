"""
@version:1.0
@file: test.py
@time: 2021/12/4-19:16

@desc:
@spider_url：
"""
import time
import requests
import brotli

def dy_search(keyword):
    url = 'https://search100-search-quic-hl.amemv.com/aweme/v1/search/item/?os_api=23&device_type=Nexus%206P&ssmix=a' \
           '&manifest_version_code=110502&dpi=560&app_name=aweme&version_name=11.5.1&ts=1637139393&cpu_support64=true' \
           '&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=11519900&channel=wandoujia_douyin&_rtic' \
           'ket=1637139393649&device_platform=android&iid=1592535192703646&version_code=110501&mac_address=AC%3ACF%3A' \
           '85%3ACA%3A14%3AB6&cdid=c1735fea-ca38-426d-907c-58ff152dbd81&openudid=c2e7eae7720965ec&device_id=265689549' \
           '9779827&resolution=1440*2392&os_version=6.0.1&language=zh&device_brand=google&aid=1128'
    headers = {
        'content-length': '222',
        "accept-language": "zh-CN,zh;q=0.9",
        "Content-Type": "text/html; charset=utf-8",
        'x-ss-req-ticket': '1637139393647',
        'sdk-version': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-ss-dp': '1128',
        'user-agent': 'com.ss.android.ugc.aweme/110502 (Linux; U; Android 6.0.1; zh_CN; Nexus 6P; Build/MTC20L; Cronet'
                      '/TTNetVersion:3c28619c 2020-05-19 QuicVersion:0144d358 2020-03-24)',
        'accept-encoding': 'gzip, deflate, br',
        'x-khronos': '1637139393'
    }

    for i in range(1, 5):
        data1 = {
            'keyword': f'{keyword}',
            'offset': '0',
            'count': f'{i * 10}',
            'source': 'video_search',
            'search_source': 'switch_tab',
            'is_pull_refresh': '1',
            'hot_search': '0',
            'query_correct_type': '1',
            'is_filter_search': '0',
            'sort_type': '0',
            'publish_time': '0',
            'enter_from': 'homepage_hot'
        }
        ret = requests.post(url=url, headers=headers, data=data1).content
        print(brotli.decompress(ret))
        time.sleep(5)


dy_search('蜘蛛')
