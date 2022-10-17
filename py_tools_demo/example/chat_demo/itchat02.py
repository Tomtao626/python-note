# coding:utf-8

import itchat

#注册监听，文本类型  python装饰器封装功能
@itchat.msg_register('Text')
def text_reply(msg):
    if msg['Text'] == "你好！":
        return "你好，很高兴认识你！"
    else:
        return '[自动回复]我现在不在，稍后联系你！'

@itchat.msg_register('File')
def xxxx(msg):
    return 'xxxx'


itchat.auto_login(hotReload=True)
#等待消息动作监听
itchat.run()