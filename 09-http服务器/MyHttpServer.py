from multiprocessing import Process
from socket import *
import re
import sys

HTML_ROOT = "./html"
WSGI_PYTHON_DIR = "./wsgipython"

class HttpServer(object):
    def __init__(self, app):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = app

    def start_response(self, status, headers):
        '''发送响应信息'''
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers

    def handle_client(self, clientSocket):
        '''处理用户请求'''
        # 获取客户端请求数据
        request_data = clientSocket.recv(1024)
        print("request_data: ", request_data)

        # 使用正则表达式解析请求头
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_data.decode("utf-8")).group(1)
        method = re.match(r"\w+ +/[^ ]*", request_data.decode("utf-8")).group(0)
        #判断请求的是动态资源还是静态资源
        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body
        # 发送请求数据给客户端
        clientSocket.send(bytes(response, "utf-8"))
        # 关闭连接
        clientSocket.close()

    def bind(self, port):
        '''绑定端口号'''
        self.serverSocket.bind(("", port))

    def start(self):
        '''启动服务器'''
        self.serverSocket.listen(128)
        while True:
            clientSocket, destAddr = self.serverSocket.accept()
            p = Process(target=self.handle_client, args=(clientSocket, ))
            p.start()
            clientSocket.close()

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    if len(sys.argv) < 2:
        sys.exit("python MyHttpServer.py Moudle:app")
    moudle_name, app_name = sys.argv[1].split(":")
    #根据模块名称导入模块
    m = __import__(moudle_name)
    #根据模块对象和对应的变量名称导入响应的变量
    app = getattr(m, app_name)
    httpServer = HttpServer(app)
    httpServer.bind(8080)
    httpServer.start()

if __name__ == "__main__":
	main()
