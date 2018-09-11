from socket import *
	
def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	localAddr = ("", 7788)
	serverSocket.bind(localAddr)
	serverSocket.setblocking(False)
	serverSocket.listen(50)
	clientAddrList = []

	while True:
		try:
			clientSocket,destAddr = serverSocket.accept()
		except:
			pass
		else:
			print("一个新的客户端到来:%s"%str(destAddr))
			clientSocket.setblocking(False)
			clientAddrList.append((clientSocket, destAddr))

		for clientSocket, destAddr in clientAddrList:
			try:
				recvData = clientSocket.recv(1024)
			except:
				pass
			else:
				if len(recvData) > 0:
					print("%s:%s"%(str(destAddr), recvData.decode("gb2312")))
				else:
					clientSocket.close()
					clientAddrList.remove((clientSocket, destAddr))
					print("%s已经下线"%str(destAddr))
			

if __name__ == "__main__":
	main()
