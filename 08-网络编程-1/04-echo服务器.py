from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

addr = ('', 7788)
udpSocket.bind(addr)

while True:
	data = udpSocket.recvfrom(1024)
	print("[%s]:%s"%(str(data[1]),data[0].decode("gb2312")))
	#发送回给对方
	#print(data[1])
	#print(data[0].decode("gb2312"))

	udpSocket.sendto(data[0],data[1])

udpSocket.close()
