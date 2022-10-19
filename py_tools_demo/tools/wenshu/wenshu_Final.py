import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
import requests
import base64
import math
import json
import time
import random
from urllib import parse
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad


##中国文书网http请求模式
def des3encrypt(plain_text: str, key: str, iv: str) -> str:
	des3 = DES3.new(key=key.encode(), mode=DES3.MODE_CBC, iv=iv.encode())
	encrypted_data = des3.encrypt(pad(plain_text.encode(), DES3.block_size))
	cipher_text = base64.b64encode(encrypted_data).decode()
	return cipher_text


def des3decrypt(cipher_text: str, key: str, iv: str) -> str:
	des3 = DES3.new(key=key.encode(), mode=DES3.MODE_CBC, iv=iv.encode())
	decrypted_data = des3.decrypt(base64.b64decode(cipher_text))
	plain_text = unpad(decrypted_data, DES3.block_size).decode()
	return plain_text


def get_pageid():
	guid = ""
	for i in range(1, 33):
		n = hex(math.floor(random.random() * 16))[-1]
		guid += n
	return guid


def encrpt(password, public_key):
	rsakey = RSA.importKey(public_key)
	cipher = Cipher_pksc1_v1_5.new(rsakey)
	cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
	return cipher_text.decode()


def get_token(size=24):
	arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
	       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
	       'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	token_str = ""
	for i in range(size):
		token_str += arr[round(random.random() * (len(arr) - 1))]
	return token_str


def get_cipher():
	timestamp = str(int(time.time() * 1000))
	salt = get_token()
	year = time.strftime('%Y')
	month = time.strftime('%m') if int(time.strftime('%m')) < 10 else str(int(time.strftime('%m')) - 1)
	day = time.strftime('%d')
	iv = year + month + day
	text_1 = des3encrypt(timestamp, salt, iv)
	text_2 = salt + iv + text_1
	result = []
	l = list(text_2)
	for i in range(len(l)):
		if i != 0:
			result.append(' ')
		item = l[i]
		result.append(bin(ord(item))[2:])
	return ''.join(result)


# 解密访问网页获取的result
def decrypt(text: str) -> json:
	try:
		# print(text)
		data = json.loads(text)
		_key = data['secretKey']
		result = data['result']
		_iv = time.strftime('%Y%m%d')
		dtext = des3decrypt(result, _key, _iv)
		return json.loads(dtext)
	except Exception as e:
		print("结果解密错误: " + str(e))
		return None


session = requests.session()
headers = {
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
	'Origin': 'https://wenshu.court.gov.cn',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'no-cors',
	'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=' + get_pageid() + '&s8=02',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 密码加密模块
key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5GVku07yXCndaMS1evPIPyWwhbdWMVRqL4qg4OsKbzyTGmV4YkG8H0hwwrFLuPhqC5tL136aaizuL/lN5DRRbePct6syILOLLCBJ5J5rQyGr00l1zQvdNKYp4tT5EFlqw8tlPkibcsd5Ecc8sTYa77HxNeIa6DRuObC5H9t85ALJyDVZC3Y4ES/u61Q7LDnB3kG9MnXJsJiQxm1pLkE7Zfxy29d5JaXbbfwhCDSjE4+dUQoq2MVIt2qVjZSo5Hd/bAFGU1Lmc7GkFeLiLjNTOfECF52ms/dks92Wx/glfRuK4h/fcxtGB4Q2VXu5k68e/2uojs6jnFsMKVe+FVUDkQIDAQAB"
public_key = '-----BEGIN PUBLIC KEY-----\n' + key + '\n-----END PUBLIC KEY-----'
password = encrpt('', public_key)
password = parse.quote(password)

username = ''
params = {
	"username": "17712635980",
	"password": password,
	"appDomain": "wenshu.court.gov.cn"
}
##通过请求获取登陆状态
response = session.post("https://account.court.gov.cn/api/login", data=params, headers=headers, verify=False)
print(response.text)
# 通过请求获取登陆凭证
headers = {
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
	'Origin': 'https://wenshu.court.gov.cn',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
	'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?open=login',

}
response1 = session.post("https://wenshu.court.gov.cn/tongyiLogin/authorize", headers=headers, verify=False)
session.get(response1.text, headers=headers)
print(response1.text)

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}

data = {
	'pageId': get_pageid(),
	's8': '04',
	'sortFields': 's50:desc',
	'ciphertext': get_cipher(),
	'pageNum': '1',
	'pageSize': '5',
	'queryCondition': '[{"key":"s8","value":"01"}]',
	'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
	'__RequestVerificationToken': get_token(24)
}

r = session.post('https://wenshu.court.gov.cn/website/parse/rest.q4w', headers=headers, data=data, verify=False)
print(r.text)
print(decrypt(r.text))
