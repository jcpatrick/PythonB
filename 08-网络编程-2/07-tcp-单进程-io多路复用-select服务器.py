from socket import *
import select
import sys

def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	localAddr = ('', 7788)
	serverSocket.bind(localAddr)

	serverSocket.listen(50)

	inputs = [serverSocket,sys.stdin]

	while True:
		readable, writeable, exceptional = select.select(inputs, [], [])
		for sock in readable:
			if sock == serverSocket:
				clientSocket,destAddr = sock.accept()
				print("%s已连接服务器"%str(destAddr))
				inputs.append(clientSocket)
			
			#监听键盘输入
			elif sock == sys.stdin:
				cmd = sys.stdin.readline()
				running = False
				break
			else:
				recvData = sock.recv(1024)
				if recvData:
					print("接收到的数据:%s"%recvData.decode("gb2312"))
					sock.send(recvData)
				else:
					#收到的长度为0，表示客户端关闭连接
					inputs.remove(sock)
					sock.close()

		#写socket
		for sock in writeable:
			pass

		#异常socket
		for sock in exceptional:
			pass

	serverSocket.close()

if __name__ == "__main__":
	main()
