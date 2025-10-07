from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable, Any


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt

    size = lst.size(lt)
    i = 0
    while i < size:
        j = i
        while j > 0 and sort_crit(lst.get_element(lt, j),
                                  lst.get_element(lt, j - 1)):
            lst.exchange(lt, j, j - 1)
            j -= 1
        i += 1
    return lt


def sort2(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt

    size = lst.size(lt)
    i = 0
    while i < size:
        j = i
        _sorted = False
        while j > 0 and not _sorted:
            if sort_crit(lst.get_element(lt, j),
                         lst.get_element(lt, j - 1)):
                lst.exchange(lt, j, j - 1)
            else:
                _sorted = True
            j -= 1
        i += 1
    return lt


def sort_r(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        mod = arlt
    elif lt["type"] == "SINGLELINKED":
        mod = sllt

    size = mod.size(lt)

    lt = _sort_r(lt, mod, sort_crit, 0, size)
    return lt


def _sort_r(lt: dict,
            module: Any,
            sort_crit: Callable,
            idx: int,
            jdx: int) -> dict:
    if idx < module.size(lt):
        j = idx
        if j > 0 and sort_crit(module.get_element(lt, j),
                               module.get_element(lt, j - 1)):
            module.exchange(lt, j, j - 1)
            j -= 1
            lt = _sort_r(lt, module, sort_crit, idx, jdx - 1)
        lt = _sort_r(lt, module, sort_crit, idx + 1, jdx)

    return lt
