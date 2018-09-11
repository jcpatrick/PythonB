from socket import *

#创建udp套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#接收方的地址
sendAddr = ("192.168.1.5", 8080)

#从键盘获取数据
sendData = input("请输入要发送的数据:")

#转码
sendData = sendData.encode(encoding="utf-8")

#发送消息到指定服务器上,如果sendData的位置直接写的是字符串，则前面加个b就可以，否则需要先转码
udpSocket.sendto(sendData, sendAddr)
#udpSocket.sendto(b"sendData", sendAddr)

#关闭套接字
udpSocket.close()
