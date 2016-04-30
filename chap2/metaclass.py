class MyInt(type):

    def __call__(cls, *args, **kw):
        print '******** here is my int ********'
        print 'Now do whatever you want with these objects...'
        return type.__call__(cls, *args, **kw)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4, 5)
