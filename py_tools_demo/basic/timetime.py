import time
mytimes = time.time()
mytimes = int(mytimes)
haha = int(mytimes)//60
haha1 = int(mytimes)//3600
haha2 = int(haha1)//24
haha3 = int(haha2)//365
print("自从1970年，现在过去了",mytimes,"秒",haha,"分钟",haha1,"小时",haha2,"天",haha3,"年")
