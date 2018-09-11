from multiprocessing import Manager, Pool
import os, time, random

def reader(q):
	print("reader启动(%s),父进程为(%s)"%(os.getpid(), os.getppid()))
	for i in range(q.qsize()):
		print("reader从Queue中获取到的信息:%s"%q.get(True))

def writer(q):
	print("writer启动(%s),父进程为(%s)"%(os.getpid(), os.getppid()))
	for i in "cjpatrick":
		q.put(i)

if __name__ == "__main__":
	print("(%s) start"%os.getpid())
	q = Manager().Queue()
	po = Pool()
	po.apply(writer, (q,))
	po.apply(reader, (q,))

	po.close()
	po.join()

	print("(%s) End"%os.getpid())
