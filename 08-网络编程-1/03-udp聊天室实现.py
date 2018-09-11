from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

addr = ('', 7788)
udpSocket.bind(addr)

while True:
	data = udpSocket.recvfrom(1024)
	msg = data[0].decode("GB2312")
	ipMsg = data[1]
	ipAddr = ipMsg[0]
	port = ipMsg[1]
	print("recv from %s:%d :%s"%(ipAddr,port,msg))

udpSocket.close()
