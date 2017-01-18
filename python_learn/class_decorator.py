class myDecorator(object):

    def __init__(self, fn, name=None):
        if name is None:
            name = fn.__name__
        print 'inside myDecorator.__init__()'
        self.fn = fn
        self.name = name

    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__() {0}".format(self.name)

@myDecorator
def aFunction():
    print 'inside aFunction()'

aFunction()
aFunction()

class makeHtmlTagClass(object):
    def __init__(self, tag, css_class=""):
        print tag,css_class
        self._tag =tag
        self._css_class = " class='{0}'".format(css_class) if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args,**kwargs):
            return "<" + self._tag + self._css_class + ">" + fn(*args, **kwargs) + "</" + self._tag + ">"
        return wrapped

@makeHtmlTagClass(tag="b", css_class='bold_css')
@makeHtmlTagClass(tag="i", css_class='italic_css')
def hello(name):
    return "Hello, {0}".format(name)

print hello('Roger Yan')