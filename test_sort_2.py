# import python modules
# from typing import Callable
import random

# functional style structure import
from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt


# import functional programing sorting algorithms
from Src.Func.Algorithms.Sorts.mgst import sort as mgst
from Src.Func.Algorithms.Sorts.inst import sort as inst

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

    for i in range(1, 27):
        points = random.randint(13 * i, 42 * (i + 1))
        temp = {"id": i,
                "points": points,
                "name": chr(96 + i)}
        arlt.add_last(a_lt, temp)
        sllt.add_last(b_lt, temp)

    print("=== BEFORE SORTING ===")
    print("Iterating functional implementation:\n")
    zipped = zip(arlt.iterator(a_lt),
                 sllt.iterator(b_lt))
    for ta, tb in zipped:
        print(f"\t'a': {ta}, \t'b': {tb}")

    # copy/clone lists
    c_lt = arlt.clone(a_lt)
    d_lt = sllt.clone(b_lt)

    # sort lists
    c_lt = mgst(c_lt, sort_crit_by_points)
    d_lt = inst(d_lt, sort_crit_by_points)

    print("\n=== AFTER SORTING ===")
    print("Iterating functional implementation:\n")
    zipped = zip(arlt.iterator(c_lt),
                 sllt.iterator(d_lt))
    for tc, td in zipped:
        print(f"\t'c': {tc}, \t'd': {td}")

    # recursive insertion sort
    e_lt = arlt.clone(a_lt)
    f_lt = sllt.clone(b_lt)
    e_lt = inst(e_lt, sort_crit_by_points)
    f_lt = instr(f_lt, sort_crit_by_points)
    print("\n=== AFTER SORTING (recursive) ===")
    print("Iterating functional implementation:\n")
    zipped = zip(arlt.iterator(a_lt),
                 arlt.iterator(e_lt),
                 sllt.iterator(f_lt))
    for ta, te, tf in zipped:
        print(f"\t'a': {ta}, \t'e': {te}, \t'f': {tf}")
