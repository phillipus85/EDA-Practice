from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
    _size = lst.size(lt)
    # print(f"size: {size}")
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

    # if size < 2:
    #     return lt

    # mid = size // 2
    # _left_lt = lst.sub_list(lt, 0, mid - 1)
    # _right_lt = lst.sub_list(lt, mid, size - 1)
    # # print(f"- left: {_left_lt},\n- right: {_right_lt}")
    # sort(_left_lt, sort_crit)
    # sort(_right_lt, sort_crit)
    # i = j = k = 0

    # _n_left = lst.size(_left_lt)
    # _n_right = lst.size(_right_lt)
    # print(f"n_left: {_n_left}, n_right: {_n_right}")
    # while (i < _n_left) and (j < _n_right):
    #     elm_i = lst.get_element(_left_lt, i)
    #     elm_j = lst.get_element(_right_lt, j)
    #     print(f"elm_i: {elm_i}, elm_j: {elm_j}")
    #     print(sort_crit(elm_i, elm_j))
    #     if sort_crit(elm_i, elm_j):
    #         lst.update(lt, k, elm_i)
    #         i += 1
    #     else:
    #         lst.update(lt, k, elm_j)
    #         j += 1
    #     k += 1

    # while i < _n_left:
    #     print(f"i: {i}, j: {j}, k: {k}")
    #     elm_i = lst.get_element(_left_lt, i)
    #     print(f"elm_i: {elm_i}")
    #     lst.update(lt, k, elm_i)
    #     # lst.update(lt, k, lst.get_element(_left_lt, i))
    #     i += 1
    #     k += 1

    # while j < _n_right:
    #     print(f"i: {i}, j: {j}, k: {k}")
    #     elm_j = lst.get_element(_right_lt, j)
    #     print(f"elm_j: {elm_j}")
    #     lst.update(lt, k, elm_j)
    #     # lst.update(lt, k, lst.get_element(_right_lt, j))
    #     j += 1
    #     k += 1
    # # print(f"i: {i}, j: {j}, k: {k}")
    # # print(lt)
    # return lt
