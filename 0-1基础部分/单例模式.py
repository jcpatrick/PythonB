class DanLi(object):
    __instance = None
    __init__flag = False #初始化标记
    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            print("111")
        return cls.__instance
    def __init__(self, name):
        if DanLi.__init__flag == False:
            self.name = name
            DanLi.__init__flag = True

aaa = DanLi("aaa")
print(id(aaa))
print(aaa.name)
bbb = DanLi("bbb")
print(id(bbb))
print(bbb.name)