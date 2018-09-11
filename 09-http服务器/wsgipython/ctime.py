import time

def application(env, start_response):
    """env包含用户的所有请求信息
    """
    try:
        result = time.ctime()
        status = "200 OK"
    except:
        status = "500 ERROR"

    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return result