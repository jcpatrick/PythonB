from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",8899))
serverSocket.listen(5)

clientSocket,clientInfo = serverSocket.accept()
#clientSocket表示客户端
#clientInfo表示这个客户端的ip和port

recvData = clientSocket.recv(1024)

print("%s:%s"%(str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()
