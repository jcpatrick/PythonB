def triangles(m):
	L = [1]
	n = 1
	#行数
	while n <= m:
		yield L
		#这个地方很巧妙，加上一个0之后，在求解每行的第一个和最后一个数值
		#即1时，刚好派上用场
		L.append(0)
		n += 1
		#当i=1时，i - 1对应的便是前面append进来的0
		#当i=n时,i下标对应的值是0
		#这时刚好用来求解每行的第一个数1,和最后一个数1
		#杨辉三角第n行的第i个数，正好等于n-1行的第i-1个数+第i个数
		L = [L[i - 1] + L[i] for i in range(n) ]
for i in triangles(10):
	print(i)
