from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
    _size = lst.size(lt)
    if _size > 1:
        mid = int(_size / 2)
        left_lt = lst.sub_list(lt, 0, mid)
        right_lt = lst.sub_list(lt, mid, _size)
        sort(left_lt, sort_crit)
        sort(right_lt, sort_crit)
        lt = _recombine(lt, left_lt, right_lt, sort_crit, lst)
    return lt


def _recombine(lt: dict,
               left_lt: dict,
               right_lt: dict,
               sort_crit: Callable,
               _mod: Callable) -> dict:
    i = 0
    j = 0
    k = 0

    while k < _mod.size(lt):
        if i < _mod.size(left_lt) and j < _mod.size(right_lt):
            e_left = _mod.get_element(left_lt, i)
            e_right = _mod.get_element(right_lt, j)
            if sort_crit(e_left, e_right):
                _mod.update(lt, k, e_left)
                i += 1
            else:
                _mod.update(lt, k, e_right)
                j += 1
        elif i < _mod.size(left_lt):
            e_left = _mod.get_element(left_lt, i)
            _mod.update(lt, k, e_left)
            i += 1
        else:
            e_right = _mod.get_element(right_lt, j)
            _mod.update(lt, k, e_right)
            j += 1
        k += 1
    return lt
