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
from Src.Func.Algorithms.Sorts.inst import sort as inst
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

# recursive implementation of insertion sort
from Src.Func.Algorithms.Sorts.inst import sort_r as instr


def sort_crit_by_points(a: dict, b: dict) -> bool:
    # print(a, b)
    if a["points"] < b["points"]:
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


if __name__ == "__main__":
    # create lists

    a_lt = arlt.new_list()
    b_lt = sllt.new_list()
    adc_lt = Arraylist()
    bdc_lt = Singlelinked()

    for i in range(1, 27):
        points = random.randint(13 * i, 42 * (i + 1))
        temp = {"id": i,
                "points": points,
                "name": chr(96 + i)}
        arlt.add_last(a_lt, temp)
        adc_lt.add_last(temp)
        sllt.add_last(b_lt, temp)
        bdc_lt.add_last(temp)

    c_lt = arlt.clone(a_lt)
    d_lt = sllt.clone(b_lt)
    e_lt = arlt.clone(a_lt)
    f_lt = sllt.clone(b_lt)
    cdc_lt = adc_lt.clone()
    ddc_lt = bdc_lt.clone()

    print("before sorting")
    print("functional implementation")

    zipped = zip(arlt.iterator(a_lt),
                 sllt.iterator(b_lt),
                 arlt.iterator(c_lt),
                 sllt.iterator(d_lt))
    for ta, tb, tc, td in zipped:
        print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

    print("dataclass implementation")
    zipped = zip(adc_lt, bdc_lt, cdc_lt, ddc_lt)
    for ta, tb, tc, td in zipped:
        print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

    # a = mgst(a, sort_crit_by_points)
    # b = inst(b, sort_crit_by_points)
    c_lt = qkst(c_lt, sort_crit_by_points)
    d_lt = shst(d_lt, sort_crit_by_points)
    # asc = dcmgst(adc, sort_crit_by_points)
    # bsc = dcinst(bdc, sort_crit_by_points)
    csc_lt = dcsest(cdc_lt, sort_crit_by_points)
    dsc_lt = dcshst(ddc_lt, sort_crit_by_points)

    print("after sorting")
    # print("functional implementation")
    # zipped = zip(arlt.iterator(a_lt),
    #              sllt.iterator(b_lt),
    #              arlt.iterator(c),
    #              sllt.iterator(d))
    # for ta, tb, tc, td in zipped:
    #     print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

    print("dataclass implementation")
    zipped = zip(adc_lt, bdc_lt, cdc_lt, ddc_lt)
    for ta, tb, tc, td in zipped:
        print(f"'a': {ta}, \t'b': {tb}, \t'c': {tc}, \t'd': {td}")

    # print("recursive insertion sort")
    # f_lt = sllt.clone(b_lt)
    # g_lt = sllt.clone(b_lt)
    # f_lt = inst(f_lt, sort_crit_by_points)
    # g_lt = instr(g_lt, sort_crit_by_points)

    # print("after sorting")
    # print("functional implementation")
    # zipped = zip(sllt.iterator(b_lt),
    #              sllt.iterator(f_lt),
    #              sllt.iterator(g_lt))
    # for tb, tf, tg in zipped:
    #     print(f"'b': {tb}, \t'f': {tf}, \t'g': {tg}")
