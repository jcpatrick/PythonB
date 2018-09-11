#def test1():
#    print("---1---")
#
#
#def test1():
#    print("---x---")
#
#test1()

#语法糖

def w1(func):
    def inner():
        print("---正在验证权限---")
        func()
    return inner
@w1
def f1():
    print("---f1---")

@w1
def f2():
    print("---f2---")

#装饰器在被调用的时候才会进行装饰
f1()
f2()
