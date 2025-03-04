# import Src.Func.DataStructs.List.arlt as lt
# from Src.Func.DataStructs.Tables import scht as mp
from Src.Func.DataStructs.Tables import lpht as mp

# a = mp.new_chaining_mp(10, rehashable=True)
a = mp.new_probing_mp(50, rehashable=False)
print(a)

map_lt = (
    {"id": 1, "name": "a"},
    {"id": 2, "name": "b"},
    {"id": 3, "name": "c"},
    {"id": 4, "name": "d"},
    {"id": 5, "name": "e"},
    {"id": 6, "name": "f"},
    {"id": 7, "name": "g"},
    {"id": 8, "name": "h"},
    {"id": 9, "name": "i"},
    {"id": 10, "name": "j"},
    {"id": 11, "name": "k"},
    {"id": 12, "name": "l"},
    {"id": 13, "name": "m"},
    {"id": 14, "name": "n"},
    {"id": 15, "name": "o"},
    {"id": 16, "name": "p"},
    {"id": 17, "name": "q"},
    {"id": 18, "name": "r"},
    {"id": 19, "name": "s"},
    {"id": 20, "name": "t"},
    {"id": 21, "name": "u"},
    {"id": 22, "name": "v"},
    {"id": 23, "name": "w"},
    {"id": 24, "name": "x"},
    {"id": 25, "name": "y"},
    {"id": 26, "name": "z"}
)

print("add elements to map")
for elm in map_lt:
    print(elm)
    mp.put(a, elm["id"], elm)
print(a)

print("get elements from map")
for elm in map_lt:
    print(mp.get(a, elm["id"]))

print(mp.size(a))
print(mp.is_empty(a))
print(a)


# print("remove elements from map")
# for elm in map_lt[10:21]:
#     print(elm)
#     a = mp.remove(a, elm["id"])
# print(mp.size(a))
# print(mp.is_empty(a))

# print("contains elements in map")
# for elm in map_lt:
#     found = mp.contains(a, elm["id"])
#     if found:
#         entry = mp.get(a, elm["id"])
#         print(entry)
# print(mp.size(a))
# print(mp.is_empty(a))

# print("keys and values")
# keys = mp.keys(a)
# print(keys)

# values = mp.values(a)
# print(values)
