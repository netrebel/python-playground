import collections
def comparer(desc, attr):
    def fn(a, b):
        a_attr, b_attr = getattr(a, attr), getattr(b, attr)
        return [None, None] if a_attr == b_attr else [desc, '{} <> {}'.format(a_attr, b_attr)]
    return fn
class Obj(object):
    def __init__(self, name, dist):
        self.name = name
        self.dist = dist
comps = [comparer('name', 'name'), comparer('distance', 'dist')]
a = Obj('a', 10)
b = Obj('b', 10)
c = Obj('c', 30)
aa = Obj('a', 40)

a_b_comps = {field: msg for (field, msg) in [comp(a, b) for comp in comps] if field}
a_c_comps = {field: msg for (field, msg) in [comp(a, c) for comp in comps] if field}
a_aa_comps = {field: msg for (field, msg) in [comp(a, aa) for comp in comps] if field}

print(a_b_comps)                           # {'name': 'a <> b'}
print(a_c_comps)                           # {'distance': '10 <> 30', 'name': 'a <> c'}
print(a_aa_comps)                          # {'distance': '10 <> 40'}