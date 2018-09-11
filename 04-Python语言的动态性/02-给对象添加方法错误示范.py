class Person(object):
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge
	
	def eat(self):
		print("%s eatting"%( self.name))

def run(self):
	print("%s running"%( self.name))

zs = Person("zs", 18)
zs.eat()

zs.run = run
zs.run() #这里调用会报错，因为没有给zs.run中传入当前对象的引用
