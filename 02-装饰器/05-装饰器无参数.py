def func(functionName):
    print("----func1----")
    def func_in():
        print("---func_in1----")
        functionName()
        print("---func_in2----")
    print("----func2-----")
    return func_in
@func
def test():
    print("----test----")

#test = func(test)
test()
