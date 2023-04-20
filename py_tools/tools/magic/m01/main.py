#  冷知识

# 1 ...语法糖
print(...)  # Ellipsis
print(id(...))  # 4551344512
print(id(Ellipsis))  # 4551344512
print(bool(Ellipsis))  # True
"""
	你会发现这是个单例，作用类似于pass bool转换是真 而且是Numpy的一个语法糖🍬
"""

# 2 end结束代码块
__builtins__.end = None


def my_abs(x):
	if x > 0:
		return x
	return -x
	end


end

print(my_abs(10))  # 10
print(my_abs(-30))  # 30
"""
	有不少编程语言，循环、判断代码块需要用 end 标明结束，这样一定程度上会使代码逻辑更加清晰一点。
	但是其实在 Python 这种严格缩进的语言里并没有必要这样做。
	如果你真的想用，也不是没有办法，具体你看下面这个例子。
"""

# 3 可直接运行的zip包
# 新建一个名为demo的文件夹，有__main__.py和calc.py两个代码文件，内容如下
"""
calc.py
def add(x, y : int) -> int:
	return x + y

__main__.py
import calc
print(calc.add(99, 88)
"""
# 在demo的上一级目录下执行 python3 -m zipfile -c demo.zip demo/* 进行打包📦
# 然后会生成一个demo.zip的文件 执行python3 demo.zip 会直接返回结果
"""
	python可直接运行的一般是.egg 或 .whl包等 其实zip包也可以
"""

# 4 反斜杠 \
print("hello\
 world")

print("\ntext\t")
"""
	反斜杠有两个作用
		在字符串中做转义
		在行尾 做续行符
"""

# 5 修改解释器指示符 主要适用于py命令行终端下
import sys

# sys.ps1  # >>>
# sys.ps2  # ...
"""
	如果要替换其标示符 直接对ps1/ps2重新赋值就可以了
"""

# 6 链式比较
print(True == False == True)  # False

# 7 and/or的短路效应
print(2 and 3 and 4)  # 4
print(2 or 7)  # 2
print((2 and 6 and 8 and 9) * (7 or 6 or 10))  # 9 * 7 = 63
"""
	当一个or表达式中所有值都为真时，py会选择第一个值
	当一个and表达式所有值都为真时，py会选择最后一个值
"""

# 7 连接多个列表
x = [1, 2, 3]
y = ['a', 'b', 'c']
z = [1.1, 2.2, 3.3]
s = sum((x, y, z), [])
print(s)  # [1, 2, 3, 'a', 'b', 'c', 1.1, 2.2, 3.3]
print(x+y+z)  # [1, 2, 3, 'a', 'b', 'c', 1.1, 2.2, 3.3]
print([i for i in zip(x, y, z)])

# 8 字典排序

dict_one = {str(i): 1 for i in range(10)}
print(dict_one)  # {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1} 已自动排序

# 9 用户无感知的小整数池
