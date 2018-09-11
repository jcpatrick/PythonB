import os
import time

#父进程
ret = os.fork()
if ret == 0:
	#子进程
	print("------1-------")
else:
	#父进程
	print("------2-------")

'''相当于上面创建的分支，在这后面又在创建的分支，所有下面的内容会被调用2次'''

#父子进程
ret = os.fork()
if ret == 0:
	#孙子
	#2儿子
	print("------11-------")
else:
	#儿子
	#父进程
	print("------22-------")
