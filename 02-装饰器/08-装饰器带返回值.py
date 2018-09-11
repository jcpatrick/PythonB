def func(functionName):
    print("----func1----")
    def func_in():
        print("---func_in1----")
        return functionName()
        print("---func_in2----")
    print("----func2-----")
    return func_in
@func
def test():
    print("----test----")
    return "haha"

#test = func(test)
ret = test()
#print(ret)
