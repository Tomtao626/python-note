class Cat():

    def __init__(self,new_name):
        print("这是一个初始化方法")
        self.name = new_name

    def eat(self):
        #哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("喝")

tom = Cat("tom")

tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat("John")


lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2= lazy_cat
print(lazy_cat2)