from Src.Func.DataStructs.List import arlt
# from Src.Func.DataStructs.List import sllt
from Src.Func.Algorithms.Sorts.mgst import sort as mst
from Src.Func.Algorithms.Sorts.inst import sort as ist
from Src.Func.Algorithms.Sorts.qkst import sort as qst
# from Src.Func.Algorithms.Sorts.shst import sort as sst
# from Src.Func.Algorithms.Sorts.sest import sort as sst
# from typing import Callable
import random


def sort_crit_by_idx(a: dict, b: dict) -> bool:
    # print(a, b)
    if a["idx"] < b["idx"]:
        return True
    else:
        return False


a = arlt.new_array_lt()

for i in range(1, 10):
    idx = random.randint(13 * i, 42 * (i + 1))
    arlt.add_last(a, {"id": i,
                      "idx": idx,
                      "name": chr(96 + i)})

print("before sorting")
for elm in arlt.iterator(a):
    print(elm)

a = mst(a, sort_crit_by_idx)

print("after sorting")
for elm in arlt.iterator(a):
    print(elm)
