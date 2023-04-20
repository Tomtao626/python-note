'''
str =13
print(str)
print(type(str))#type（var），求var的类型
print(id(str))#求内存地址
'''
'''
#python变量可以改变数据类型
num1 = 11
print(num1)
print(type(num1))
num1 = 22
print(num1)
print(type(num1))
num = "怒视的那份"#字符串
print(num1)
print(type(num1))
'''
num1 = 3
num2 = 3
print(id(num1),id(num2))#变量名虽然不同，但都指向相同地址
num1 = 20
print(id(num1),id(num2))#num1指向地址改变