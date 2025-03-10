from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from Src.Func.Algorithms.Sorts.mergesort import sort as mst
from typing import Callable
import random


def sort_crit_by_idx(a: dict, b: dict) -> bool:
    # print(a, b)
    return a["idx"] <= b["idx"]


a = arlt.new_array_lt()

for i in range(1, 27):
    idx = random.randint(13 * i, 42 * (i + 1))
    arlt.add_last(a, {"id": i,
                      "idx": idx,
                      "name": chr(96 + i)})

print(a)

a = mst(a, sort_crit_by_idx)


for elm in arlt.iterator(a):
    print(elm)
