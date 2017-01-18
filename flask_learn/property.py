class Person():
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    def say(self):
        print self._name

    name = property(_get_name,_set_name, doc='')
    del _get_name, _set_name
p = Person('roger')
assert "roger" == p.name
p.name = 'ryan'
assert "ryan" == p.name
print p.__dict__
print object().__dict__

print p.say.__module__

print dir(p)