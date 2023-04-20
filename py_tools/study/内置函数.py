
# # all()  如果可迭代对象里的所有元素都为真或为空，返回为真
# print(all([1,3,0,8]))   #存在 0  所以为假 false
# print(all([1,5,67,3]))  # 全为真，所以返回为真
#
# # any() 可迭代数据里任意数据为真，即为真，为空即为假
# print(any([]))  # 为空，即为假
# print(any([1,9,0,-2,3])) # 任意数据为真，即为真
#
# #ascii
# print(ascii([1,2,3,'你好']))
# a = (ascii([1,2,3,'你好']))
# print(type(a),[a])  # 格式变换  从列表转换至字符串 [] --->> "[]"
#
# # bin 十进制数字转换2进制  b 代表2进制
# print(bin(1))
# print(bin(4))
#
# bytes  #bytearray
# a = bytes("abcde",encoding="utf-8")
# b = bytearray("abcde",encoding="utf-8")
# print(b[0])   #bytearray  将制定的字符转换成对应的ASCII
# b[2] = 100  # bytearray(b'abcde') ---->>>   # bytearray(b'abdde')
#
# print(b)
# print(a.capitalize(),a)
# #
# # callable
# print(callable([]))  # 不能返回为callable，为假
#
# chr()  ord()  字符串与acsii互转
# print(chr(97))
# print(ord('a'))
#
# compile()  python底层编译函数
# code = "for i in range(10):print(i)"
# compile(code,'','exec')
#
# divcom 求两个数的商和余数   如 divmod(5,2)  ---->>> (2,1)
# eval  将字符串转换成字典
#
#普通函数
# def sayhai(n):
#      print(n)
#      for i in range(n):
#          print(i)
# sayhai(3)
# #匿名函数 只能用于三元运算及简单运算
# (lambda n:print(n))(5)
# calc = lambda n:print(n)
# calc(5)
#
# filter  一组数据中，过滤出想要的
# res = filter(lambda n :n>5,range(10))
# res = map(lambda n:n*n,range(10))  #相当于列表生成式  [lambda i:i*2 for i in range(10)]
# for i in res:
#     print(i)
# #
# #reduce()  3.0x已内置至函数
# import functools
# res = functools.reduce(lambda x,y:x+y,range(10))  #从0加9
# print(res)
#
#frozenset  冻结 不可变的集合
# a = set([1,2,3,4,54,54,2,87])
# a.add() a.clear() a.pop() 当为set时，集合a存在上述方法
# a = frozenset([1,2,3,4,54,54,2,87])
# a 当为frzenset时，集合a不存在上述方法
#
#globals()  返回当前程序的所有全局变量key和value
# print(globals())
#
# hash()  将数据转换为hash值
#
# locals()
# def test():
#     local_var = 333
#     print(locals())
#     print(globals())
# test()
# print(globals().get(local_var))
#
# oct()  转8进制
# print(oct(1))  #0o1
# print(oct(2))  #0o2
# #
# #  pow() 求一个数的次幂
# print(pow(2,3))  # 8
# print(pow(3,2))  # 9
#
#repe()  字符串转换
#
#round()  小数位数控制
# print(round(1.3543698,2))  #保留两位 1.35
#
#sorted()  对字典数据排序  可按照key 也可按照value排序
# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
# print(sorted(a.items()))  #按照key从小到大排序
# print(sorted(a.items(),key = lambda x:x[1]))  #按照value从小到大排序
# print(a) #原有顺序
#
# zip()  组合两个数据
#

# info = {
#     'name':'tom_tao',
#     'age':20,
#     'sex':'boy'
# }
# f = open('test.text','w')
# f.write(str(info))
# f.close()