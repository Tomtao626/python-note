class Cat:

    def __init__(self,new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        #会在对象调用完毕后，销毁对象
        print("%s was died" % self.name)

    def __str__(self):
        # __str__()方法必须返回一个字符串
        return ("我是小猫[%s]" % self.name)



#tom 是一个全局变量
tom = Cat("xxxxx")

print(type(tom))
print(tom)

