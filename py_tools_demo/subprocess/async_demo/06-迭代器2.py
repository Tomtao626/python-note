import time
from collections import Iterable
from collections import Iterator

class Classmate(object):
	def __init__(self):
		self.names = list()  # 等于 self.names = []
		self.current_num = 0

	def add(self,name):
		self.names.append(name)

	def __iter__(self):
		'''如果想要一个对象成为一个可以迭代的对象，即可以使用for,那么必须使用__iter__方法'''
		return ClassIterator(self) # 返回对象的引用

	def __next__(self):
		if self.current_num < len(self.names):
			ret = self.names[elf.current_num]
			self.current_num += 1
			return ret
		else:
			raise StopIteration


classmate = classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断clasmate是否可以迭代的对象:",isinstance(classmate,Iterable))
# classmate_iterator = iter(clasmate)
# print("判断classmate_iterator是否是迭代器:",isinstance(classmate_iterator,Iterator))
# print(next(classmate_iterator))

for name in classmate:
	print(name)
	time.sleep(1)















