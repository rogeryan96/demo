classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
try:
    print classmates[3]
except Exception as e:
    print e
print classmates[-1]
print classmates[-2]
try:
    print classmates[-4]
except Exception as e:
    print e

classmates.append('Adam')
print classmates

classmates.insert(1, 'Jack')
print classmates

print classmates.pop()
print classmates.pop(1)
print classmates
L = ['Apple', 123, True]
print L
s = ['python', 'java', ['asp', 'php'], 'schema']
print len(s)
L = []
print len(L)
t = (1,2)
print t
t = ()
print t
t = (1)
print t
t = (1,)
print t
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t