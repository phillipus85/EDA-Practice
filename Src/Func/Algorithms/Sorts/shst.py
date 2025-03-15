from OLD.DISClib.Utils import config as cf

assert cf
from Src.Func.DataStructs.List import arlt as arlt
from Src.Func.DataStructs.List import sllt as slt
from dataclasses import dataclass, field

"""
Implementación del algoritmo shellsort, basado en
la propuesta de Robert Sedgewick

Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne

Se utiliza la secuencia de incrementos 3x+1: 1, 4, 13, 40, 121, 364, 1093,
(D. Knuth)
Sedgewick: 1,5,19,41,109,209,929,2161,...
"""


def sort(lt, sort_crit):
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = slt
    else:
        raise ValueError("Tipo de lista no soportado")
    
    n = lst.size(lt)
    h = 1
    while h < n/3:
        h = 3*h + 1
        
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(
                lst.get_element(lt, j),
                lst.get_element(lt, j-h)):
                lst.exchange(lt, j, j-h)
                j -= h
        h //= 3
        
    return lt  

