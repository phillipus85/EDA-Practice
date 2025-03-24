from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt

    size = lst.size(lt)
    i = 0
    while i < size:
        _min = i
        j = i + 1
        while j < size:
            if sort_crit(lst.get_element(lt, j),
                         lst.get_element(lt, _min)):
                _min = j
            j += 1
        lst.exchange(lt, i, _min)
        i += 1
    return lt
