class Obj(object):

    def __init__(self, name):
        self.items = {'name' : name}

    def __getattr__(self, item):
        return  self.items[item] if item in self.items else "{0} not found".format(item)


obj = Obj("roger")
print getattr(obj,"name")
print getattr(obj,"roger")