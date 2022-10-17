class Cat():

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

tom = Cat()
tom.eat()
tom.drink()
print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)

input_str = input("请输入:")

print(eval(input_str))
print(__import__('os').system('touch aa'))

__import__('os').system('ls')
# 等价于
import os
os.system('ls')