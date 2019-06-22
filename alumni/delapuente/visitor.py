
class dict_values:

    def __init__(self, something):
        self._visitable = something

    def __iter__(self):
        for value in self._visitable.__dict__.values():
            yield value


class filtered_dict_values_per_key:

    def __init__(self, filter, something):
        self._filter = filter
        self._visitable = something

    def __iter__(self):
        something = self._visitable
        for value in filter(lambda p: self._filter(p[0]), something.__dict__.items()):
            yield value[1]


class Visitable:

    def accept(self, visitor):
        yield from visitor.visit(self)


v = Visitable()
v.a = 1
v.b = 2
v.z = 3
v.zz = 4

for value in filtered_dict_values_per_key(lambda k: k[0] == 'z', v):
    print(value)
