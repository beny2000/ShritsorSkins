class Foo():
    def __init__(self):
        self.x = 42

class Bar(object):
    def __init__(self, foo):
        print(foo.x)

a = Foo()
b = Bar(a)
