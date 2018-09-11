class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __getattribute__(self, obj):
		"""不允许在这个方法里面调用self的属性，不然调用的那个属性又会回到这里
		会造成死循环，程序就出错了
		"""
		if obj == "name":#判断调用的是什么属性或者方法名
			return "hello" +  object.__getattribute__(self, obj)
		else:
			temp =  object.__getattribute__(self, obj)
			print("====2>%s"%str(temp))
			return temp#不return的话，函数就无法被调用了，函数相当于是None

	def show(self):
		print("this is in show method")

zs = Person("zs", 18)
print(zs.name)
print(zs.age)
ls = Person("ls", 22)
print(ls.name)
print(ls.age)

zs.show()
#1. 先获取show属性对应的结果，，是一个方法
#2. 调用返回
