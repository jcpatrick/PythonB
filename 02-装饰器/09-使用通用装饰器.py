def func(functionName):
    print("----func1----")
    def func_in(*args, **kwargs):#加入通用参数接收
        print("---func_in1----")
        ret = functionName(*args, **kwargs)
        print("---func_in2----")
        return ret#没有返回值就会None，这样就可以对有返回值和无返回值进行共同处理
    print("----func2-----")
    return func_in
@func
def test():
    print("----test----")
    return "haha"

@func
def test2():
    print("-----test2----")

@func
def test3(a, b):
    print("-----test3-a=%d, b=%d"%(a, b))

#test = func(test)
ret = test()#有接收则表示有返回值，没有接收则没有返回值
print(ret)

test2()

test3(3,7)
