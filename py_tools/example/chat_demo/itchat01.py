# coding:utf-8
"""
Function:itchat的使用
Author: tom_tao
"""

import itchat

# 登录
itchat.auto_login(hotReload=True)
# 给文件助手发消息
itchat.send("hello world", toUserName='filehelper')
# 给好友发消息
print(itchat.get_friends()[1])
# 获取昵称信息
nickname = itchat.get_friends()[1]["Nickname"]
# 获取用户名
username = itchat.get_friends()[1]["Username"]
print(nickname)
print(username)

# 给最近的好友发消息
# 注意username是微信消息的一个字符串（动态字符串）
itchat.send("hello world", toUserName=username)
print(itchat.search_friends(name="username"))
