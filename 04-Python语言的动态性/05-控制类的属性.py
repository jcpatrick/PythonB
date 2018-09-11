class Person(object):
	__slots__ = ("name", "age")
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge

zs = Person("zs", 18)
print(zs)

zs.addr = "aaaa"
print(zs.addr)
