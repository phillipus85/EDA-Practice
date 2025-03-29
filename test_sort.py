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
from Src.Func.Algorithms.Sorts.mgst import sort as mgst
from Src.Func.Algorithms.Sorts.inst import sort2 as inst
# TODO add other sorting algorithms imports as needed
from Src.Func.Algorithms.Sorts.qkst import sort as qkst
from Src.Func.Algorithms.Sorts.sest import sort as sest
from Src.Func.Algorithms.Sorts.shst import sort as shst


# import dataclass programing sorting algorithms
from Src.Dataclass.Algorithms.Sorts.sest import sort as dcsest
from Src.Dataclass.Algorithms.Sorts.mgst import sort as dcmgst
# TODO also add other sorting algorithms imports as needed
from Src.Dataclass.Algorithms.Sorts.inst import sort as dcinst
from Src.Dataclass.Algorithms.Sorts.shst import sort as dcshst


def sort_crit_by_idx(a: dict, b: dict) -> bool:
    # print(a, b)
    if a["idx"] < b["idx"]:
        return True
    else:
        return False


def sort_crit_by_rating(book1: dict, book2: dict) -> bool:
    r1 = float(book1["average_rating"])
    r2 = float(book2["average_rating"])
    if r1 < r2:
        return True
    else:
        return False


a = arlt.new_list()
b = sllt.new_list()
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

c = arlt.clone(a)
d = sllt.clone(b)
e = arlt.clone(a)
cdc = adc.clone()
ddc = bdc.clone()

print("before sorting")
print("functional implementation")

zipped = zip(arlt.iterator(a),
             sllt.iterator(b),
             arlt.iterator(c),
             sllt.iterator(d))
for ta, tb, tc, td in zipped:
    print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

print("dataclass implementation")
zipped = zip(adc, bdc, cdc, ddc)
for ta, tb, tc, td in zipped:
    print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

# a = mgst(a, sort_crit_by_idx)
b = inst(b, sort_crit_by_idx)
c = qkst(c, sort_crit_by_idx)
d = shst(d, sort_crit_by_idx)
# asc = dcmgst(adc, sort_crit_by_idx)
# bsc = dcinst(bdc, sort_crit_by_idx)
csc = dcsest(cdc, sort_crit_by_idx)
dsc = dcshst(ddc, sort_crit_by_idx)

print("after sorting")
print("functional implementation")
zipped = zip(arlt.iterator(a),
             sllt.iterator(b),
             arlt.iterator(c),
             sllt.iterator(d))
for ta, tb, tc, td in zipped:
    print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

print("dataclass implementation")
zipped = zip(adc, bdc, cdc, ddc)
for ta, tb, tc, td in zipped:
    print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")
