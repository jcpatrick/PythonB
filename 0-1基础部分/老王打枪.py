class Person(object):
    def __init__(self, name):
        self.name = name
        self.gun = None
    def setup_zidan(self, danjia, zidan):
        """将子弹安装到枪中"""
        danjia.add_zidan(zidan)
    def setup_danjia(self, gun, danjia):
        """将弹夹安装到枪中"""
        gun.setup_danjia(danjia)
    def set_gun(self, gun):
        """老王拿枪"""
        self.gun = gun
    def shoot(self, enemy):
        if self.gun and enemy:
            self.gun.shoot(enemy)
        else:
            print("%s没有枪"%(self.name))
    def __str__(self):
        return self.name + ":\n枪：\n" + str(self.gun)
class Gun(object):
    def __init__(self, name):
        self.name = name
        self.danjia = None
    def setup_danjia(self, danjia):
        self.danjia = danjia
    def shoot(self, enemy):
        if self.danjia:
            self.danjia.fire(enemy)
        else:
            print("没有弹夹")
    def __str__(self):
        return "枪名:" + self.name + "\n弹夹：" + str(self.danjia)
class DanJia(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.zidan_list = []
    def add_zidan(self, zidan):
        """将子弹安装到弹夹中"""
        self.zidan_list.append(zidan)
    def fire(self, enemy):
        if self.zidan_list:
            zidan = self.zidan_list.pop()
            zidan.demage_enemy(enemy)
        else:
            print("弹夹没有子弹")
    def __str__(self):
        return str([zd.demage for zd in self.zidan_list])
class ZiDan(object):
    def __init__(self, demage):
        self.demage = demage
    def demage_enemy(self, enemy):
        enemy.hurted(self.demage)

class Enemy(object):
    def __init__(self, name, health):
        self.name = name
        self.total_hp = health
        self.hp = health
    def hurted(self, demage):
        if self.hp - demage <= 0:
            print("敌人" + self.name + "已经死亡")
            self.hp = 0
        else:
            self.hp -= demage
            print("敌人总血量为%d，还剩%d血"%(self.total_hp, self.hp))

def main():
    #1、创建一个人对象
    laowang = Person("老王")
    #2、创建抢
    ak47 = Gun("ak47")
    #3、创建弹夹
    danjia = DanJia(20)
    #4、创建子弹
    zidan1 = ZiDan(10)
    zidan2 = ZiDan(5)
    #5、将子弹安装到弹夹中
    laowang.setup_zidan(danjia, zidan1)
    laowang.setup_zidan(danjia, zidan2)
    #6、件弹夹安装到枪中
    laowang.setup_danjia(ak47, danjia)
    #7、老王拿枪
    laowang.set_gun(ak47)
    print(laowang)
    #8、创建一个敌人
    lisi = Enemy("list", 100)
    #9、老王开枪
    laowang.shoot(lisi)


if __name__ == '__main__':
    main()