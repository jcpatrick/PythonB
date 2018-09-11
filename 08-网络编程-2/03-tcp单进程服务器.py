from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#使得服务器端开始主动接收请求
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

localAddr = ("", 7788)

serverSocket.bind(localAddr)

serverSocket.listen(5)

while True:
	
	clientSocket,destAddr = serverSocket.accept()
	try:
		while True:
			recvData = clientSocket.recv(1024)
			if len(recvData) > 0:
				print("recv[%s]:%s"%(destAddr, recvData.decode("gb2312")))
			else:
				#如果接收到的消息长度为0，表示客户端关闭了socket
				print("客户端已经关闭")
				break
	finally:
		clientSocket.close()
serverSocket.close()
