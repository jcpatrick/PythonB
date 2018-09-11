from ctypes import *
from threading import Thread

#加载动态库
lib = cdll.LoadLibrary("./libDeadLoop.so")

#创建一个子线程,让其执行C语言编写的函数
t = Thread(target=lib.DeadLoop)
t.start()

#主线程也调用c语言编写的那个死循环函数
#lib.DeadLoop()

while True:
	pass
