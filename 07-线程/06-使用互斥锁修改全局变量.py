from threading import Thread,Lock
import time

glb_num = 0
lock = Lock()#创建一个互斥锁
def work1():
	global glb_num
	#这个线程和work2中的线程都会争抢这个所, 一方上锁,那么另一方就会阻塞,知道这个所被释放为止
	lock.acquire()
	for i in range(1000000):
		glb_num += 1
	print("----work1----%d"%glb_num)
	lock.release()#释放锁,只有释放锁之后，其他线程才能进行执行

def work2():
	global glb_num,flag
	lock.acquire()
	for i in range(1000000):
		glb_num += 1
	print("----work2----%d"%glb_num)
	lock.release()
def main():

	t1 = Thread(target=work1)
	t1.start()
	
	#time.sleep(3)#确保work1执行完之后再执行work2
	
	t2 = Thread(target=work2)
	t2.start()

if __name__ == "__main__":
	main()
