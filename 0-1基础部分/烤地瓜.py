class SweetPotato:
    def __init__(self):
        self.currentState = "生的"
        self.level = 0
        self.seasoning = []
    def __str__(self):
        return "地瓜烤了%d,已经%s,添加了作料:%s"%(self.level, self.currentState, str(self.seasoning))

    def cook(self, cooktime):
        self.level += cooktime
        if self.level <= 3:
            self.currentState = "生的"
        elif self.level <= 5:
            self.currentState = "半生不熟"
        elif self.level <= 7:
            self.currentState = "熟了"
        elif self.level > 7:
            self.currentState = "糊了"

    def addSeasoning(self, seasoning):
        self.seasoning.append(seasoning)

sp = SweetPotato()
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)
sp.addSeasoning("胡椒粉")
print(sp)
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)
sp.addSeasoning("盐")
print(sp)
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)
sp.addSeasoning("孜然粉")
print(sp)
sp.cook(1)
print(sp)
sp.cook(1)
print(sp)