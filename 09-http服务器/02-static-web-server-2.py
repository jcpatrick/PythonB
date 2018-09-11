from multiprocessing import Process
from socket import *
import re

HTML_ROOT = "./html"


def handle_client(clientSocket, destAddr):
    # 获取客户端请求数据
    request_data = clientSocket.recv(1024)
    print("request_data: ", request_data)

    # 使用正则表达式解析请求头
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_data.decode("utf-8")).group(1)
    if file_name == "/":
        file_name = "/index.html"
    try:
        # 打开相应的html文件
        f = open(HTML_ROOT + file_name, "rb")
    except IOError:
        response_start_line = "HTTP1.1 404 File Not Found\r\n"
        response_headers = "Server:My Server\r\n"
        response_body = "File Not Found"
    else:
        file_data = f.read()
        f.close()
        # 构造服务端响应数据
        response_start_line = "HTTP1.1 200 OK\r\n"
        response_headers = "Server:My Server\r\n"
        response_body = file_data.decode("utf-8")
    response = response_start_line + response_headers + "\r\n" + response_body
    # 发送请求数据给客户端
    clientSocket.send(bytes(response, "utf-8"))
    # 关闭连接
    clientSocket.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serverSocket.bind(localAddr)
    serverSocket.listen(128)

    while True:
        clientSocket, destAddr = serverSocket.accept()
        p = Process(target=handle_client, args=(clientSocket, destAddr))
        p.start()
        clientSocket.close()


if __name__ == "__main__":
    main()
