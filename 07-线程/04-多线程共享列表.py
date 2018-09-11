from threading import Thread
import time

def work1(nums):
	nums.append(44)
	print("----work1----%s"%str(nums))
def work2(nums):
	time.sleep(1)
	print("----work2----%s"%str(nums))

def main():
	nums = [11,22,33]

	t1 = Thread(target=work1, args=(nums,))
	t1.start()
	
	#time.sleep(3)#确保work1执行完之后再执行work2
	
	t2 = Thread(target=work2, args=(nums,))
	t2.start()

if __name__ == "__main__":
	main()
