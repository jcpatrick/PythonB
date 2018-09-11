from threading import Thread
import time

glb_num = 0

def work1():
	global glb_num
	for i in range(1000000):
		glb_num += 1
	print("----work1----%d"%glb_num)
def work2():
	global glb_num
	for i in range(1000000):
		glb_num += 1
	print("----work2----%d"%glb_num)

def main():
	t1 = Thread(target=work1)
	t1.start()
	
	time.sleep(3)#确保work1执行完之后再执行work2
	
	t2 = Thread(target=work2)
	t2.start()

if __name__ == "__main__":
	main()
