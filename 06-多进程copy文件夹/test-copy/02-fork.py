import os
import time
'''os.fork()创建一个子进程，相当于将当前代码复制一份
	os.fork()会有两个返回值，在父进程中返回的是1，子进程返回的是0
	这就是为什么下面程序的代码会交替打印------1----------和-------2----------的原因
'''
ret = os.fork()

if ret == 0:
	while True:
		print("------1-------")
		time.sleep(1)
else:
	while True:
		print("------2-------")
		time.sleep(1)
