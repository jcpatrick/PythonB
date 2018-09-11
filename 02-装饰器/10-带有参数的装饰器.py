def func_arg(arg):
	print('arg------' + arg)
	def func(functionName):
		def func_in():#通过arg参数，可以做到装饰器区分的功能
			if arg == "heihei":
				functionName()
				functionName()
			else:
				functionName()
		return func_in
	return func

#1. 线执行func_arg("heihei")这个函数，return的结果是func函数的引用
#2. 相当于再使用一次@func
#3. 使用@func对test进行装饰
@func_arg("heihei")
def test():
    print("----test----")

#带有参数的装饰器，能够起到运行，有不同的功能
@func_arg("hehe")
def test2():
    print("----test----")

test()
print("------------------")
test2()
