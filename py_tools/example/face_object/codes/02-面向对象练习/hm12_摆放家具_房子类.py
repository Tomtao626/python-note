class HouseItem:

    def __init__(self,name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s,占地面积是%.2f ||" % (self.name,self.area)


class House:

    def __init__(self,area, house_type):
        self.free_area = area
        self.area = area
        self.house_type = house_type
        self.item_list = []

    def __str__(self):
        return ("户型是%s \n面积是:%.2f[剩余面积:%.2f] \n家具列表:%s" %
                (self.house_type,self.area,self.free_area,self.item_list))

    def add_item(self,item):
        print("要添加的家具有%s" % item)


bed = HouseItem("席梦思",4.0)
table = HouseItem("桌子",2.0)
chesk = HouseItem("衣柜",3.0)
print(bed)
print(table)
print(chesk)

my_home = House("两室一厅",150)
# my_home.add_item(bed)
# my_home.add_item(chesk)
# my_home.add_item(table)
print(my_home)


