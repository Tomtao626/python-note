class Dog(object):
    name = "sakas"
    def __init__(self,name):
        self.name = name

    # @staticmethod
    @classmethod
    def eat(self):
        # print("%s is eatting %s"% (self.name,food))
        print("%s is eatting %s" % (self.name,"hah"))

    def talk(self):
        print("%s is talking %s" % (self.name,'dfg'))
# d = Dog("陈永华")
# # d.eat("包子")
d = Dog("陈永华")
d.eat()
