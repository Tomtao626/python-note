# coding :utf-8

import requests

KEY = "883f924f7d1043419b54775229271e26"
UID = "vaster"
msg = "恩施天气"
api_tuling = 'htpp://www.tuling123.com/openapi/api'

data = {
    'key':KEY,
    'info':msg,
    'userid':UID,
}

ret = requests.post(api_tuling,data=data).json()
print(ret.get('text'))
