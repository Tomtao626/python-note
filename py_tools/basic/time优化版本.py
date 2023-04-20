import time
mytimes = time.time()
print(mytimes)
#mytimes = 86400
print("自从1970年，现在过去了",int(mytimes),"秒")
seconds = int(mytimes)%60
hours = int(mytimes)//3600
mins =  int(mytimes)%3600 #(int(mytimes)-int(mytimes)//3600*3600)
mins = (mins - seconds)//60
days = hours//24
hours = hours%24#用作一天24小时划分
month = days // 30
days = days%30#用作一月30天划分
years = month//12
month = month%12#用作12月一次划分
print("自从1970年，现在过去了",
      years,"年",
      month,"月",
      days,"天",
      hours,"小时",
      mins,"分钟",
      seconds,"秒")

#100%9=100//9*9=1
#3600+1550秒=5150秒
#1小时 50秒
#5150-50-3600/60=25

