from MyHttpServer import HttpServer
import time

HTML_ROOT = "./html"

class MyApplication(object):
    def __init__(self, urls):
        self.urls = urls
    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        if path == "/":
            path = "/index.html"

        #如果是静态资源或者是直接访问的index.html就会直接访问静态资源
        if path.startswith("/static") or path == "/index.html":
            if path != "/index.html":
                statis_file_name = path[7:]
            else:
                statis_file_name = path
            try:
                # 打开相应的静态资源
                f = open(HTML_ROOT + statis_file_name, "rb")
            except IOError:
                status = "404 File Not Found"
                response_headers = [
                    ("Server", "MyServer")
                ]
                start_response(status, response_headers)
                return "not found"
            else:
                file_data = f.read()
                f.close()
                # 构造服务端响应数据
                status = "200 OK"
                response_headers = [
                    ("Server", "MyServer")
                ]
                start_response(status, response_headers)
                return file_data.decode("utf-8")
        #处理非静态资源
        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)
        status = "404 File Not Found"
        headers = []
        start_response(status, headers)
        return "not found"


def showCtime(env, start_response):
    try:
        #执行程序
        result = time.ctime()
    except :
        #异常处理
        status = "500 Error"
        headers = [
            ("Server", "MyServer")
        ]
        start_response(status, headers)
        return "error"
    else:
        status = "200 OK"
        headers = [
            ("Server", "MyServer")
        ]
        start_response(status, headers)
        return result
def sayHello(env, start_response):
    status = "200 OK"
    headers = [
        ("Server", "MyServer")
    ]
    start_response(status, headers)
    return "<h1>hello</h1>"
urls = [
    ("/ctime", showCtime),
    ("/sayhello", sayHello)
]
app = MyApplication(urls)
# if __name__ == "__main__":
#     urls = [
#         ("/ctime", showCtime)
#     ]
#     app = MyApplication(urls)
#     httpServer = HttpServer(app)
#     httpServer.bind(8080)
#     httpServer.start()