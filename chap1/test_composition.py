class A(object):

    def a1(self):
        print "a1"


class B(object):

    def b1(self):
        print "b1"
        A().a1()


if __name__ == '__main__':
    b = B()
    b.b1()
