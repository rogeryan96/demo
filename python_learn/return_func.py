def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
f1 = lazy_sum(1,3,5,7,9)
print f
print f()
assert f != f1

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

def count_fix():
    fs = []
    for i in range(1,4):
        def f(j):
            return lambda : j * j
        fs.append(f(i))
    return fs

f1, f2, f3 = count_fix()

print f1(), f2(), f3()