from socket import *
from threading import Thread

udpSocket = None
localPort = None
remotePort = None
remoteIp = None
chatingFlag = True

def recvData():
	global udpSocket
	global chatingFlag
	while chatingFlag:
		remoteData = udpSocket.recvfrom(1024)
		recvMsg = remoteData[0].decode("gb2312")
		print("\n>>>[%s]:%s\n<<<："%(remoteData[1],recvMsg), end='')
		if recvMsg.rstrip() == "bye":
			chatingFlag = False


def sendMsg():
	global udpSocket
	global remotePort
	global remoteIp
	global chatingFlag

	while chatingFlag:
		sendData = input("<<<:")
		udpSocket.sendto(sendData.encode(encoding="gb2312"), (remoteIp, remotePort))
		if sendData.rstrip() == "bye":
			chatingFlag = False


def main():
	global udpSocket
	global localPort
	global remotePort
	global remoteIp
	
	#localPort = int(input("请输入本地端口："))
	#remoteIp = input("请输入远端IP：")
	#remotePort = int(input("请输入远端端口："))

	localPort = 8888 
	remoteIp = "192.168.1.5"
	remotePort = 8888

	udpSocket = socket(AF_INET, SOCK_DGRAM)
	udpSocket.bind(("", localPort))

	recvThread = Thread(target=recvData)
	sendThread = Thread(target=sendMsg)

	recvThread.start()
	sendThread.start()

	recvThread.join()
	sendThread.join()

if __name__ == "__main__":
	main()
