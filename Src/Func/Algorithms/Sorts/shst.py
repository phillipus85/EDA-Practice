from DataStructs.List import arlt
from DataStructs.List import sllt
from typing import Callable


def shell_sort(lt, sort_crit):
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
        
    n = lst.size(lt)
    h = 1
    while h < n/3:
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(lst.get_element(lt, j),
                                        lst.get_element(lt, j-h)):
                lst.exchange(lt, j, j-h)
                j -= h
        h //= 3
    return lt 