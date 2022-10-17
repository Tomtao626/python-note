class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod   #实际上和类没什么关系
    def eat(self):
        # print("%s is eatting %s"% (self.name,food))
        print("%s is eatting %s" % (self.name,"hah"))

    def talk(self):
        print("%s is talking %s" % (self.name,'dfg'))
# d = Dog("陈永华")
# # d.eat("包子")
d = Dog("陈永华")
d.eat(d)
d.talk()