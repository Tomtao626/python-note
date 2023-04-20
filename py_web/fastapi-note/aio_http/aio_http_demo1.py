#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/28 5:00 下午
# @Author : admin
# @Software: PyCharm
# @File: aio_http_demo1.py

import requests


def hello():
    response = requests.get("http://httpbin.org/get")
    return response


print(hello().text)
text = {
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.25.1",
    "X-Amzn-Trace-Id": "Root=1-6143fff6-0c6e96c80f1ebd8a3c4a00f9"
  },
  "origin": "13.70.19.199",
  "url": "http://httpbin.org/get"
}
