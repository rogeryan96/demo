class Person(object):

    a = 'abc'

    def __getattribute__(self, item):
        print '__getattribute__() ' + item
        return object.__getattribute__(self,item)

    def __getattr__(self, item):
        return '__getattr__() ' + item

    def __get__(self, instance, owner):
        return 'instance {0} owner {1}'.format(instance, owner)

class Student(object):
    p = Person()

p = Person()
print p.a
print p.b
print '========================'
s = Student()

print s.p

