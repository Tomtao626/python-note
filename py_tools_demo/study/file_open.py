# -*- coding:utf-8 -*-
# Ayuthor:Tom_Tao

#data = open("yesterday",encoding = "utf-8").read()#打开文件并读取
#'w'创建一个新文件
#f = open("yesterday2",'r+',encoding="utf-8")#文件句柄 读写
#f = open("yesterday2",'w+',encoding="utf-8")#文件句柄 写读  先创建一个新文件，再写
#f = open("yesterday2",'a+',encoding="utf-8")#文件句柄a+追加读
f = open("yesterday2",'wb')#文件句柄 二进制文件
f.write("hello world\n".encode())
f.close()

'''
print(f.readline()) #b 字节文件
#rb -- 适用于网络传输
print(f.readline())
print(f.readline())

f.write("------shadiao------\n")
f.write("------shadiao------\n")
f.write("------shadiao------\n")
f.write("------shadiao------\n")
print(f.tell())#打印位置
f.seek(10)#回到第10个位置
print(f.tell())
print(f.readline())#继续打印
f.write("shou be at the beginning of the second line")
f.close()
'''


'''
f.seek(10)
f.truncate(20)#从头截取文件
print(f.tell())#按字符计数
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())#按字符计数
f.seek(10)#查找
print(f.readline())

print(f.encoding)#读编码

print(f.fileno())#返回文件在内存中的编号
print(f.flush())#刷新
#'a'追加到文件最后,不覆盖文件
'''
#high bige
'''
count = 1
for line in f:
    if count == 10:
        print("----hahaha----")
        count +=1
        continue
    print(line)
    count += 1
    '''
#low loop
'''
for index,line in enumerate(f.readlines()):
    if  index == 9:
        print("------------够了-------------")
        continue
    print(line.strip())

#for i in range(10):
    #print(f.readline())

f.close()
'''