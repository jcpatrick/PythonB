from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(("192.168.1.5", 8899))

#注意：
#1.tcp客户端已经连接好服务器了，所以后面就不需要填对方的ip和port
#2.udp在发送数据的时候，因为没有之前的链接，所以每次发送都需要
#ip和port
sendData = input("请输入要发送的数据:")
clientSocket.send(sendData.encode("gb2312"))

recvData = clientSocket.recv(1024)
print("recvData:%s"%recvData.decode("gb2312"))
clientSocket.close()
