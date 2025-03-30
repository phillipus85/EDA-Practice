"""
Module to handle a single linked list nodes (slln) data structure.
This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

_RED = "red"
_BLACK = "black"


def new_bst_node(k: object, v: object, n: int = 1) -> dict:
    """new_bst_node _crea un nuevo nodo para un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        k (object): llave de la pareja
        v (object): valor de la pareja
        n (int, optional): tamaño del subárbol al que pertenece el nodo. Por defecto es 1

    Returns:
        dict: nuevo nodo BST con la pareja llave-valor
    """
    _new_node = dict(
        key=k,
        value=v,
        size=n,
        left=None,
        right=None,
        _type="BST"
    )
    return _new_node


def new_rbt_node(k: object,
                 v: object,
                 n: int,
                 color: str) -> dict:
    """new_rbt_node _summary_

    Args:
        k (object): _description_
        v (object): _description_
        n (int): _description_
        color (str): _description_

    Returns:
        dict: _description_
    """
    _new_node = dict(
        key=k,
        value=v,
        size=n,
        parent=None,
        left=None,
        right=None,
        color=color,
        _type="RBT"
    )
    return _new_node


def is_red(node: dict) -> bool:
    """is_red _summary_

    Args:
        node (dict): _description_

    Returns:
        bool: _description_
    """
    return node.get("color") == _RED


def get_value(node: dict) -> object:
    """get_value _summary_

    Args:
        node (dict): _description_

    Returns:
        object: _description_
    """
    if node is not None:
        return node.get("value")
    return node


def set_value(node: dict, value: object) -> None:
    """set_value _summary_

    Args:
        node (dict): _description_
        value (object): _description_

    Returns:
        _type_: _description_
    """
    if node is not None:
        node["value"] = value
    return node


def get_key(node: dict) -> object:
    """get_key _summary_

    Args:
        node (dict): _description_

    Returns:
        object: _description_
    """
    if node is not None:
        return node.get("key")
    return node


def set_key(node: dict, key: object) -> None:
    """set_key _summary_

    Args:
        node (dict): _description_
        key (object): _description_

    Returns:
        _type_: _description_
    """
    if node is not None:
        node["key"] = key
    return node
