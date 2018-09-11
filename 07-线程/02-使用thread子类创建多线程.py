from threading import Thread
import time

class MyThread(Thread):
	def run(self):
		for i in range(5):
			time.sleep(1)
			msg = "I'm" + self.name + "@" + str(i)
			print(msg)

def main():
	t = MyThread()
	t.start()

if __name__ == "__main__":
	main()
