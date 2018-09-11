def fibo(n):
	a, b = 0, 1
	for i in range(n):
		print(b)
		a, b = b, a + b
fibo(5)
