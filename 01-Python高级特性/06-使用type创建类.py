class Test:
	pass

def printNum(self):
	print("----num-%d-----"%self.num)

t1 = Test()
print(type(t1))



Test2 = type("Test2",(),{"printNum": printNum})#使用type生成类,字典可以传入属性或者是方法
t2 = Test2()
print(type(t2))

t2.num = 100
t2.printNum()
