class Cat:

    def __init__(self,new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        #会在对象调用完毕后，销毁对象
        print("%s was died" % self.name)

'''
    __init__改造初始化方法，可以让创建对象更加灵活
    __del__如果希望在对象被销毁前，在做一些事情，可以考虑使用__del__方法
    
    生命周期
        一个对象从调用类名()创建，生命周期开始
        一个对象的__del__()方法一旦调用，生命周期结束
        在对象的生命周期内，可以访问对象属性，或者让对象调用方法
'''



#tom 是一个全局变量
tom = Cat("xxxxx")
print(tom.name)

print(type(tom))
print(tom)
# del 关键字可以删除一个对象
del tom
print("---"*30)

