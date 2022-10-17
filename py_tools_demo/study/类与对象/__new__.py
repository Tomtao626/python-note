# #普通方式
# class Foo(object):
#     def __init__(self,name):
#         self.name = name
# f = Foo("Alex")
# print(type(f))   #来自于Foo   <class '__main__.Foo'>
# print(type(Foo))  #来自于type   <class 'type'>

def func(self):
    print("hello %s" % self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age
#装逼方式
Foo = type('Foo',(object,),{'talk':func,
                     '__init__':__init__})
f = Foo("haha",20)
f.talk()
print(type(Foo))  #<class 'type'>