def fibo():
	a, b = 0, 1
	for i in range(10):
		c = yield i
		print(c)
		a, b = b, a+b

t = fibo()

print("---next方法---")
ret = next(t)
print(ret)

print("\n--------------")
print("---send方法----")
ret = t.send("hello")
print(ret)
