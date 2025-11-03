"""
Module to handle the transversal of a binary search tree (bst) data structure. Includes the in-order, pre-order, and post-order transversal methods.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


# import python modules
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.Trees import bst as te
# from Src.Func.DataStructs.List import queue as qe


def in_order(tree: dict) -> object:
    """in_order recorrido en in-orden de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en in-orden.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    if tree is not None:
        _xvers = _in_order(tree["root"], _xvers)
    return _xvers


def _in_order(node: dict, _xvers: object) -> object:
    """_in_order función recursiva que realiza el recorrido en in-orden de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol. Mantiene el estado del recorrido.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en in-orden.
    """
    if node is None:
        return None
    else:
        _in_order(node["left"], _xvers)
        lt.add_last(_xvers, node["value"])
        _in_order(node["right"], _xvers)
    return _xvers


def in_order_reverse(tree: dict) -> object:
    """in_order_reverse recorrido en in-orden inverso de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en in-orden inverso.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    if tree is not None:
        _xvers = _in_order_reverse(tree["root"], _xvers)
    return _xvers


def _in_order_reverse(node: dict, _xvers: object) -> object:
    """_in_order_reverse función recursiva que realiza el recorrido en in-orden inverso de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol. Mantiene el estado del recorrido.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en in-orden inverso.
    """
    if node is None:
        return None
    else:
        _in_order_reverse(node["right"], _xvers)
        lt.add_last(_xvers, node["value"])
        _in_order_reverse(node["left"], _xvers)
    return _xvers


def pre_order(tree: dict) -> object:
    """pre_order recorrido en pre-orden de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en pre-orden.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    if tree is not None:
        _xvers = _pre_order(tree["root"], _xvers)
    return _xvers


def _pre_order(node: dict, _xvers: object) -> object:
    """_pre_order función recursiva que realiza el recorrido en pre-orden de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol. Mantiene el estado del recorrido.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en pre-orden.
    """
    if node is None:
        return None
    else:
        lt.add_last(_xvers, node["value"])
        _pre_order(node["left"], _xvers)
        _pre_order(node["right"], _xvers)
    return _xvers


def pre_order_reverse(tree: dict) -> object:
    """pre_order_reverse recorrido en pre-orden inverso de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en pre-orden inverso.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    if tree is not None:
        _xvers = _pre_order_reverse(tree["root"], _xvers)
    return _xvers


def _pre_order_reverse(node: dict, _xvers: object) -> object:
    """_pre_order_reverse función recursiva que realiza el recorrido en pre-orden inverso de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol. Mantiene el estado del recorrido.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en pre-orden inverso.
    """
    if node is None:
        return None
    else:
        lt.add_last(_xvers, node["value"])
        _pre_order_reverse(node["right"], _xvers)
        _pre_order_reverse(node["left"], _xvers)
    return _xvers


def post_order(tree: dict) -> object:
    """post_order recorrido en post-orden de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en post-orden.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    if tree is not None:
        _xvers = _post_order(tree["root"], _xvers)
    return _xvers


def _post_order(node: dict, _xvers: object) -> object:
    """_post_order función recursiva que realiza el recorrido en post-orden de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol. Mantiene el estado del recorrido.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en post-orden.
    """
    if node is None:
        return None
    else:
        _post_order(node["left"], _xvers)
        _post_order(node["right"], _xvers)
        lt.add_last(_xvers, node["value"])
    return _xvers


def post_order_reverse(tree: dict) -> object:
    """post_order_reverse recorrido en post-orden inverso de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en post-orden inverso.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    if tree is not None:
        _xvers = _post_order_reverse(tree["root"], _xvers)
    return _xvers


def _post_order_reverse(node: dict, _xvers: object) -> object:
    """_post_order_reverse función recursiva que realiza el recorrido en post-orden inverso de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol. Mantiene el estado del recorrido.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en post-orden inverso.
    """
    if node is None:
        return None
    else:
        lt.add_last(_xvers, node["value"])
        _post_order_reverse(node["right"], _xvers)
        _post_order_reverse(node["left"], _xvers)
    return _xvers


def level_order(tree: dict) -> object:
    """level_order recorrido en nivel de un árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST).

    Returns:
        object: lista encadada (sllt) con los elementos del árbol en nivel.
    """
    _cmp = tree["cmp_func"]
    _xvers = lt.new_list(cmp_function=_cmp)
    # _alt = list()
    if tree is not None:
        _level = 0
        # max lvl = height + 1
        while _level < te.height(tree) + 1:
            _level_order(tree["root"], _xvers, _level)
            _level += 1
    return _xvers


def _level_order(node: dict, _xvers: object, tgt_lvl: int) -> object:
    """_level_order función recursiva que realiza el recorrido en nivel de un árbol binario de búsqueda (BST) y agrega los elementos a una lista encadenada (sllt).

    Args:
        node (dict): nodo actual del árbol binario de búsqueda (BST).
        _xvers (object): lista encadenada (sllt) donde se almacenan los elementos del árbol.
        lvl (int): nivel actual del árbol.

    Returns:
        object: lista encadenada (sllt) con los elementos del árbol en nivel.
    """
    if node is None:
        return _xvers

    if tgt_lvl == 0:
        lt.add_last(_xvers, node["value"])
        # _xvers.append(node["value"])

    else:
        _level_order(node["left"], _xvers, tgt_lvl - 1)
        _level_order(node["right"], _xvers, tgt_lvl - 1)
    return _xvers
