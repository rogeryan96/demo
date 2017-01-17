d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print d['Bob']
print d.get('ry96','notfound')


class JsonObject(object):
    def __init__(self,dic):
        for key in dic:
            setattr(self,key,dic[key])


obj = JsonObject(d)
print obj.Bob
