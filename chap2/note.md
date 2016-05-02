1. one globally accessed object

2. logging, database operation, printer spooler

3. thread pools, caches, dialog boxes, registry settings

## singleton

```
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
```

## lazy instantiation

```
class Singleton(object):
    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            print "__init__ method called .."
        else:
            print "Instance already created:", self.getInstance()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
        return cls.__instance
```

3. python's module is Singleton


## only one object of a class VS different instances sharing the same state -- The Monostate pattern

## metaclass 

```
A = type(name, bases, dict)
```

```
class MyInt(type):

    def __call__(cls, *args, **kw):
        print '******** here is my int ********'
        print 'Now do whatever you want with these objects...'
        return type.__call__(cls, *args, **kw)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## drawbacks

global variable
