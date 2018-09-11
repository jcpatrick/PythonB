#多个装饰器-----装饰者模式
def makeBold(func):
    def wrapped():
        print("-----1----")
        return "<b>" + func() + "</b>"
    return wrapped

def makeItalic(func):
    def wrapped():
        print("-----2----")
        return "<i>" + func() + "</i>"
    return wrapped

#根据顺序从上到下调用装饰器
@makeBold
@makeItalic
def f1():
    print("-----3----")
    return "hello world"

#@makeItalic
#@makeBold
#def f2():
#    print("---f2---")

ret = f1()
print(ret)
#f2()
