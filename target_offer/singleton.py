
def singleton(cls, *args, **kw):
    classlist = {}
    def single():
        if 'cls' not in classlist:
            classlist['cls'] = cls(*args, **kw)
        return classlist['cls']
    return single

@singleton
class Myclass(object):
    def __init__(self, x = 10):
        self.x = x

one = Myclass()
two = Myclass()
print(one == two)
one.x = 3
print(two.x)