import threading

local_school = threading.local()

def process_student():
	std = local_school.student
	print("Hello, %s (in %s)" %(std, threading.current_thread().name))

def process_thread(name):
	local_school.student = name
	process_student()
#name是线程名称
t1 = threading.Thread(target = process_thread, args = ("zss",), name = "Thread---A")
t2 = threading.Thread(target = process_thread, args = ("ls",), name = "Thread---B")

t1.start()
t2.start()

t1.join()
t2.join()
