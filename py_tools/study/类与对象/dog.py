#
# class Dog:
#     def __init__(self,name):
#         self.name = name
#
#     def sound(self):
#         print("%s:hahah hjahah  uajajaj" %self.name)
#
# d1 = Dog("陶朋")
# d2 = Dog("张三丰")
# d3 = Dog("李天一")
#
# d1.sound()
# d2.sound()
# d3.sound()
a = {1:1,2:2,3:3}
print(','.join([str(i) for i in sorted(list(a.keys()))]))