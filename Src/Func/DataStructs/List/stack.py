# import python libs
from typing import Any
# import csv
# import project libs
from Src.Func.DataStructs.List import dllt as lt
# import project errors
from Src.Func.Utils.error import error_handler as err


def new_stack(cmp_function=None, key: str = "id") -> dict:
    """new_stack create a new stack

    Args:
        cmp_function (Callable, optional): compara dos elementos. Por defecto es None.
        key (str, optional): llave de los elementos. Por defecto es "id".

    Returns:
        dict: diccionario que representa la pila
    """
    try:
        return lt.new_list(cmp_function, key)
    except Exception as exp:
        err("stack", "new_stack()", exp)


def push(stk: dict, elm: Any) -> None:
    """push agrega un elemento a la pila

    Args:
        stk (dict): diccionario que representa la pila
        elm (Any): elemento a agregar a la pila
    """
    try:
        lt.add_first(stk, elm)
    except Exception as exp:
        err("stack", "push()", exp)


def pop(stk: dict) -> Any:
    """pop elimina el elemento al tope de la pila y lo retorna

    Args:
        stk (dict): diccionario que representa la pila

    Returns:
        Any: elemento eliminado de la pila
    """
    try:
        return lt.remove_first(stk)
    except Exception as exp:
        err("stack", "pop()", exp)


def top(stk: dict) -> Any:
    """top retorna el elemento al tope de la pila sin eliminarlo

    Args:
        stk (dict): diccionario que representa la pila

    Returns:
        Any: elemento al tope de la pila
    """
    try:
        return lt.get_first(stk)
    except Exception as exp:
        err("stack", "top()", exp)


def is_empty(stk: dict) -> bool:
    """is_empty verifica si la pila es vacia

    Args:
        stk (dict): diccionario que representa la pila

    Returns:
        bool: True si la pila es vacia, False de lo contrario
    """
    try:
        return lt.is_empty(stk)
    except Exception as exp:
        err("stack", "is_empty()", exp)


def size(stk: dict) -> int:
    """size retorna el tamaño de la pila

    Args:
        stk (dict): diccionario que representa la pila

    Returns:
        int: tamaño de la pila
    """
    try:
        return lt.size(stk)
    except Exception as exp:
        err("stack", "size()", exp)
