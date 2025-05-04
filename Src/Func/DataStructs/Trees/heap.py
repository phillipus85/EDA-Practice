"""
Module to handle a heap data structure. to use in priority queues (min or max).

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# import python modules
from typing import Any, Callable

# import modules for data structures ranges in tree
from Src.Func.DataStructs.List import arlt

# import error handler
from Src.Func.Utils.error import error_handler as err


def dflt_heap_elm_cmp(id1: Any, id2: Any) -> int:
    """dflt_heap_elm_cmp is the default comparison function for elements in the array list.

    Args:
        id1 (Any): first element to compare.
        id2 (Any): second element to compare.

    Returns:
        int: returns 1 if id1 > id2, -1 if id1 < id2, 0 if id1 == id2
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0


def new_heap(cmp_function: Callable[[Any, Any], int] = None) -> dict:
    """new_heap crea un nuevo montículo (heap) basado en un arreglo, cuyo primer elemento es el menor elemento del montículo (heap).

    Args:
        cmp_function (Callable[[Any, Any], int]): funcion de comparacion para los elementos del montículo (heap). Por defecto es None, en cuyo caso se utiliza la funcion de comparacion por defecto (dflt_heap_elm_cmp) o la proporcionada por el usuario.

    Returns:
        dict: diccionario que representa el montículo (heap) con los siguientes campos:
            - elements: lista de elementos del montículo (heap).
            - size: tamaño del montículo (heap).
            - cmp_function: funcion de comparacion para los elementos del montículo (heap).
    """
    try:
        _nhp = {
            "elements": None,
            "size": 0,
            "cmp_function": cmp_function
        }
        if cmp_function is None:
            _nhp["cmp_function"] = dflt_heap_elm_cmp

        # create the heap using an array list
        _nhp["elements"] = arlt.new_list(_nhp["cmp_function"])
        return _nhp
    except Exception as exp:
        err("heap", "new_heap()", exp)


def size(hp: dict) -> int:
    """size retorna el número de elementos en el montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).

    Returns:
        int: tamaño del montículo (heap).
    """
    try:
        return hp["size"]
    except Exception as exp:
        err("heap", "size()", exp)


def is_empty(hp: dict) -> bool:
    """is_empty indica si el montículo (heap) está vacío.

    Args:
        hp (dict): diccionario que representa el montículo (heap).

    Returns:
        bool: True si el montículo (heap) está vacío, False en caso contrario.
    """
    try:
        return hp["size"] == 0
    except Exception as exp:
        err("heap", "is_empty()", exp)


def get_min(hp: dict) -> Any:
    """get_min retorna el primer elemento del montículo (heap), es decir el menor elemento.

    Args:
        hp (dict): diccionario que representa el montículo (heap).

    Returns:
        Any: primer elemento del montículo (heap).
    """
    try:
        if is_empty(hp):
            return None
        _elements = hp["elements"]
        _min = arlt.get_element(_elements, 0)
        return _min
    except Exception as exp:
        err("heap", "get_min()", exp)


def insert(hp: dict, elm: Any) -> None:
    """insert inserta un nuevo elemento en el montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        elm (Any): elemento a insertar en el montículo (heap).
    """
    try:
        hp["size"] += 1
        arlt.add_element(hp["elements"], elm, hp["size"] - 1)
        _swim(hp, hp["size"] - 1)
        # return hp
    except Exception as exp:
        err("heap", "insert()", exp)


def delete_min(hp: dict) -> Any:
    """delete_min elimina el menor elemento del montículo (heap) y lo retorna.

    Args:
        hp (dict): diccionario que representa el montículo (heap).

    Returns:
        Any: menor elemento del montículo (heap).
    """
    try:
        if is_empty(hp):
            return None
        _min = arlt.get_element(hp["elements"], 0)
        _last = arlt.get_element(hp["elements"], hp["size"] - 1)
        arlt.update(hp["elements"], 0, _last)
        arlt.update(hp["elements"], hp["size"] - 1, None)
        hp["size"] -= 1
        _sink(hp, 0)
        return _min
    except Exception as exp:
        err("heap", "delete_min()", exp)


def _swim(hp: dict, idx: int) -> None:
    """_swim hace "swim", "sube" o "flota" "bottom-up reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "swim".
    """
    try:
        while idx > 0:
            _parent = arlt.get_element(hp["elements"], idx // 2)
            _element = arlt.get_element(hp["elements"], idx)
            if _greater(hp, _parent, _element):
                _exchange(hp, idx, idx // 2)
            idx = idx // 2
    except Exception as exp:
        err("heap", "_swim()", exp)


def _sink(hp: dict, idx: int) -> None:
    """_sink hace "sink", "baja" o "hundir" "top-down reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "sink".
    """
    try:
        _size = hp["size"]
        while 2 * idx < _size:
            j = 2 * idx
            if j < _size:
                _elm1 = arlt.get_element(hp["elements"], j)
                _elm2 = arlt.get_element(hp["elements"], j + 1)
                if _greater(hp, _elm1, _elm2):
                    j += 1
            _elm1 = arlt.get_element(hp["elements"], idx)
            _elm2 = arlt.get_element(hp["elements"], j)
            if not _greater(hp, _elm1, _elm2):
                break
            _exchange(hp, idx, j)
            idx = j
    except Exception as exp:
        err("heap", "_sink()", exp)


def _greater(hp: dict, elm1: Any, elm2: Any) -> bool:
    """_greater compara dos elementos del montículo (heap) usando la función de comparación.

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        elm1 (Any): primer elemento a comparar.
        elm2 (Any): segundo elemento a comparar.

    Returns:
        bool: True si elm1 > elm2, False en caso contrario.
    """
    try:
        _cmp = hp["cmp_function"]
        if _cmp(elm1, elm2) > 0:
            return True
        return False
    except Exception as exp:
        err("heap", "_greater()", exp)


def _exchange(hp: dict, idx1: int, idx2: int) -> None:
    """_exchange intercambia dos elementos en el montículo (heap).

    Args:
        hp (dict): diccionario que representa el montículo (heap).
        idx1 (int): índice del primer elemento.
        idx2 (int): índice del segundo elemento.
    """
    try:
        arlt.exchange(hp["elements"], idx1, idx2)
    except Exception as exp:
        err("heap", "_exchange()", exp)
