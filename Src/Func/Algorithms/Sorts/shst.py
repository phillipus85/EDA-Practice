"""
*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.

Utiliza el incremento de D. Knuth definido como f(x) = 3x + 1 para calcular el valor de h, con secuencias de incrementos de la forma 1, 4, 13, 40, 121, 364, 1093, 3280, 9841, ...
"""

from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt

    size = lst.size(lt)
    h = 0
    while h < size / 3:
        h = 3 * h + 1
    while h >= 1:
        i = h
        while i < size:
            j = i
            while j >= h and sort_crit(lst.get_element(lt, j),
                                       lst.get_element(lt, j - h)):
                lst.exchange(lt, j, j - h)
                j -= h
            i += 1
        h //= 3
    return lt
