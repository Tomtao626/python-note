# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: main
    Github: https://github.com/Tomtao626/tools
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2022-03-16 14:50
    Project: tools
    IDE: PyCharm
"""
import random
import time
import json
import ujson
from typing import AnyStr
from pyquery import PyQuery as Pq
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def crawl_page(province_name: str):
	"""

	@param province_name:
	@return:
	"""
	desired_capabilities = DesiredCapabilities.CHROME
	desired_capabilities["pageLoadStrategy"] = "none"
	chrome_options = webdriver.ChromeOptions()
	# 无窗口模式
	chrome_options.add_argument('--headless')
	# 禁止硬件加速，避免严重占用cpu
	chrome_options.add_argument('--disable-gpu')
	# 关闭安全策略
	chrome_options.add_argument("disable-web-security")
	# 禁止图片加载
	chrome_options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
	# 隐藏Chrome正在受到自动软件的控制
	chrome_options.add_argument('disable-infobars')
	# no sandbox
	chrome_options.add_argument('--no-sandbox')
	# 设置开发者模式启动，该模式下webdriver属性为正常值
	chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

	browser = webdriver.Chrome(options=chrome_options,
	                           executable_path="/Users/tao626/Documents/workspaces/selenium_driver_path/mac/chromedriver")

	browser.get(f"https://time.is/{province_name}")

	doc = Pq(browser.page_source)
	time.sleep(random.randint(2, 5))
	if not doc:
		return False, ""
	cur_timezone = doc('.infobox').text()
	fix_timezone = cur_timezone.split(" ")[-1].replace(".", "")
	print("current timezone------------", fix_timezone)
	return True, fix_timezone


def fix_data():
	"""
	解析数据
	@return:
	"""
	with open("city.json", "r", encoding="utf-8") as fr:
		sread = ujson.load(fr)
	return sread


country_list = ['新西兰']
TotalList = fix_data()
print(f"total-{len(TotalList)}")
print(f"now-{len(country_list)}")
for tmp1_k, tmp1_v in enumerate(TotalList):
	if tmp1_v['country'] not in country_list:
		continue
	print(f"-----------{tmp1_k}-{tmp1_v['country']}----------")
	for tmp2_k, tmp2_v in enumerate(tmp1_v['children']):
		print(f"----------{tmp2_k}-{tmp2_v['province']}----------")
		# if tmp2['province'] == "Wales":
		if tmp2_v['province'] == "others":
			status, timezone = crawl_page(tmp2_v['subchildren'][0]['city'])
		else:
			status, timezone = crawl_page(tmp2_v['province'])
		if not status:
			continue
		for tmp3 in tmp2_v['subchildren']:
			tmp3.update({"timezone": f"{timezone}"})
	print(ujson.dumps(tmp1_v['children'], ensure_ascii=False).replace('\/', "/"))
	print(f"----------{tmp1_v['country']}-----------已完成")
	# dic = ujson.dumps(tmp1, ensure_ascii=False).replace('\/', "/")
	with open(f'temp/{tmp1_k}-{tmp1_v["country"]}.json', 'a', encoding='utf-8') as fw:
		json.dump(tmp1_v, fw, ensure_ascii=False)



