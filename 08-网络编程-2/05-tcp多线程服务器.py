from socket import *
from threading import Thread
def dealWithClient(clientSocket, destAddr):
	while True:
		recvData = clientSocket.recv(1024)
		if len(recvData) > 0:
			print("recv[%s]:%s"%(destAddr,recvData.decode("gb2312")))
		else:
			print("客户端已经关闭")
			break
	clientSocket.close()
	
def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR ,1)
	localAddr = ("", 7788)
	serverSocket.bind(localAddr)
	serverSocket.listen(5)
	try:
		while True:
			
			print("主进程等待客户端的请求")
			clientSocket, destAddr = serverSocket.accept()

			print("---主进程开始处理客户端的请求[%s]---"%str(destAddr))
			clientTask = Thread(target=dealWithClient,args=(clientSocket, destAddr))
			clientTask.start()
			#多线程里面不能关闭，因为给Thread里面传的是引用，双方是共享的
			#而多进程的话，则是会copy一份新的，双方互不影响
			#clientSocket.close()
	finally:
		serverSocket.close()
if __name__ == "__main__":
	main()
