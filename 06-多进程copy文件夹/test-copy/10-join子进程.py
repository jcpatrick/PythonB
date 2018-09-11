from multiprocessing import Process
import time
import random

def test():
	for i in range(random.randint(1,,5)):
		print("---%d----"%i)
		time.sleep(1)

p = Process(target=test)

p.start()#让这个进程开始执行test函数里面的代码

p.join()#堵塞，

print("---main---")
