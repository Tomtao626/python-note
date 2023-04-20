def bulk(self):
    print("%s is yelling..."%self.name)
class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating.."% self.name,food)

d = Dog("tuyao")
choice = input(">>>:").strip()

if hasattr(d,choice):
    # delattr(d,choice)
    # attr = getattr(d,choice)
    # setattr(d,choice,"hahah")
    # print(attr)
    # func("chenronghua")  #字符串不能call
    getattr(d,choice)
else:
    # setattr(d, choice, bulk)
    # d.talk(d)
#     setattr(d,choice,22)
#     print(getattr(d,choice))
# print(d.name)
    setattr(d,choice,bulk)
    func = getattr(d,choice)
    func(d)