def fibo():
	print("---start---")
	a, b = 0, 1
	for i in range(10):
		print("-----1-----")
		yield b
		print("-----2-----")
		a, b = b, a + b
		print("-----3-----")

a = fibo()

#方法一
#使用next的方式可能会出现越跌，超出迭代器范围的情况
#ret = next(a)
#print(ret)
#ret = next(a)
#print(ret)
#ret = next(a)
#print(ret)
#ret = next(a)
#print(ret)

#方法一.1
#a.__next__()

#方法二
#可以使用for循环遍历的方式，这样就可以避免超出了
for ret in a:
	print(ret)
