def test(a, b):
    print("a----%d\nb----%d"%(a,b))
    def test_in(x):
        print(a*x + b)
    return test_in

line = test(1,2)
line(1)