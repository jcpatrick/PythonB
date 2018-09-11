import os

ret = os.fork()
#print(ret)
if ret > 0:
	print("这是父进程：%d"%os.getpid())
else:
	print("这是子进程：%d，父进程id：%d"%(os.getpid(),os.getppid()))
