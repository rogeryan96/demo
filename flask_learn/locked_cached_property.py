from threading import RLock

_missing = object()

class locked_cached_property(object):
    """A decorator that converts a function into a lazy property.  The
    function wrapped is called the first time to retrieve the result
    and then that calculated result is used the next time you access
    the value.  Works like the one in Werkzeug but has a lock for
    thread safety.
    """

    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func
        self.lock = RLock()
        print '__init__', self.__dict__

    def __get__(self, obj, type=None):
        if obj is None:
            print 'obj is None'
            return self
        with self.lock:
            print 'before if obj dict', obj.__dict__
            value = obj.__dict__.get(self.__name__, _missing)
            if value is _missing:
                print 'missing'
                value = self.func(obj)
                obj.__dict__[self.__name__] = value
                print 'obj __dict__ ', obj.__dict__
            return value

class Person(object):

    @locked_cached_property
    def get_name(self):
        return "hello world"

p = Person()
print p.__dict__
print 'first'
print p.get_name
print p.__dict__
print 'second'
print p.get_name

