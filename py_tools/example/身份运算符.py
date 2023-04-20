num1 = 3
num2 = 4

# 主要时判断num1,num2是否共用一个地址
print(id(num1),id(num2))
if num1 is num2:
    print("同一个地址")

if num1 is num2:
    print("同一个地址")
else:
    print("不是同一个地址")

if num1 is not num2:
    print("不是同一个和地址")
else:
    print("是同一个地址")