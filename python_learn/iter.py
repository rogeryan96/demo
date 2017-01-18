d = {'a': 1, 'b': 2,'c': 3}

for key in d.iterkeys():
    print key

for value in d.itervalues():
    print value

for key, value in d.iteritems():
    print key, value

from collections import Iterable

print isinstance(d, Iterable)

for i,value in enumerate(d):
    print i ,value

for x, y in [(1, 1), (2, 4), (3,9)]:
    print x, y