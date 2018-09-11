class House:
    def __init__(self, new_area, new_intro,new_addr):
        self.area = new_area
        self.intro = new_intro
        self.addr = new_addr
        self.left_area = new_area
        self.contentItems = []

    def __str__(self):
        msg = "房子总面积为：%d,剩余空间：%d,户型：%s,位置:%s \n 房子中添加的内容%s"%(self.area, self.left_area, self.intro, self.addr, str(self.contentItems))
        return msg
    def addItem(self, item):
        self.left_area -= item.area
        self.contentItems.append(item.name)

class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "床的类型：%s,床的大小：%d"%(self.name, self.area)

house = House(128, "商住两用", "深圳市 罗湖区 东门 翠湖小区5栋104")
print(house)

bed1 = Bed("席梦思", 4)
print(bed1)

house.addItem(bed1)

bed2 = Bed("三人床", 6)
print(bed2)

house.addItem(bed2)

print(house)