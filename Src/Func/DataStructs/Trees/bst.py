"""
Module to handle a binary search tree (bst) data structure.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# import python modules
from typing import Any

# import modules for data structures ranges in tree
from Src.Func.DataStructs.List import sllt

# import error handler
from Src.Func.Utils.error import error_handler as err

# import map entry
from Src.Func.DataStructs.Trees import trnode as trn


def dflt_tree_node_cmp(key1, key2):
    """dflt_tree_node_cmp 

    Args:
        key1 (_type_): _description_
        key2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


def new_tree(cmp_func=dflt_tree_node_cmp) -> dict:
    """new_tree _crea un nuevo árbol binario de búsqueda (BST) y lo retorna.

    Args:
        cmp_func (function, optional): _description_. Defaults to dflt_tree_node_cmp.

    Returns:
        dict: _description_
    """
    try:
        _new_bst = dict(
            root=None,
            size=0,
            cmp_func=cmp_func,
            _type="BST"
        )
        return _new_bst
    except Exception as exp:
        err("bst", "new_tree()", exp)


def insert(tree: dict, k: Any, v: Any) -> dict:
    """insert _summary_

    Args:
        tree (dict): _description_
        k (Any): _description_
        v (Any): _description_

    Returns:
        dict: _description_
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        _root = _insert(_root, k, v, _cmp)
        tree["root"] = _root
    except Exception as exp:
        err("bst", "insert()", exp)


def _insert(node: dict, k: Any, v: Any, cmp_func) -> dict:
    try:
        # caso base, el arbol esta vacio
        if node is None:
            node = trn.new_bst_node(k, v, 1)
        # caso base, el arbol no esta vacio
        else:
            _cmp = cmp_func(k, node["key"])
            # si la llave es menor, insertar en el subarbol izquierdo
            if _cmp < 0:
                node["left"] = _insert(node["left"],
                                       k,
                                       v,
                                       cmp_func)
            # si la llave es mayor, insertar en el subarbol derecho
            elif _cmp > 0:
                node["right"] = _insert(node["right"],
                                        k,
                                        v,
                                        cmp_func)
            # si la llave es igual, actualizar el valor
            else:
                node["value"] = v
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        # actualizar el tamaño del nodo
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("bst", "_insert()", exp)


def get(tree: dict, k: Any) -> dict:
    """get _summary_

    Args:
        tree (dict): _description_
        k (Any): _description_

    Returns:
        dict: _description_
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _get(_root, k, _cmp)
    except Exception as exp:
        err("bst", "get()", exp)


def _get(node: dict, k: Any, cmp_func) -> dict:
    """_get _summary_

    Args:
        node (dict): _description_
        k (Any): _description_
        cmp_func (_type_): _description_

    Returns:
        dict: _description_
    """
    try:
        # caso base, el arbol esta vacio
        _node = None
        # caso base, el arbol no esta vacio
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si el nodo es igual a la llave, retornar el nodo
            if _cmp == 0:
                _node = node
            # si el nodo es menor que la llave, buscar en el subarbol izquierdo
            elif _cmp < 0:
                _node = _get(node["left"], k, cmp_func)
            # si el nodo es mayor que la llave, buscar en el subarbol derecho
            elif _cmp > 0:
                _node = _get(node["right"], k, cmp_func)
        return _node
    except Exception as exp:
        err("bst", "_get()", exp)


