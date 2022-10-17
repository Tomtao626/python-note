import time#1970年1月1日00:00
timedata = time.time()
timedata = int(timedata)
print(timedata/3600)#多少小时
print(timedata/3600/24)#多少天
print(timedata/3600/24/365)#多少年
print(timedata&60)