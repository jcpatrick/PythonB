import os
import time
ret = os.fork()
#从fork开始，后面的内容都会被调用两次
if ret==0:
	print("---子进程----")
	time.sleep(5)
	print("----子进程结束----", end="")
else:
	print("---父进程---")
	time.sleep(3)


print("---over---")
