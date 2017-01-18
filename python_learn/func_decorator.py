def now():
    print '2013-12-25'

f = now
f()
print now.__name__, f.__name__

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now_1():
    print '2013-12-25'

now_1()

