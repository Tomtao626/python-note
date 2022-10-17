a = 0
b = 1
nums = list()
while i<10:
	nums.append(a)
	a,b = b,a+b
	i+=1
for num in nums:
	print(num)