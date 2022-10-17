class HouseItem:

    def __init__(self,name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s,占地面积是%.2f ||" % (self.name,self.area)

bed = HouseItem("席梦思",4.0)
table = HouseItem("桌子",2.0)
chesk = HouseItem("衣柜",3.0)

print(bed,table,chesk)