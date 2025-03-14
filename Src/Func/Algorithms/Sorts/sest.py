from OLD.DISClib.Utils import config as cf
assert cf

from Src.Func.DataStructs.List import arlt as arlt
from Src.Func.DataStructs.List import sllt as slt

def get_list_module(lt):

    if lt["type"] == "ARRAYLIST":
        return arlt
    elif lt["type"] == "SINGLELINKED":
        return slt
    else:
        raise ValueError("Tipo de lista no soportado")

def selection_sort(lt, sort_criteria: callable) -> list:

    lst = get_list_module(lt)
    size = lst.size(lt)

    for start in range(size - 1):
        min_element = start
        for current in range(start + 1, size):
            if sort_criteria(lst.get_element(lt, current), lst.get_element(lt, min_element)):
                min_element = current

        if min_element != start:
            lst.exchange(lt, start, min_element)

    return lt
