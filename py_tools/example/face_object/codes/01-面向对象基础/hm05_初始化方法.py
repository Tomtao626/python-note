class Cat:
    def __init__(self):
        print("这是一个初始化方法")

        self.name = 'tom'

    def eat(self):
        print("%s 爱吃鱼" % self.name)

#使用类名()创建对象，__init__方法会自动初始化对象，也是对象的内置方法
tom = Cat()
tom.eat()