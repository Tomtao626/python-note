class Cat():

    def eat(self):
        #哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("喝")

tom = Cat()

tom.name = 'tom'

tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()

lazy_cat.name = 'lazy'

lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2= lazy_cat
print(lazy_cat2)