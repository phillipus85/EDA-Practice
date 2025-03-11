from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
    size = lst.size(lt)
    if size > 0:
        mid = (size // 2)
        _left_lt = lst.sub_list(lt, 0, mid)
        _right_lt = lst.sub_list(lt, mid + 1, size - 1)
        sort(_left_lt, sort_crit)
        sort(_right_lt, sort_crit)
        i = j = k = 0

        _n_left = lst.size(_left_lt)
        _n_right = lst.size(_right_lt)

        while (i < _n_left) and (j < _n_right):
            elemi = lst.get_element(_left_lt, i)
            elemj = lst.get_element(_right_lt, j)
            if sort_crit(elemj, elemi):
                lst.update(lt, k, elemj)
                j += 1
            else:
                lst.update(lt, k, elemi)
                i += 1
            k += 1

        while i < _n_left:
            lst.update(lt, k, lst.get_element(_left_lt, i))
            i += 1
            k += 1

        while j < _n_right:
            lst.update(lt, k, lst.get_element(_right_lt, j))
            j += 1
            k += 1
    return lt
