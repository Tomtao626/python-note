class Role(object):
    def __init__(self,name,role,weapon,first_life=100,first_money=10000):
        #构造函数
        #在实例化时做一些类的初始化的工作
        self.name = name
        self.role = role
        self.weapon = weapon
        self.first_life = first_life
        self.first_money = first_money
    def shot(self):
        print("shotting...")
    def get_shot(self):
        print("%s:I got shot.." % self.name)
    def buy_gun(self,gun_name):
        print("%s:I just bought a gun %s"% (self.name,gun_name))

r1 = Role('tom_tao','police','AK47')  #把一类变成一个具体对象的过程叫实例化（初始化一个类）
# r2 = Role('张三丰','chief','QBZ95') #生成一个角色
r1.get_shot()
r1.buy_gun("AK47")