def upperAttr(future_class_name, future_class_parents,future_class_attr):
	"""
		future_class_name:类的名称
		future_class_parents:类的父类
		future_class_attr:类的属性
	"""
	newAttr = {}
	for name,value in future_class_attr.items():
		if not name.startswith("__"):
			newAttr[name.upper()] = value
	#创建一个新类
	return type(future_class_name, future_class_parents, newAttr)

class Foo(object):
	__metaclass__ = upperAttr#通过__metaclass__控制类的创建
	bar = "bip"

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

t = Foo()
print(t.BAR)
print(t.bar)
