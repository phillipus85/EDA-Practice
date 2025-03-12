from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable

def shell_sort(lt: dict, sort_crit: Callable) -> dict:
    """Ordena una lista (arraylist o linkedlist) utilizando Shell Sort."""
    
    # Determinar la estructura de datos a utilizar
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt
    else:
        raise ValueError("Tipo de lista no soportado")

    size = lst.size(lt)
    gap = size // 2  # Inicializamos el gap a la mitad del tamaño de la lista

    while gap > 0:
        for i in range(gap, size):
            temp = lst.get_element(lt, i)  # Guardamos el elemento actual
            j = i

            # Aplicamos el método de inserción con el gap dado
            while j >= gap and sort_crit(temp, lst.get_element(lt, j - gap)):
                lst.exchange(lt, j, j - gap)
                j -= gap

        gap //= 2  # Reducimos el gap

    return lt  # Devolvemos la lista ordenada

