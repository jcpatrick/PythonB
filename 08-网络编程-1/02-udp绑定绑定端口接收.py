from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

#绑定本地相关信息，如果一个网络程序不绑定，则会随机分配
bindAddr = ('', 7788)
udpSocket.bind(bindAddr)

while True:
	recvData = udpSocket.recvfrom(1024)#表示本次请求最大接收1024字节）
	data = recvData[0].decode("gb2312")#发送的软件用的是gb2312的编码，所以在这里也要用这个编码进行解码
	print(data)
	if recvData == "bye":
		break

udpSocket.close()
