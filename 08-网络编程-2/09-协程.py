import time

def testA():
	while True:
		print("---A---")
		yield
		time.sleep(0.5)


def testB(c):
	while True:
		print("----B---")
		c.__next__()
		time.sleep(0.5)

if __name__ == "__main__":
	a = testA()
	testB(a)
