# import python libs
from typing import Any
# import csv
# import project libs
from Src.Func.DataStructs.List import sllt as lt
# import project errors
from Src.Func.Utils.error import error_handler as err


def new_queue(cmp_function=None, key: str = "id") -> dict:
    """new_queue create a new queue

    Args:
        cmp_function (Callable, optional): compara dos elementos. Por defecto es None.
        key (str, optional): llave de los elementos. Por defecto es "id".

    Returns:
        dict: diccionario que representa la cola
    """
    try:
        return lt.new_list(cmp_function, key)
    except Exception as exp:
        err("queue", "new_queue()", exp)


def enqueue(q: dict, elm: Any) -> None:
    """enqueue agrega un elemento al final de la cola

    Args:
        q (dict): diccionario que representa la cola
        elm (Any): elemento a agregar a la cola
    """
    try:
        lt.add_last(q, elm)
    except Exception as exp:
        err("queue", "enqueue()", exp)


def dequeue(q: dict) -> Any:
    """dequeue elimina el elemento al frente de la cola y lo retorna

    Args:
        q (dict): diccionario que representa la cola

    Returns:
        Any: elemento eliminado de la cola
    """
    try:
        return lt.remove_first(q)
    except Exception as exp:
        err("queue", "dequeue()", exp)


def peek(q: dict) -> Any:
    """peek retorna el elemento al frente de la cola sin eliminarlo

    Args:
        q (dict): diccionario que representa la cola

    Returns:
        Any: elemento al frente de la cola
    """
    try:
        return lt.get_first(q)
    except Exception as exp:
        err("queue", "peek()", exp)


def is_empty(q: dict) -> bool:
    """is_empty informa si la cola es vacia o no

    Args:
        q (dict): diccionario que representa la cola

    Returns:
        bool: True si la cola es vacia, False de lo contrario
    """
    try:
        return lt.is_empty(q)
    except Exception as exp:
        err("queue", "is_empty()", exp)


def size(q: dict) -> int:
    """size informa el tamaño de la cola

    Args:
        q (dict): diccionario que representa la cola

    Returns:
        int: tamaño de la cola
    """
    try:
        return lt.size(q)
    except Exception as exp:
        err("queue", "size()", exp)
