from OLD.DISClib.Utils import config as cf

assert cf
from Src.Func.DataStructs.List import arlt as arlt
from Src.Func.DataStructs.List import sllt as slt
from dataclasses import dataclass, field


"""
  Los algoritmos de este libro están basados en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


def sort(lt, sort_criteria: callable) -> list:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = slt
    else:
        raise ValueError("Tipo de lista no soportado")
    
    size = lst.size(lt)
    pos1 = 0
    while pos1 < size:
        minimum = pos1
        pos2 = pos1 + 1
        while pos2 < size:
            if sort_criteria(lst.get_element(lt, pos2), lst.get_element(lt, minimum)):
                minimum = pos2
            pos2 += 1
        lst.exchange(lt, pos1, minimum)
        pos1 += 1
    
    return lt  

