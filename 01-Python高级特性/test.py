def fibo():
	print("---start---")
	a, b = 0, 1
	for i in range(10):
		print("-----1-----")
		yield b
		print("-----2-----")
		a, b = b, a + b
		print("-----3-----")

