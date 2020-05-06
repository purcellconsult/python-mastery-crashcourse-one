from collections import OrderedDict

od = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
od.move_to_end('b')
print(od)
od.move_to_end('c', last=False)
print(od)
od.popitem()
('b', 2)