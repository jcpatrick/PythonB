from socket import *
import select

def main():
	serverSocket = socket(AF_INET,SOCK_STREAM)
	localAddr = ('', 7788)
	serverSocket.bind(localAddr)
	serverSocket.listen(50)

	#创建epoll对象
	epoll = select.epoll()

	#注册socket监听事件
	epoll.register(serverSocket.fileno(), select.EPOLLIN|select.EPOLLET)

	#创建客户端socket列表和地址信息列表
	socketConditions = {}
	addrConditions = {}
	

	while True:
		#获取有事件通知的列表
		epoll_list = epoll.poll()
		#遍历事件通知列表
		for fd, event in epoll_list:
			#处理客户端连接
			if fd == serverSocket.fileno():
				clientSocket, destAddr = serverSocket.accept()
				print("用户%s已连接"%str(destAddr))
				socketConditions[clientSocket.fileno()] = clientSocket
				addrConditions[clientSocket.fileno()] = destAddr

				epoll.register(clientSocket.fileno(), select.EPOLLIN|select.EPOLLET)
			#接收客户端消息
			elif event == select.EPOLLIN:
				clientSocket = socketConditions[fd]
				destAddr = addrConditions[fd]
				recvData = clientSocket.recv(1024)
				if recvData:
					print("%s:%s"%(str(destAddr),recvData.decode("gb2312")))
				else:
					epoll.unregister(clientSocket.fileno())
					del(socketConditions[fd])
					del(addrConditions[fd])
					clientSocket.close()
					clientSocket.close()

if __name__ == "__main__":
	main()
