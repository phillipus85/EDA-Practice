# import python modules
# from typing import Callable
import random

# functional style structure import
from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
# dataclass style structure import
from Src.Dataclass.DataStructs.Lists.arlt import Arraylist
from Src.Dataclass.DataStructs.Lists.sllt import Singlelinked

# import functional programing sorting algorithms
from Src.Func.Algorithms.Sorts.mgst import sort as mst
from Src.Func.Algorithms.Sorts.inst import sort as ist
from Src.Func.Algorithms.Sorts.sest import sort as sest
from Src.Func.Algorithms.Sorts.shst import sort as shst
# TODO add other sorting algorithms imports as needed
# from Src.Func.Algorithms.Sorts.qkst import sort as qst

# import dataclass programing sorting algorithms
from Src.Dataclass.Algorithms.Sorts.sest import sort as dcsest
from Src.Dataclass.Algorithms.Sorts.mgst import sort as dcmgst
# TODO also add other sorting algorithms imports as needed
# from Src.Dataclass.Algorithms.Sorts.inst import sort as dcinst


def sort_crit_by_idx(a: dict, b: dict) -> bool:
    # print(a, b)
    if a["idx"] < b["idx"]:
        return True
    else:
        return False


a = arlt.new_array_lt()
b = sllt.new_single_lt()
adc = Arraylist()
bdc = Singlelinked()

for i in range(1, 27):
    idx = random.randint(13 * i, 42 * (i + 1))
    temp = {"id": i,
            "idx": idx,
            "name": chr(96 + i)}
    arlt.add_last(a, temp)
    adc.add_last(temp)
    sllt.add_last(b, temp)
    bdc.add_last(temp)

print("before sorting")
print("functional implementation")
for ta, tb in zip(arlt.iterator(a), sllt.iterator(b)):
    print(ta, tb)
print("dataclass implementation")
for ta, tb in zip(adc, bdc):
    print(ta, tb)

a = sest(a, sort_crit_by_idx)
b = shst(b, sort_crit_by_idx)
asc = dcsest(adc, sort_crit_by_idx)
bsc = dcmgst(bdc, sort_crit_by_idx)

print("after sorting")
print("functional implementation")
for ta, tb in zip(arlt.iterator(a), sllt.iterator(b)):
    print(ta, tb)

print("dataclass implementation")
for ta, tb in zip(asc, bsc):
    print(ta, tb)
