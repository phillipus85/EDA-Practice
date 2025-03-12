from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable

def selection_sort(lt: dict, sort_crit: Callable) -> dict:
    """Ordena una lista (arraylist o linkedlist) utilizando Selection Sort."""
    
    # Determinar la estructura de datos a utilizar
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt
    else:
        raise ValueError("Tipo de lista no soportado")

    size = lst.size(lt)

    for i in range(size - 1):  # Recorremos toda la lista excepto el último elemento
        min_index = i  # Suponemos que el mínimo está en la posición actual
        for j in range(i + 1, size):  # Buscamos el mínimo en el resto de la lista
            if sort_crit(lst.get_element(lt, j), lst.get_element(lt, min_index)):
                min_index = j  # Actualizamos el índice del mínimo encontrado
        
        if min_index != i:
            lst.exchange(lt, i, min_index)  # Intercambiamos los elementos
    
    return lt  # Devolvemos la lista ordenada