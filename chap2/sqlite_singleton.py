import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kw):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,
                                        cls).__call__(*args, **kw)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.sqlite3')
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()
print "Datebasxe Object DB1", db1
print "Datebasxe Object DB2", db2
