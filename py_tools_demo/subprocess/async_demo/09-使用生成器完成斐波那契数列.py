def create_num(all_num):
	print("---1---")
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		# print(a)
		# 如果一个函数中由yield语句，那么这个就不再是函数，而是一个生成器的模板
		print("---2---")
		yield a
		print("---3---")
		a, b = b, a+b
		current_num += 1
		print("---4---")

# 如果在调用create_num的时候，发现这函数中有yield，那么此时，不是调用函数，而是创建一个生成器对象
obj = create_num(10)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

'''
打印结果如下:
	---1---
	---2---
	0
	---3---
	---4---
	---2---
	1
'''

# for num in obj:
# 	print(num)