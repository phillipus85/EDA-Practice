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
