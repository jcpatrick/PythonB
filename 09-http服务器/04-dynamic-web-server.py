from multiprocessing import Process
from socket import *
import re
import sys

HTML_ROOT = "./html"
WSGI_PYTHON_DIR = "./wsgipython"

class HttpServer(object):
    def __init__(self, localAddr):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSocket.bind(localAddr)

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers +=  "%s: %s\r\n" % header
        self.response_headers = response_headers

    def handle_client(slef, clientSocket):

        # 获取客户端请求数据
        request_data = clientSocket.recv(1024)
        print("request_data: ", request_data)

        # 使用正则表达式解析请求头
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_data.decode("utf-8")).group(1)
        method = re.match(r"\w+ +/[^ ]*", request_data.decode("utf-8")).group(0)
        #判断请求的是动态资源还是静态资源
        if file_name.endswith(".py"):
            try:
                m = __import__(file_name[1:-3])
            except:
                slef.response_headers = "HTTP/1.1 404 File Not Found\r\n"
                response_body = "not found"
            else:
                #用户请求参数
                env = {
                    "PATH_INFO" : file_name,
                    "METHOD" : method
                }
                response_body = m.application(env, slef.start_response)
            response = slef.response_headers + "\r\n" + response_body
        else:
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


    def start(self):
        self.serverSocket.listen(128)
        while True:
            clientSocket, destAddr = self.serverSocket.accept()
            p = Process(target=self.handle_client, args=(clientSocket, ))
            p.start()
            clientSocket.close()

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    localAddr = ('', 7788)
    httpServer = HttpServer(localAddr)
    httpServer.start()

if __name__ == "__main__":
	main()
