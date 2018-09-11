from multiprocessing import Pool
import os
import random
import time

def worker(num):
	for i in range(5):
		print("======pid = %d=====num=%d"%(os.getpid(), num))
		time.sleep(1)

pool = Pool(3)

for i in range(10):
	print("-----%d----"%i)
	pool.apply_async(worker, (i,))#创建子进程来执行任务,第一个参数是任务函数，
									#第二个是任务函数的参数，需要用元组来保存

print("-----start-----")
pool.close()#关闭进程池，关闭后不再接受任何请求
pool.join()#主进程 创建/添加 任务后，默认不会等待进程池中的任务执行完成后才结束
			#而是 当主进程的任务完成后 立马结束,如果没有join会导致进程池中的任务不会执行
print("----close----")
