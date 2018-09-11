from socket import *
from multiprocessing import Process
def dealWithClient(clientSocket, destAddr):
	while True:
		recvData = clientSocket.recv(1024)
		if len(recvData) > 0:
			print("recv[%s]:%s"%(destAddr,recvData.decode("gb2312")))
		else:
			print("客户端[%s]已经关闭"%str(destAddr))
			break
	clientSocket.close()
	
def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	localAddr = ("", 7788)
	serverSocket.bind(localAddr)
	serverSocket.listen(5)
	try:
		while True:
			
			print("主进程等待客户端的请求")
			clientSocket, destAddr = serverSocket.accept()

			print("---主进程开始处理客户端的请求[%s]---"%str(destAddr))
			clientProcess = Process(target=dealWithClient,args=(clientSocket, destAddr))
			clientProcess.start()
			#这里能够关闭clientSocket，因为多进程中，会在copy一份，两者互不影响
			clientSocket.close()
	finally:
		serverSocket.close()
if __name__ == "__main__":
	main()
