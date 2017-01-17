def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc(*numbers):
    print numbers
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1,2)
print calc()
print calc(*[1,2,3])

def person(name, age, **kw):
    print 'name', name, 'age', age, 'other', kw

person('Roger', 34, city='ChengDu')