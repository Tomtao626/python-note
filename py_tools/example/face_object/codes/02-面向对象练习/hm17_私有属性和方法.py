class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18
    # 在对象的方法内部，是可以直接访问对象的私有属性的
    def __secret(self):
        print("%s's age is %s" % (self.name,self.__age))

xiaomei = Women("小美")
#私有属性不能在外界直接被访问
#私有方法不能再外界直接被调用
# xiaomei.__secret()
# print(xiaomei.__age)