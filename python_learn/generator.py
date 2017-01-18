g = (x * x for x in range(10))
print g, type(g)

for value in g:
    print value


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print b
        a,b = b, a+b
        n = n + 1

fib(6)

def fib_generator(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n = n + 1

print fib_generator(6)