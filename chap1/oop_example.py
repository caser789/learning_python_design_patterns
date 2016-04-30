class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return "<Person ({name}, {age})>".format(name=self.name,
                                                 age=self.age)


if __name__ == '__main__':
    name = 'John'
    age = 32
    p = Person(name, age)
    print "Type of Object is {t}, and its Memory Address is {addr}".format(
        t=type(p),
        addr=id(p),
    )
