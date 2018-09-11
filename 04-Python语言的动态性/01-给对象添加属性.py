class Person(object):
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge

laowan = Person("laowang", 18)
print(laowan.name)
print(laowan.age)
laowan.addr = "shenzhen...."
print(laowan.addr)

laozhao = Person("laozhao", 30)
#print(laozhao.addr)

Person.num = 100
print(laowan.num)
print(laozhao.num)
