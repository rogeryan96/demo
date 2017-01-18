def add(x,y,f):
    return f(x) + f(y)

assert 11 == add(-5,6,abs)