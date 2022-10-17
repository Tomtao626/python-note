class Gun:
    def __init__(self,model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s] no bullet" % self.model)
            return
        self.bullet_count -= 1
        print("[%s]'s bullet_count have %s"% (self.model,self.bullet_count))


class Solider:

    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        # if self.gun == None:
        if self.gun is None:
            print("[%s] no gun" % self.name)
            return
        print("go go go! [%s]" % self.name)
        self.gun.add_bullet(45)
        self.gun.shoot()

AK47 = Gun("AK47")

# AK47.add_bullet(30)
# AK47.shoot()

solider = Solider("许三多")
solider.gun = AK47
print(solider.gun)