def remove(tree: dict, k: Any) -> dict:
    """remove _summary_

    Args:
        tree (dict): _description_
        k (Any): _description_

    Returns:
        dict: _description_
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _remove(_root, k, _cmp)
    except Exception as exp:
        err("bst", "remove()", exp)


def _remove(node: dict, k: Any, cmp_func) -> dict:
    try:
        # caso base, el arbol esta vacio\
        if node is None:
            return None
        # caso base, el arbol no esta vacio
        elif node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es igual
            if _cmp == 0:
                # caso 1, el nodo no tiene hijo derecho
                if node["right"] is None:
                    return node["left"]
                # caso 2, el nodo no tiene hijo izquierdo
                elif node["left"] is None:
                    return node["right"]
                # caso 3, el nodo tiene ambos hijos
                else:
                    _node = node
                    # encontrar el nodo minimo del subarbol derecho
                    node = _min(node["right"])
                    # reemplazar el nodo por el nodo minimo
                    node["right"] = _delete_min(_node["right"])
                    node["left"] = _node["left"]
            # si la llave es menor, buscar en el subarbol izquierdo
            elif _cmp < 0:
                node["left"] = _remove(node["left"], k, cmp_func)
            # si la llave es mayor, buscar en el subarbol derecho
            elif _cmp > 0:
                node["right"] = _remove(node["right"], k, cmp_func)
        # actualizar el tamaño del nodo
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("bst", "_remove()", exp)


def contains(tree: dict, k: Any) -> bool:
    """contains _summary_

    Args:
        tree (dict): _description_
        k (Any): _description_

    Returns:
        bool: _description_
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _contains(_root, k, _cmp)
    except Exception as exp:
        err("bst", "contains()", exp)


def _contains(node: dict, k: Any, cmp_func) -> bool:
    pass


def size(tree: dict) -> int:
    """size _summary_

    Args:
        tree (dict): _description_

    Returns:
        int: _description_
    """
    try:
        return tree["size"]
    except Exception as exp:
        err("bst", "size()", exp)


def _size(node: dict) -> int:
    """_size _summary_

    Args:
        node (dict): _description_

    Returns:
        int: _description_
    """
    if node is None:
        return 0
    return node["size"]


def is_empty(tree: dict) -> bool:
    """is_empty _summary_

    Args:
        tree (dict): _description_

    Returns:
        bool: _description_
    """
    try:
        return tree["size"] == 0
    except Exception as exp:
        err("bst", "is_empty()", exp)


def min(tree: dict) -> dict:
    """min _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        return _min(tree["root"])
    except Exception as exp:
        err("bst", "min()", exp)


def _min(node: dict) -> dict:
    pass


def delete_min(tree: dict) -> dict:
    """delete_min _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        return _delete_min(tree["root"])
    except Exception as exp:
        err("bst", "delete_min()", exp)


def _delete_min(node: dict) -> dict:
    try:
        pass
    except Exception as exp:
        err("bst", "_delete_min()", exp)


def max(tree: dict) -> dict:
    """max _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        return _max(tree["root"])
    except Exception as exp:
        err("bst", "max()", exp)


def _max(node: dict) -> dict:
    pass


def delete_max(tree: dict) -> dict:
    """delete_max _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        return _delete_max(tree["root"])
    except Exception as exp:
        err("bst", "delete_max()", exp)


def _delete_max(node: dict) -> dict:
    try:
        pass
    except Exception as exp:
        err("bst", "_delete_max()", exp)


def height(tree: dict) -> int:
    """height _summary_

    Args:
        tree (dict): _description_

    Returns:
        int: _description_
    """
    try:
        return _height(tree["root"])
    except Exception as exp:
        err("bst", "height()", exp)


def _height(node: dict) -> int:
    pass


def keys(tree: dict) -> dict:
    """keys _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        keys_lt = sllt.new_list(cmp_function=tree["cmp_func"],
                                key=tree["key"])
        _keys(tree["root"], keys_lt)
        return keys_lt
    except Exception as exp:
        err("bst", "keys()", exp)


def _keys(node: dict, keys_lt: dict) -> None:
    pass


def values(tree: dict) -> dict:
    """values _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        values_lt = sllt.new_list(cmp_function=tree["cmp_func"],
                                  key=tree["key"])
        _values(tree["root"], values_lt)
        return values_lt
    except Exception as exp:
        err("bst", "values()", exp)


def _values(node: dict, values_lt: dict) -> None:
    pass
