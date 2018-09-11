import os
import time

'''全局变量，局部变量等等，都是每个子进程会有自己的一份，互不干扰
'''
g_num = 100

ret = os.fork()
if ret==0:
	print("----proccess--1-----")
	g_num += 1
	print("----proccess--1  g_num=%d----"%g_num)
else:
	time.sleep(3)#保证子进程先执行
	print("----proccess--2-----")
	print("----proccess--2  g_num=%d----"%g_num)
