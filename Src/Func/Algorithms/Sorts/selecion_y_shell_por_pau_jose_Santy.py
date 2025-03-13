"""
1. Santiago Pinilla Perez, s.pinillap2@uniandes.edu.co , 202315246.
2. Pau Suso Otoya, p.suso@uniandes.edu.co, 202421032.
3. Jose Daniel Largo Santanilla, j.largos@unaindes.edu.co, 202420549.
"""

from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def selection_sort(lt: dict, sort_crit: Callable):
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt

    if not lt or lst.size(lt) <= 1:
        return lt

    size = lst.size(lt)

    for i in range(size):
        menor = i
        for j in range(i + 1, size):
            if sort_crit(lst.get_element(lt, j), lst.get_element(lt, menor)):
                menor = j
        lst.exchange(lt, i, menor)

    return lt

def shell_sort(lt: dict, sort_crit: Callable):
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
        
    if not lt or lst.size(lt) <= 1:
        return lt

    size = lst.size(lt)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            temp = lst.get_element(lt, i)
            j = i
            while j >= gap and sort_crit(temp, lst.get_element(lt, j - gap)):
                lst.exchange(lt, j, j - gap)
                j -= gap
        gap //= 2

    return lt

