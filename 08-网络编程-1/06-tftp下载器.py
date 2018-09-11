from socket import *
import struct
import os

def main():
	
	downloadFileName = input("请输入要下载的文件名：")
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	requestField = struct.pack("!H%dsb5sb"%len(downloadFileName),1,bytes(downloadFileName, encoding="utf-8"),0,bytes("octet",encoding="utf-8"),0)

	udpSocket.sendto(requestField,("192.168.1.5",69))
	
	flag = True
	num = 0
	#写入的是二进制文件是可以加上b表示二进制文件
	#但是这样的话对于正常的一些文本文件之类的就会有问题了
	f = open(downloadFileName, "wb")

	while True:
		responseData = udpSocket.recvfrom(1024)
		recvData,serverInfo = responseData
		#操作码(是个元组）
		opNum = struct.unpack("!H", recvData[:2])
		#块编号
		blockNum = struct.unpack("!H", recvData[2:4])
		
		if opNum[0] == 3:
			#计算应该接收到的文件的序号
			num = num + 1
			# 如果一个下载的文件特别大，即接收到的数据包编号超过了2个字节的大小
			# 那么会从0继续开始，所以这里需要判断，如果超过了65535 那么就改为0
			if num ==65536:
				num = 0
			#判断这次服务器发送过来的块编号和本地累加的块编号是否相同
			#如果是才会写入到文件中，否则不写（因为会出现重复）
			if num == blockNum[0]:
				#暂时先这么处理，对于不同的文件，编码会有问题
				f.write(recvData[4:])
				num = blockNum[0]

			ackData = struct.pack("!HH", 4, blockNum[0])
			udpSocket.sendto(ackData,serverInfo)

		elif opNum[0] == 5:
			print("没有这个文件....")
			flag = False

		if len(recvData) < 516:
			break
	if flag == True:
		f.close()
	else:
		os.unlink(downloadFileName)#没有下载到这个文件，应该把本地创建的文件删除

if __name__ == "__main__":
	main()
