class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我叫 %s ,体重是%s KG" % (self.name,self.weight)

    def run(self):
        # print("%s 爱跑步，跑步减肥快,体重是%s " % (self.name,self.weight))
        self.weight -= 0.5

    def eat(self):
        # print("%s 是个吃货，吃完这顿的体重是%s" % (self.name,self.weight))
        self.weight += 1

xiaoming = Person("小明",75.0)
xiaoming.run()
xiaoming.eat()

print(xiaoming)

xiaomei = Person("小美",45.0)
xiaoming.eat()
xiaomei.run()

print(xiaomei)