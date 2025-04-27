from Src.Func.DataStructs.Trees import bst as te
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.Algorithms.Trees import transversal as transv

t = te.new_tree()

elm_lt = (
    {"id": 0, "data": "A"},
    {"id": -3, "data": "B"},
    {"id": 2, "data": "C"},
    {"id": 1, "data": "D"},
    {"id": 11, "data": "E"},
    {"id": -8, "data": "F"},
    {"id": -2, "data": "G"},
    {"id": 5, "data": "H"},
    {"id": 9, "data": "I"},
    {"id": -4, "data": "J"},
    {"id": 7, "data": "K"},
    {"id": -5, "data": "L"},
    {"id": 13, "data": "M"},
    {"id": 3, "data": "N"},
)

for elm in elm_lt:
    print(elm)
    te.insert(t, elm["id"], elm)

print(t)
print(te.size(t))
print(te.is_empty(t))
print(te.height(t))

in_order = transv.in_order(t)
pre_order_rev = transv.pre_order_reverse(t)

trans_str = ""
print("In-order:")
for elm in lt.iterator(transv.in_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(trans_str)

print("Pre-order reverse:")
trans_str = ""
for elm in lt.iterator(transv.pre_order_reverse(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(trans_str)

print("Pre-order:")
trans_str = ""
for elm in lt.iterator(transv.pre_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(trans_str)

print("Post-order:")
trans_str = ""
for elm in lt.iterator(transv.post_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(trans_str)
