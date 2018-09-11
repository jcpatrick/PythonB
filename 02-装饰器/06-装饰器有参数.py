def func(functionName):
    print("----func1----")
    def func_in(a, b):
        print("---func_in1----")
        functionName(a, b)
        print("---func_in2----")
    print("----func2-----")
    return func_in
@func
def test(a, b):
    print("----test-a=%d,b=%d"%(a, b))

#test = func(test)
test(1, 2)
