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

s1 = Singleton()
s2 = Singleton.getInstance()
print "Object created", s2
s3 = Singleton()
