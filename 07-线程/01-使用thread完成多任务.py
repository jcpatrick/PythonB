from threading import Thread
import time

def test():
	print("-----哈哈哈哈哈-----")
	time.sleep(1)

def main():
	for i in range(5):
		t = Thread(target=test)
		t.start()
	print("---ending---")

if __name__ == "__main__":
	main()
