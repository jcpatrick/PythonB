from multiprocessing import Process
from socket import * 

def handle_client(clientSocket, destAddr):
	#获取客户端请求数据
	request_data = clientSocket.recv(1024)
	print("request_data: ",request_data)
	#构造服务端响应数据
	response_start_line = "HTTP1.1 200 OK\r\n"
	response_headers = "Server:My Server\r\n"
	response_body = "hello world"
	response = response_start_line + response_headers + "\r\n" + response_body
	clientSocket.send(bytes(response, "utf-8"))
	#关闭连接
	clientSocket.close()

def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	localAddr = ('', 7788)
	serverSocket.bind(localAddr)
	serverSocket.listen(5)

	while True:
		clientSocket,destAddr = serverSocket.accept()
		p = Process(target=handle_client, args=(clientSocket, destAddr))
		p.start()
		clientSocket.close()


if __name__ == "__main__":
	main()
