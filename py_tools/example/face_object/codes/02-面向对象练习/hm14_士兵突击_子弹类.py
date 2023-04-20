class Gun:

    def __init__(self, model):

        self.model = model
        self.buffer_count = 0

    def add_buffer(self,count):

        self.buffer_count += count

    def shoot(self):

        if self.buffer_count <= 0:
            print("[%s]没有子弹了.." % self.models)
            return
        self.buffer_count -= 1

        print("突突突， [%s] 还有%s 颗子弹" % (self.model,self.buffer_count))

ak47 = Gun("ak47")

ak47.add_buffer(10)
ak47.shoot()