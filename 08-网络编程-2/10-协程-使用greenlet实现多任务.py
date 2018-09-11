from greenlet import greenlet
import time

def test1():
	while True:
		print("---A---")
		gl2.switch()
		time.sleep(0.5)
def test2():
	while True:
		print("---B---")
		gl1.switch()
		time.sleep(0.5)

gl1 = greenlet(test1)
gl2 = greenlet(test2)

def main():
	gl1.switch()

if __name__ == "__main__":
	main()
