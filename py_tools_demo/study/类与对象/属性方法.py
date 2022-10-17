class Dog(object):
    '''这个类用于描述Dog这个对象'''
    def __init__(self,name):
        self.name = name
        self.__food = None
    # @staticmethod
    @property
    def eat(self):
        # print("%s is eatting %s"% (self.name,food))
        print("%s is eatting %s" % (self.name,self.__food))

    @eat.setter  #修改
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.deleter  #删除
    def eat(self):
        del self.__food
        print("删完了")
    def talk(self):
        print("%s is talking %s" % (self.name,'dfg'))
# d = Dog("陈永华")
# # d.eat("包子")
# d = Dog("陈永华")
# d.eat
# d.eat = ("baozi")
# d.eat
# del d.eat
# d.eat
print(Dog.__doc__)
# del d.name  删除普通属性
# print(d.name)