import gevent
import time
from gevent import monkey

# 有耗时操作时需要
monkey.patch_all() # 将程序中用到的耗时操作的代码，换成gevent中自己实现的模块

def test1(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

def test2(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

def test3(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

# print("---1---")
# g1 = gevent.spawn(test1, 5)
# print("---2---")
# g2 = gevent.spawn(test2, 5)
# print("---3---")
# g3 = gevent.spawn(test3, 5)
# print("---4---")
# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
		gevent.spawn(test1, "---1---"),
		gevent.spawn(test2, "---2---"),
		gevent.spawn(tets3, "---3---")
	])

'''
执行结果如下:

---1---
---2---
---3---
---4---
<Greenlet at 0x28081468048: test1(5)> 0
<Greenlet at 0x280fff9bbf8: test2(5)> 0
<Greenlet at 0x28081468268: test3(5)> 0
<Greenlet at 0x28081468048: test1(5)> 1
<Greenlet at 0x280fff9bbf8: test2(5)> 1
<Greenlet at 0x28081468268: test3(5)> 1
<Greenlet at 0x28081468048: test1(5)> 2
<Greenlet at 0x280fff9bbf8: test2(5)> 2
<Greenlet at 0x28081468268: test3(5)> 2
<Greenlet at 0x28081468048: test1(5)> 3
<Greenlet at 0x280fff9bbf8: test2(5)> 3
<Greenlet at 0x28081468268: test3(5)> 3
<Greenlet at 0x28081468048: test1(5)> 4
<Greenlet at 0x280fff9bbf8: test2(5)> 4
<Greenlet at 0x28081468268: test3(5)> 4

'''