print(10.12,12,112.1)
print(10.12,123,112.12)
print(10.123,1234,112.123)
print(10.1234,12345,112.1234)
print(10.12345,123456,112.12345)

#////////////////////////////
#format是一个字符串格式化对齐函数，f用于float（小数）格式化，d用于整数格式化，e用于指数  format返回值类型为str
#<15.7f 是指 15表示域宽度 .7是精度  f,d就不做介绍   %用于将数字格式化位百分数   s用于字符串的对齐
print(format(10.12,"<15.7f"),format(12,"<10d"),112.1)
print(format(10.123,"<15.7f"),format(123,"<10d"),112.12)
print(format(10.1234,"<15.7f"),format(1234,"<10d"),112.123)
print(format(10.12345,"<15.7f"),format(12345,"<10d"),112.1234)
print(format(10.123456,"<15.7f"),format(123456,"<10d"),112.12345)

