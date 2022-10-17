import random

# num1 = random.randint(0,100)
# num2 = random.randint(0,100)   #生成0-100之间的随机数 包含0，包含100
num1 =random.randrange(0,10)
num2 = random.randrange(0,100)
print("傻逼 %d + %d" %(num1,num2))
num = input("baby input:")
num = eval(num)
if num == num1+num2:
    print("你是傻逼")
else:
    print("你不傻")
