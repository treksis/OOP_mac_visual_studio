def inc(x):
    return x+1

def dec(x):
    return x-1

def operate(func, x):
    result = func(x)
    return result

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")


if __name__ == '__main__':
    
    pretty = make_pretty(ordinary)
    pretty()
