from Src.Func.DataStructs.Trees import bst as te
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.Algorithms.Trees import transversal as transv

t = te.new_tree()

elm_lt = (
    {"id": 0, "data": "A"},     # Root, 0
    {"id": -3, "data": "B"},    # 1
    {"id": 5, "data": "C"},     # 2
    {"id": -7, "data": "D"},     # 3
    {"id": 11, "data": "E"},    # 4
    {"id": -13, "data": "F"},    # 5
    {"id": 2, "data": "G"},    # 6
    {"id": -23, "data": "H"},     # 7
    {"id": 17, "data": "I"},     # 8
    {"id": -1, "data": "J"},    # 9
    # {"id": 27, "data": "K"},     # 10
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
print("==== In-order: ====")
for elm in lt.iterator(transv.in_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")

print("==== Pre-order: ====")
trans_str = ""
for elm in lt.iterator(transv.pre_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")


print("==== Post-order: ====")
trans_str = ""
for elm in lt.iterator(transv.post_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")


print("==== Level-order: ====")
trans_str = ""
# for elm in transv.level_order(t):
for elm in lt.iterator(transv.level_order(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")


print("==== Pre-order Reverse: ====")
trans_str = ""
for elm in lt.iterator(transv.pre_order_reverse(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")


print("====Post-order reverse: ====")
trans_str = ""
for elm in lt.iterator(transv.post_order_reverse(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")


print("==== In-order reverse: ====")
trans_str = ""
for elm in lt.iterator(transv.in_order_reverse(t)):
    trans_str += f"[{elm['id']}, {elm['data']}], "
print(f"\tTrans: {trans_str}\n")
