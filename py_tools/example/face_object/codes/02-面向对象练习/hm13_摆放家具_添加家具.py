class HouseItem:

    def __init__(self,name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s],占地面积是%.2f" % (self.name, self.area)


class House:

    def __init__(self, area, house_type):
        self.area = area
        self.house_type = house_type
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


#创建家具
bed = HouseItem("席梦思", 4)
table = HouseItem("桌子", 2)
chesk = HouseItem("衣柜", 3)
print(bed)
print(table)
print(chesk)

#创建房子
# 切记传值的顺序要和定义的类中的属性位置一一对应
my_home = House(150, "两室一厅")
my_home.add_item(bed)
my_home.add_item(chesk)
my_home.add_item(table)
print(my_home)


