num = 100
def func1():
	#num = 200
	def func2():
		#num = 300
		print(num)
	return func2
#num的查找顺序是func2——》func1——》全局变量——》内件
ret = func1()
ret()
