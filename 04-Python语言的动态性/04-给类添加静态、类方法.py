import types
class Person(object):
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge
	
	def eat(self):
		print("%s eatting"%( self.name))

#静态方法
@staticmethod
def run():
	print(" running")

@classmethod
def laugh(cls):
	print("laughing")

zs = Person("zs", 18)
zs.eat()

#给Person类添加静态方法
Person.run = run
Person.run()

#给Persion类添加类方法
Person.laugh = laugh
Person.laugh()
