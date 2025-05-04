"""
Module to handle a heap data structure. to use in priority queues (min or max).

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# import python modules
from typing import Any, Callable

# import modules for data structures ranges in tree
from Src.Func.DataStructs.List import arlt as lt
from Src.Func.DataStructs.Tables import lpht as mp

# import error handler
from Src.Func.Utils.error import error_handler as err


def new_heap(cmp_function: Callable = None) -> dict:
    """new_heap crea un nuevo montículo (heap) basado en un arreglo y un mapa de dispersión lineal (linear probing hash table), util para busquedas de elementos en algoritmos como Dijkstra o Prim.

    Args:
        cmp_function (Callable, optional): funcion de comparacion para los elementos del montículo (heap). Por defecto es None, en cuyo caso se utiliza la funcion de comparacion del ArrayList

    Returns:
        dict: diccionario que representa el montículo (heap) con los siguientes campos:
            - elements: lista de elementos del montículo (heap).
            - pqmap: mapa de dispersión lineal (linear probing hash table) para busquedas de elementos.
            - size: tamaño del montículo (heap).
            - cmp_function: funcion de comparacion para los elementos del montículo (heap).
    """
    try:

        _nihp = {
            "elements": None,
            "pqmap": None,
            "size": 0,
            "cmp_function": cmp_function
        }

        _nihp["elements"] = lt.new_list(_nihp["cmp_function"])
        _nihp["pqmap"] = mp.new_mp(_nihp["cmp_function"])

        return _nihp
    except Exception as exp:
        err("Idx Heap", "new_heap", exp)


def size(ihp: dict) -> int:
    """size retorna el tamaño del montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).

    Returns:
        int: tamaño del montículo (heap).
    """
    try:
        return ihp["size"]
    except Exception as exp:
        err("Idx Heap", "size", exp)


def is_empty(ihp: dict) -> bool:
    """is_empty verifica si el montículo (heap) está vacío.

    Args:
        ihp (dict): diccionario que representa el montículo (heap).

    Returns:
        bool: True si el montículo (heap) está vacío, False en caso contrario.
    """
    try:
        return ihp["size"] == 0
    except Exception as exp:
        err("Idx Heap", "is_empty", exp)


def contains(ihp: dict, key: Any) -> bool:
    """contains verifica si el montículo (heap) contiene un elemento.

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        key (Any): elemento a verificar.

    Returns:
        bool: True si el elemento está en el montículo (heap), False en caso contrario.
    """
    try:
        return mp.contains(ihp["pqmap"], key)
    except Exception as exp:
        err("Idx Heap", "contains", exp)


def get_min(ihp: dict) -> Any:
    """get_min retorna el elemento mínimo del montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).

    Returns:
        Any: elemento mínimo del montículo (heap).
    """
    try:
        if ihp["size"] > 0:
            return lt.get_element(ihp["elements"], 0)["key"]
        return None
    except Exception as exp:
        err("Idx Heap", "get_min", exp)
        

def del_min(ihp: dict) -> Any:
    """del_min elimina el elemento mínimo del montículo (heap) y lo retorna.

    Args:
        ihp (dict): diccionario que representa el montículo (heap).

    Returns:
        Any: elemento mínimo eliminado del montículo (heap).
    """
    try:
        if ihp["size"] > 0:
            _min = lt.get_element(ihp["elements"], 0)["key"]
            _exchange(ihp, 0, ihp["size"] - 1)
            ihp["size"] -= 1
            _sink(ihp, 0)
            lt.remove_element(ihp["elements"], ihp["size"])
            mp.remove(ihp["pqmap"], _min)
            return _min
        return None
    except Exception as exp:
        err("Idx Heap", "del_min", exp)


def decrease_key(ihp: dict, key: Any, nidx: int) -> None:
    """decrease_key disminuye la clave de un elemento en el montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        key (Any): elemento a disminuir la clave.
        nidx (int): nuevo índice del elemento.

    Raises:
        Exception: si el elemento no está en el montículo (heap).
    """
    try:
        val = mp.get(ihp["pqmap"], key)
        if val is not None:
            elm = lt.get_element(ihp["elements"], val["value"])
            elm["idx"] = nidx
            lt.update(ihp["elements"], val["value"], elm)
            _swim(ihp, val["value"])
    except Exception as exp:
        err("Idx Heap", "decrease_key", exp)


def increase_key(ihp: dict, key: Any, nidx: int) -> None:
    """increase_key aumenta la clave de un elemento en el montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        key (Any): elemento a aumentar la clave.
        nidx (int): nuevo índice del elemento.

    Raises:
        Exception: si el elemento no está en el montículo (heap).
    """
    try:
        val = mp.get(ihp["pqmap"], key)
        if val is not None:
            elm = lt.get_element(ihp["elements"], val["value"])
            elm["idx"] = nidx
            lt.update(ihp["elements"], val["value"], elm)
            _sink(ihp, val["value"]) 
    except Exception as exp:
        err("Idx Heap", "increase_key", exp)


def insert(ihp: dict, key: Any, idx: int) -> None:
    """insert _summary_

    Args:
        ihp (dict): _description_
        key (Any): _description_
        idx (int): _description_
    """
    try:
        if not mp.contains(ihp["pqmap"], key):
            ihp["size"] += 1
            lt.add_element(ihp["elements"],
                           ihp["size"] - 1,
                           {"key": key, "idx": idx})
            mp.put(ihp["pqmap"], key, ihp["size"] - 1)
        _swim(ihp, ihp["size"] - 1)
    except Exception as exp:
        err("Idx Heap", "insert", exp)


#  ---------------------------------------------------------
#   Funciones Helper
#  ---------------------------------------------------------


def _swim(ihp: dict, idx: int) -> None:
    """_swim hace "swim", "sube" o "flota" "bottom-up reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "swim".
    """
    try:
        while idx > 0:
            _parent = lt.get_element(ihp["elements"], idx // 2)
            _element = lt.get_element(ihp["elements"], idx)
            if _greater(ihp, _parent, _element):
                _exchange(ihp, idx, idx // 2)
            idx = idx // 2
    except Exception as exp:
        err("heap", "_swim()", exp)


def _sink(ihp: dict, idx: int) -> None:
    """_sink hace "sink", "baja" o "hundir" "top-down reheapfy" el elemento en la posición idx del montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        idx (int): índice del elemento a hacer "sink".
    """
    try:
        _size = ihp["size"]
        while 2 * idx < _size:
            j = 2 * idx
            if j < _size:
                _elm1 = lt.get_element(ihp["elements"], j)
                _elm2 = lt.get_element(ihp["elements"], j + 1)
                if _greater(ihp, _elm1, _elm2):
                    j += 1
            _elm1 = lt.get_element(ihp["elements"], idx)
            _elm2 = lt.get_element(ihp["elements"], j)
            if not _greater(ihp, _elm1, _elm2):
                break
            _exchange(ihp, idx, j)
            idx = j
    except Exception as exp:
        err("heap", "_sink()", exp)


def _greater(ihp: dict, elm1: Any, elm2: Any) -> bool:
    """_greater compara dos elementos del montículo (heap) usando la función de comparación.

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        elm1 (Any): primer elemento a comparar.
        elm2 (Any): segundo elemento a comparar.

    Returns:
        bool: True si elm1 > elm2, False en caso contrario.
    """
    try:
        # _cmp = ihp["cmp_function"]
        # if _cmp(elm1, elm2) > 0:
        #     return True
        return elm1["idx"] > elm2["idx"]
    except Exception as exp:
        err("heap", "_greater()", exp)


def _exchange(ihp: dict, idx1: int, idx2: int) -> None:
    """_exchange intercambia dos elementos en el montículo (heap).

    Args:
        ihp (dict): diccionario que representa el montículo (heap).
        idx1 (int): índice del primer elemento.
        idx2 (int): índice del segundo elemento.
    """
    try:
        elm1 = lt.get_element(ihp["elements"], idx1)
        elm2 = lt.get_element(ihp["elements"], idx2)
        lt.update(ihp["elements"], idx1, elm2)
        lt.update(ihp["elements"], idx2, elm1)
        mp.put(ihp["pqmap"], elm1["key"], idx2)
        mp.put(ihp["pqmap"], elm2["key"], idx1)
    except Exception as exp:
        err("heap", "_exchange()", exp)
