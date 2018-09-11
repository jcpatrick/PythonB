class Test(object):
	def __init__(self, func):
		"""在初始化Test类的时候，会将该函数的引用传入进来
		"""
		print("---初始化---")
		print("函数名是%s"%(func.__name__))
		self.__func = func
	def __call__(self):
		print("----装饰器中的功能----")
		self.__func()

#在Python解释器加载python文件的时候，就会创建Test类，同时传入fff方法的引用
#每次都会创建调用__init__方法，也就是会创建一次Test类
@Test#这句相当于test = Test(test)
def fff():
	print("---ffff----")
@Test
def bbb():
	print('-----bbb------')
fff()#调用这个变量相当于调用test()也就是Test类的__call__方法
bbb()
