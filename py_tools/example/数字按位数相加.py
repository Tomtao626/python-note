num = eval(input("请输入一个0~1000之间的数字："))
t = num//100
g = num%10
s = num//10%10
w = t+g+s
print("所有数之和为：",w)
