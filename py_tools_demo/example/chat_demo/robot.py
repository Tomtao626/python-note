# coding:utf-8

import itchat
import requests
from itchat.content import *

KEY = "883f924f7d1043419b54775229271e26"
UID = "vaster"


def get_reply(msg):
	api_tuling = 'htpp://www.tuling123.com/openapi/api'

	data = {
		'key': KEY,
		'info': msg,
		'userid': UID,
	}
	ret = requests.post(api_tuling, data=data).json()
	print(ret.get('text'))


# 注册监听，文本类型  python装饰器封装功能
@itchat.msg_register('Text')
def text_reply(msg):
	defaultmsg = msg['Text']
	reply = get_reply(defaultmsg)
	return reply
	# if msg['Text'] == "你好！":
	#     return "你好，很高兴认识你！"
	# else:
	#     return '[自动回复]我现在不在，稍后联系你！'


# @itchat.msg_register('File')
# def xxxx(msg):
#     return 'xxxx'

@itchat.msg_register([TEXT, MAP, CARD, NOTE], isGroupChat=True)
def group_reply(msg):
	if msg['isAt']:
		defaultmsg = msg['Text']
		return get_reply(defaultmsg)
	return


itchat.auto_login(hotReload=True)
# 等待消息动作监听
itchat.run()
