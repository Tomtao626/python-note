
# class Person:  经典类
class Person(object): # 新式类
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
    def eat(self):
        print("%s is eatting ...." %self.name)

    def sleep(self):
        print("%s is sleeping...." %self.name)

    def play(self):
        print("%s is playying" %self.name)
class Relation(object):
    # def __init__(self):
    #     print(self)
    def make_friends(self,obj):
        print("%s is makeing friends with %s" %(self.name,obj.name))
        # self.friends.append(obj.name)
        self.friends.append(obj)
class Man(Relation,Person):  #从左到右
    # def __init__(self,name,age,money):
    #     # Person.__init__(self,name,age)
    #     super(Man, self).__init__(name,age)
    #     self.money = money
    #     print("%s 一出生就有 %s money"% (self.name,self.money))
    def piao(self):
        print("%s is piaoing....20s...done" %self.name)
    def sleep(self):
        Person.sleep(self)
        print("man is sleeping....")
class Woman(Person):
    def get_birth(self):
        print("%s is birthing baby....."%self.name)

m1 = Man("tom_tao",20)
# m1.eat()
# m1.piao()
# m1.sleep()

w1 = Woman("niexiaoqian",22)
# w1.sleep()
# w1.get_birth()
m1.make_friends(w1)
w1.name = "比尔盖茨"
# print(m1.friends[0])
print(m1.friends[0].name)  #obj.name为字符串  obj才是真正需要的