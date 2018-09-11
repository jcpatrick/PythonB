from multiprocessing import Process, Queue
import random, time, os

def write(q):
	for value in ['A', 'B', 'C']:
		print("Put %s to queue"%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print("Get %s from queue"%value)
			time.sleep(random.random())

		else:
			break;

if __name__ == "__main__":
	q = Queue(3)
	pw = Process(target = write, args = (q,))#创建写进程
	pr = Process(target = read, args = (q,))#创建读进程

	pw.start()
	print("------启动写进程----")
	pw.join()

	pr.start()
	print("------启动读进程------")
	pr.join()

