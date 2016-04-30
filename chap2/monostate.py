# method one

class Borg(object):
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print 'Borg Object "b": ', b
print 'Borg Object "b1": ', b1
print 'Object state of b', b.__dict__
print 'Object state of b1', b1.__dict__

# method two


class Monostate(object):
    _shared_state = {}

    def __new__(cls, *args, **kw):
        obj = super(Monostate, cls).__new__(cls, *args, **kw)
        obj.__dict__ = cls._shared_state
        return obj

b = Monostate()
b1 = Monostate()
b.x = 4

print 'Borg Object "b": ', b
print 'Borg Object "b1": ', b1
print 'Object state of b', b.__dict__
print 'Object state of b1', b1.__dict__

