# coding:utf-8

import requests
import ujson


class WxUtils(object):
	"""
	wxutils
	"""

	def __init__(self):
		self.appId = "wxb35ea106890f03ddwxb35ea106890f03dd"
		self.Secret = "38994483f30518981afd5a8e18cf1960"
		self.GetAccessUrl = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.appId}&secret={self.Secret}"
		self.CreateCodeUrl = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s"
		self.ResUrl = "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s"

	def __doc__(self):
		self.url = "https://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index"

	def get_access_token(self):
		"""
		get access token
		"""
		return ujson.loads(requests.get(self.Url).content.decode("utf-8"))["access_token"]

	def get_ticket(self):
		"""
		get ticket
		"""
		create_qrcode_url = self.CreateCodeUrl.format(self.get_access_token())
		sence_id = int(time.time() * 100000)
		data = {
			"expire_seconds": 300,
			"action_name": "QR_SCAN",
			"action_info": {
				"sence": {
					"sence_id": sence_id
				}
			}
		}
		resp = requests.post(self.CreateCodeUrl, json=data)
		content = ujson.loads(resp.content.decode("utf-8"))
		ticket = content["ticket"]
		ret_url = self.ResUrl.format(ticket)
		return ret_url

