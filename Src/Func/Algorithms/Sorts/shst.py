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

def calculate_knuth_sequence(n):

    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    return gap

def shell_sort(lt, sort_crit):

    lst = get_list_module(lt)
    size = lst.size(lt)
    gap = calculate_knuth_sequence(size)

    while gap >= 1:
        for i in range(gap, size):
            j = i
            while j >= gap and sort_crit(lst.get_element(lt, j), lst.get_element(lt, j - gap)):
                lst.exchange(lt, j, j - gap)
                j -= gap
        gap //= 3

    return lt
