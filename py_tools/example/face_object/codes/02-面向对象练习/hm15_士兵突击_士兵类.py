class Gun:
    def __init__(self,model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):

        self.bullet_count += count

    def shoot(self):
        print("[%s] 的子弹数量是%s " %(self.model,self.bullet_count))

        if self.bullet_count <= 0:
            print("%s ，没有子弹了。。。" % self.model)
            return
        self.bullet_count -= 1
        print("突突突，[%s] 的子弹还有%s " % (self.model,self.bullet_count))

class Solider:

    def __init__(self,name):

        self.name = name

        self.gun = None

AK47 = Gun("AK47")
AK47.add_bullet(45)
AK47.shoot()

solider = Solider("许三多")
# solider.gun = AK47
print("%s 的枪的型号是%s" % (solider.name,solider.gun))