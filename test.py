# import Src.Func.DataStructs.List.arlt as lt
from Src.Func.DataStructs.List import sllt as lt

# a = lt.new_array_lt()
a = lt.new_list()
# print(a)
lt.add_last(a, {"id": 1, "name": "a"})
# print(a)
lt.add_last(a, {"id": 2, "name": "b"})
# print(a)
lt.add_first(a, {"id": 3, "name": "c"})
cmp = lt.compare(a, lt.get_first(a), lt.get_last(a))
print(cmp)

for elm in lt.iterator(a):
    print("Element:", elm)
print("Size:", lt.size(a))
print("Is empty:", lt.is_empty(a))
lt.exchange(a, 0, 2)
for elm in lt.iterator(a):
    print("Element:", elm)
# print(a)

present = lt.find(a, {"id": 1, "name": "a"})
print(present)
print(a)

b = lt.sub_list(a, 0, 1)
print(b)

lt.update(b, 0, {"id": 4, "name": "d*"})
print(b)

c = lt.concat(a, b)
print(c)

lt.remove_first(c)
print(c)
