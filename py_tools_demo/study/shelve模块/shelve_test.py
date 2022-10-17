import shelve
import datetime
d = shelve.open('shelve_test')  # 打开一个文件
print(d.get('test'))
print(d.get('info'))
print(d.get('date'))

# class Test(object):
#     def __init__(self, n):
#         self.n = n


# t = Test(123)
# t2 = Test(123334)
#
info = {'age':22,'job':'it'}

name = ["alex", "rain", "test"]
d["test"] = name  # 持久化列表
# # # # d["t1"] = t  # 持久化类
# # # # d["t2"] = t2
d['info'] = info
d['date'] = datetime.datetime.now()
d.close()