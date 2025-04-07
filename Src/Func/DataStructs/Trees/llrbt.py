"""
Module to handle a binary search tree (bst) data structure.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# import python modules
from typing import Any, Callable

# import modules for data structures ranges in tree
from Src.Func.DataStructs.List import sllt

# import error handler
from Src.Func.Utils.error import error_handler as err

# import map entry
from Src.Func.DataStructs.Trees import trnode as trn


def dflt_tree_node_cmp(key1: Any, key2: Any) -> int:
    """dflt_tree_node_cmp funcion de comparacion por defecto para los nodos de un árbol binario balanceado hacia la izquierda (LLRBT).

    Args:
        key1 (Any): primera llave a comparar
        key2 (Any): segunda llave a comparar

    Returns:
        int: -1 si key1 < key2, 0 si key1 == key2, 1 si key1 > key2
    """
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


def new_tree(cmp_func=dflt_tree_node_cmp) -> dict:
    """new_tree crea un nuevo árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        cmp_func (function, optional): funcion de comparacion para los elementos del árbol. Por defecto es dflt_tree_node_cmp

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) con sus propiedades
    """
    try:
        # definir el árbol binario balanceado hacia la izquierda (LLRBT)
        # y sus propiedades
        # root: nodo raiz del árbol
        # size: tamaño del árbol
        # cmp_func: funcion de comparacion para los elementos del árbol
        # _type: tipo de árbol (BST o LLRBT)
        _new_bst = dict(
            root=None,
            size=0,
            cmp_func=cmp_func,
            _type="LLRBT"
        )
        if _new_bst["cmp_func"] is None:
            _new_bst["cmp_func"] = dflt_tree_node_cmp
        # retorna el árbol binario balanceado hacia la izquierda (LLRBT)
        return _new_bst
    except Exception as exp:
        err("llrbt", "new_tree()", exp)


def insert(tree: dict, k: Any, v: Any) -> dict:
    """insert aggrega un nuevo nodo al árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave del nodo a agregar
        v (Any): valor del nodo a agregar

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        # configurando los parametros para la funcion recursiva
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        # invocando la funcion recursiva para agregar el nodo al árbol
        _root = _insert(_root, k, v, _cmp)
        # actualizando la raiz del árbol
        tree["root"]["color"] = trn.BLACK
        tree["root"] = _root
    except Exception as exp:
        err("llrbt", "insert()", exp)


def _insert(node: dict, k: Any, v: Any, cmp_func: Callable) -> dict:
    """_insert funcion recursiva que agrega un nuevo nodo al árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a agregar
        v (Any): valor del nodo a agregar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        # caso base, el arbol esta vacio
        if node is None:
            node = trn.new_rbt_node(k, v, 1, trn.RED)
        # caso base, el arbol no esta vacio
        else:
            _cmp = cmp_func(k, node["key"])
            # si la llave es menor, insertar en el subarbol izquierdo
            if _cmp < 0:
                node["left"] = _insert(node["left"], k, v, cmp_func)
            # si la llave es mayor, insertar en el subarbol derecho
            elif _cmp > 0:
                node["right"] = _insert(node["right"], k, v, cmp_func)

            # si la llave es igual, actualizar el valor
            else:
                node["value"] = v

            # despues de insertar el nodo, verificar si el arbol esta balanceado
            # caso base, si el hijo derecho es rojo y el izquierdo no
            if _is_red(node["right"]) and not _is_red(node["left"]):
                # rotar a la izquierda
                node = _rotate_left(node)
            # caso base, si el hijo y nieto izquierdo son rojos
            if _is_red(node["left"]) and _is_red(node["left"]["left"]):
                # rotar a la derecha
                node = _rotate_right(node)
            # caso base, si el hijo izquierdo y derecho son rojos
            if _is_red(node["left"]) and _is_red(node["right"]):
                # invertir colores
                _flip_colors_node(node)
        # actualizar el tamaño del nodo
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("llrbt", "_insert()", exp)


def get(tree: dict, k: Any) -> dict:
    """get recupera un nodo del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave del nodo a recuperar

    Returns:
        dict: diccionario con el nodo recuperado
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _get(_root, k, _cmp)
    except Exception as exp:
        err("llrbt", "get()", exp)


def _get(node: dict, k: Any, cmp_func: Callable) -> dict:
    """_get funcion recursiva que recupera un nodo del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a recuperar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario con el nodo recuperado
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
        err("llrbt", "_get()", exp)


def remove(tree: dict, k: Any) -> dict:
    """remove elimina un nodo del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el nodo a eliminar.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave del nodo a eliminar

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        # caso base, si el hijo izquierdo y derecho NO son rojos
        if not _is_red(_root["left"]) and not _is_red(_root["right"]):
            # cambiar el color del padre a rojo
            _root["color"] = trn.RED
        # invocando la funcion recursiva para eliminar el nodo del árbol
        tree["root"] = _remove(_root, k, _cmp)
        # actualizando el color de la raiz
        if not is_empty(tree):
            tree["root"]["color"] = trn.BLACK
        return tree
    except Exception as exp:
        err("llrbt", "remove()", exp)


def _remove(node: dict, k: Any, cmp_func: Callable) -> dict:
    """_remove funcion recursiva que elimina un nodo del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el nodo a eliminar.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a eliminar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        # caso base, si el nodo es menor que la llave
        _cmp = cmp_func(k, node["key"])
        if _cmp < 0:
            # caso base, el hijo izq y su susesor izq no son rojos
            if not _is_red(node["left"]) and not _is_red(node["left"]["left"]):
                # invertir colores a la izquierda
                node = _move_red_left(node)
            # de lo contrario, buscar en el subarbol izquierdo
            node["left"] = _remove(node["left"], k, cmp_func)
        # caso base, el nodo es igual a la llave
        else:
            # caso base, si el nodo izquierdo es rojo
            if _is_red(node["left"]):
                # rotar a la derecha
                node = _rotate_right(node)
            # caso base, si el nodo es igual a la llave y no hay un nodo derecho
            if _cmp == 0 and node["right"] is None:
                # eliminar el nodo
                return None
            # caso base, si el hijo der no es rojo y su suzesor izq no es rojo
            if not _is_red(node["right"]) and not _is_red(node["right"]["left"]):
                # invertir colores a la derecha
                node = _move_red_right(node)
            # caso base, si el nodo es igual a la llave y el hijo der es None
            if _cmp == 0:
                # eliminar el nodo
                # buscar el sucesor
                _node = _min(node["right"])
                # asignar la llave y el valor del sucesor al nodo actual
                node["key"] = _node["key"]
                node["value"] = _node["value"]
                # eliminar el sucesor
                node["right"] = _delete_min(node["right"])
            else:
                # buscar en el subarbol derecho
                node["right"] = _remove(node["right"], k, cmp_func)
        # balancear el árbol
        node = _balance(node)
        return node
    except Exception as exp:
        err("llrbt", "_remove()", exp)


def contains(tree: dict, k: Any) -> bool:
    """contains revisa si un nodo existe en el árbol binario balanceado hacia la izquierda (LLRBT) y retorna True o False.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave del nodo a buscar

    Returns:
        bool: True si el nodo existe, False si no existe
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        _found = False
        return _contains(_root, k, _cmp, _found)
    except Exception as exp:
        err("llrbt", "contains()", exp)


def _contains(node: dict, k: Any, cmp_func: Callable, found: bool) -> bool:
    """_contains funcion recursiva que revisa si un nodo existe en el árbol binario balanceado hacia la izquierda (LLRBT) y retorna True o False.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a buscar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol
        found (bool): bandera que indica si el nodo fue encontrado. False por defecto

    Returns:
        bool: True si el nodo existe, False si no existe
    """
    try:
        # caso base, el arbol esta vacio
        if node is None:
            return found
        # caso base, el arbol no esta vacio
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es igual, retornar True
            if _cmp == 0:
                found = True
            # si la llave es menor, buscar en el subarbol izquierdo
            elif _cmp < 0:
                found = _contains(node["left"], k, cmp_func, found)
            # si la llave es mayor, buscar en el subarbol derecho
            elif _cmp > 0:
                found = _contains(node["right"], k, cmp_func, found)
        return found
    except Exception as exp:
        err("llrbt", "_contains()", exp)


def size(tree: dict) -> int:
    """size contador de nodos del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el tamaño del árbol.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        int: tamaño del árbol binario balanceado hacia la izquierda (LLRBT)
    """
    try:
        return _size(tree["root"])
    except Exception as exp:
        err("llrbt", "size()", exp)


def _size(node: dict) -> int:
    """_size funcion recursiva que cuenta los nodos del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el tamaño del árbol.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        int: tamaño del árbol binario balanceado hacia la izquierda (LLRBT), por defecto 0. Ademas, recordar que el nodo BST por defecto es de tamaño 1
    """
    if node is None:
        return 0
    return node["size"]


def is_empty(tree: dict) -> bool:
    """is_empty revisa si el árbol binario balanceado hacia la izquierda (LLRBT) está vacío y retorna True o False.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        bool: True si el árbol está vacío, False si no está vacío
    """
    try:
        return tree["root"] is None
    except Exception as exp:
        err("llrbt", "is_empty()", exp)


def min(tree: dict) -> dict:
    """min recupera el nodo con la llave mínima del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        dict: diccionario con el nodo minimo
    """
    try:
        _min_node = _min(tree["root"])
        if _min_node is not None:
            return _min_node["key"]
        return None
    except Exception as exp:
        err("llrbt", "min()", exp)


def _min(node: dict) -> dict:
    """_min funcion recursiva que recupera el nodo con la llave mínima del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario con el nodo minimo
    """
    try:
        __min__ = node
        if node is not None:
            if node["left"] is not None:
                __min__ = node
            else:
                __min__ = _min(node["left"])
        return __min__
    except Exception as exp:
        err("llrbt", "_min()", exp)


def delete_min(tree: dict) -> dict:
    """delete_min elimina el nodo con la llave mínima del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el nodo a eliminar.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        _root = tree["root"]
        # caso base, si el arbol no esta vacio
        if _root is not None:
            # caso base, si el hijo izquierdo y derecho no son rojos
            if not _is_red(_root["left"]) and not _is_red(_root["right"]):
                # cambiar el color del padre a rojo
                _root["color"] = trn.RED
            _root = _delete_min(_root)
            # actualizando el color de la raiz
            if _root is not None:
                _root["color"] = trn.BLACK
        # actualizando la raiz del árbol
        tree["root"] = _root
        # retornando el árbol actualizado
        return tree
    except Exception as exp:
        err("llrbt", "delete_min()", exp)


def _delete_min(node: dict) -> dict:
    """_delete_min funcion recursiva que elimina el nodo con la llave mínima del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el nodo a eliminar.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        if node is not None:
            if node["left"] is None:
                return node["right"]
            if not _is_red(node["left"]) and not _is_red(node["left"]["left"]):
                node = _move_red_left(node)
            # caso base, si el nodo izquierdo es rojo
            node["left"] = _delete_min(node["left"])
            # balancear el árbol
            node = _balance(node)
            # actualizar el tamaño del nodo
            # TODO: revisar si es necesario actualizar el tamaño del nodo
            # node["size"] = _size(node["left"]) + _size(node["right"]) + 1
        return node
    except Exception as exp:
        err("llrbt", "_delete_min()", exp)


def max(tree: dict) -> dict:
    """max recupera el nodo con la llave máxima del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        dict: diccionario con el nodo maximo
    """
    try:
        _max_node = _max(tree["root"])
        if _max_node is not None:
            return _max_node["key"]
        return None
    except Exception as exp:
        err("llrbt", "max()", exp)


def _max(node: dict) -> dict:
    """_max funcion recursiva que recupera el nodo con la llave máxima del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario con el nodo maximo
    """
    try:
        __max__ = None
        if node is not None:
            if node["right"] is not None:
                __max__ = node
            else:
                __max__ = _max(node["right"])
        return __max__
    except Exception as exp:
        err("llrbt", "_max()", exp)


def delete_max(tree: dict) -> dict:
    """delete_max elimina el nodo con la llave máxima del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el nodo a eliminar.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        _root = tree["root"]
        # caso base, si el arbol no esta vacio
        if _root is not None:
            # caso base, si el hijo izquierdo y derecho no son rojos
            if not _is_red(_root["left"]) and not _is_red(_root["right"]):
                # cambiar el color del padre a rojo
                _root["color"] = trn.RED
            _root = _delete_max(_root)
            # actualizando el color de la raiz
            if _root is not None:
                _root["color"] = trn.BLACK
        # actualizando la raiz del árbol
        tree["root"] = _root
        # retornando el árbol actualizado
        return tree
    except Exception as exp:
        err("llrbt", "delete_max()", exp)


def _delete_max(node: dict) -> dict:
    """_delete_max funcion recursiva que elimina el nodo con la llave máxima del árbol binario balanceado hacia la izquierda (LLRBT) y retorna el nodo a eliminar.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT) actualizado
    """
    try:
        # caso base, si el hijo izquierdo es rojo
        if _is_red(node["left"]):
            # rotar a la derecha
            node = _rotate_right(node)
        # caso base, si no tiene hijo derecho
        if node["right"] is None:
            return None
        # caso base, si el hijo derecho y su hijo izquierdo no son rojos
        if not _is_red(node["right"]) and not _is_red(node["right"]["left"]):
            # invertir colores a la derecha
            node = _move_red_right(node)
        # caso base, si el nodo derecho es rojo
        node["right"] = _delete_max(node["right"])
        # balancear el árbol
        node = _balance(node)
        return node
    except Exception as exp:
        err("llrbt", "_delete_max()", exp)


def floor(tree: dict, k: Any) -> dict:
    """floor recupera el nodo con la llave máxima menor o igual a k del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave a buscar

    Returns:
        dict: diccionario con el nodo maximo menor o igual a k
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _floor(_root, k, _cmp)
    except Exception as exp:
        err("llrbt", "floor()", exp)


def _floor(node: dict, k: Any, cmp_func: Callable) -> dict:
    """_floor funcion recursiva que recupera el nodo con la llave máxima menor o igual a k del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        k (Any): llave a buscar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario con el nodo maximo menor o igual a k
    """
    try:
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es igual, retornar el nodo
            if _cmp == 0:
                return node
            # si la llave es menor, buscar en el subarbol izquierdo
            elif _cmp < 0:
                return _floor(node["left"], k, cmp_func)
            # si la llave es mayor, buscar en el subarbol derecho
            else:
                _node = _floor(node["right"], k, cmp_func)
                if _node is not None:
                    return _node
                else:
                    return node
        # caso base, el arbol esta vacio
        # TODO retornar node es viable?
        return None
    except Exception as exp:
        err("llrbt", "_floor()", exp)


def ceiling(tree: dict, k: Any) -> dict:
    """ceiling recupera el nodo con la llave mínima mayor o igual a k del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave a buscar

    Returns:
        dict: diccionario con el nodo minimo mayor o igual a k
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _ceiling(_root, k, _cmp)
    except Exception as exp:
        err("llrbt", "ceiling()", exp)


def _ceiling(node: dict, k: Any, cmp_func: Callable) -> dict:
    """_ceiling funcion recursiva que recupera el nodo con la llave mínima mayor o igual a k del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        k (Any): llave a buscar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario con el nodo minimo mayor o igual a k
    """
    try:
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es igual, retornar el nodo
            if _cmp == 0:
                return node
            # si la llave es menor, buscar en el subarbol izquierdo
            elif _cmp < 0:
                _node = _ceiling(node["left"], k, cmp_func)
                if _node is not None:
                    return _node
                else:
                    return node
            # si la llave es mayor, buscar en el subarbol derecho
            else:
                return _ceiling(node["right"], k, cmp_func)
        # caso base, el arbol esta vacio
        # TODO retornar node es viable?
        return None
    except Exception as exp:
        err("llrbt", "_ceiling()", exp)


def select(tree: dict, k: int) -> dict:
    """select recupera el nodo con la k-esima llave del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (int): k-esima llave a buscar

    Returns:
        dict: diccionario con el nodo k-esimo
    """
    try:
        _root = tree["root"]
        return _select(_root, k)
        # node = selectKey(bst['root'], pos)
        # if (node is not None):
        #     return node['key']
    except Exception as exp:
        err("llrbt", "select()", exp)


def _select(node: dict, k: int) -> dict:
    """_select funcion recursiva que recupera el nodo con la k-esima llave del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        k (int): k-esima llave a buscar

    Returns:
        dict: diccionario con el nodo k-esimo
    """
    try:
        if node is not None:
            _left_n = _size(node["left"])
            # si la k-esima llave es menor que el tamaño del subarbol izquierdo
            if k < _left_n:
                return _select(node["left"], k)
            # si la k-esima llave es mayor que el tamaño del subarbol izquierdo
            elif k > _left_n:
                return _select(node["right"], k - _left_n - 1)
            # si la k-esima llave es igual al tamaño del subarbol izquierdo
            elif k == _left_n:
                return node
        # caso base, el arbol esta vacio
        # TODO retornar node es viable?
        return None
    except Exception as exp:
        err("llrbt", "_select()", exp)


def rank(tree: dict, k: Any) -> int:
    """rank recupera el tamaño del subarbol izquierdo del nodo con la llave k del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        k (Any): llave a buscar

    Returns:
        int: tamaño del subarbol izquierdo del nodo con la llave k
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _rank(_root, k, _cmp)
    except Exception as exp:
        err("llrbt", "rank()", exp)


def _rank(node: dict, k: Any, cmp_func: Callable) -> int:
    """_rank funcion recursiva que recupera el tamaño del subarbol izquierdo del nodo con la llave k del árbol binario balanceado hacia la izquierda (LLRBT) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        k (Any): llave a buscar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        int: tamaño del subarbol izquierdo del nodo con la llave k
    """
    try:
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es menor, buscar en el subarbol izquierdo
            if _cmp < 0:
                return _rank(node["left"], k, cmp_func)
            # si la llave es mayor, buscar en el subarbol derecho
            elif _cmp > 0:
                _n_left = _size(node["left"])
                # retornar el tamaño del subarbol izquierdo + 1 + el tamaño del subarbol derecho
                _n_right = _rank(node["right"], k, cmp_func)
                # retornar el tamaño del subarbol izquierdo + 1 + el tamaño del subarbol derecho
                return _n_left + 1 + _n_right
            # si la llave es igual, retornar el tamaño del subarbol izquierdo
            else:
                return _size(node["left"])
        # caso base, el arbol esta vacio
        return 0
    except Exception as exp:
        err("llrbt", "_rank()", exp)


def height(tree: dict) -> int:
    """height retorna la altura del árbol binario balanceado hacia la izquierda (LLRBT).

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)

    Returns:
        int: altura del árbol binario balanceado hacia la izquierda (LLRBT)
    """
    try:
        return _height(tree["root"])
    except Exception as exp:
        err("llrbt", "height()", exp)


def _height(node: dict) -> int:
    """_height funcion recursiva que retorna la altura del árbol binario balanceado hacia la izquierda (LLRBT).

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        int: altura del árbol binario balanceado hacia la izquierda (LLRBT)
    """
    try:
        if node is None:
            return -1
        else:
            left_h = _height(node["left"])
            right_h = _height(node["right"])
            return max(left_h, right_h) + 1
    except Exception as exp:
        err("llrbt", "_height()", exp)


def range(tree: dict, low: Any, high: Any) -> dict:
    """range retorna una lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango

    Returns:
        dict: lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        _lt_range = sllt.new_list(cmp_function=_cmp)
        _lt_range = _range(_root, low, high, _cmp, _lt_range)
        return _lt_range
    except Exception as exp:
        err("llrbt", "range()", exp)


def _range(node: dict,
           low: Any,
           high: Any,
           cmp_func: Callable,
           lt_range: dict) -> dict:
    """_range funcion recursiva que retorna una lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango
        cmp_func (Callable): funcion de comparacion para los elementos del árbol
        lt_range (dict): lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]

    Returns:
        dict: _description_
    """
    # TODO check the if statement for infinite loops
    try:
        return lt_range
    except Exception as exp:
        err("llrbt", "_range()", exp)


def keys(tree: dict, low: Any, high: Any) -> dict:
    """keys retorna una lista con las llaves del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango

    Returns:
        dict: lista con las llaves del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    try:
        _keys_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        _cmp = tree["cmp_func"]
        _keys_lt = _keys(tree["root"], low, high, _cmp, _keys_lt)
        return _keys_lt
    except Exception as exp:
        err("llrbt", "keys()", exp)


def _keys(node: dict,
          low: Any,
          high: Any,
          cmp_func: Callable,
          keys_lt: dict) -> dict:
    """_keys funcion recursiva que retorna una lista con las llaves del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango
        cmp_func (Callable): funcion de comparacion para los elementos del árbol
        keys_lt (dict): lista con las llaves del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]

    Returns:
        dict: lista con las llaves del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    # TODO check if i generate an in-order traversal of the tree
    try:
        return keys_lt
    except Exception as exp:
        err("llrbt", "_keys()", exp)


def values(tree: dict, low: Any, high: Any) -> dict:
    """values retorna una lista con los valores del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango

    Returns:
        dict: lista con los valores del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    try:
        _values_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        _cmp = tree["cmp_func"]
        _values_lt = _values(tree["root"], low, high, _cmp, _values_lt)
        return _values_lt
    except Exception as exp:
        err("llrbt", "values()", exp)


def _values(node: dict,
            low: Any,
            high: Any,
            cmp_func: Callable,
            values_lt: dict) -> dict:
    """_values funcion recursiva que retorna una lista con los valores del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango
        cmp_func (Callable): funcion de comparacion para los elementos del árbol
        values_lt (dict): lista con los valores del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]

    Returns:
        dict: lista con los valores del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    # TODO check if i generate an in-order traversal of the tree
    try:
        return values_lt
    except Exception as exp:
        err("llrbt", "_values()", exp)


def entries(tree: dict, low: Any, high: Any) -> dict:
    """entries retorna una lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high].

    Args:
        tree (dict): diccionario que representa el árbol binario balanceado hacia la izquierda (LLRBT)
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango

    Returns:
        dict: lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    try:
        _entries_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        _cmp = tree["cmp_func"]
        _entries_lt = _entries(tree["root"], low, high, _cmp, _entries_lt)
        return _entries_lt
    except Exception as exp:
        err("llrbt", "entries()", exp)


def _entries(node: dict,
             low: Any,
             high: Any,
             cmp_func: Callable,
             entries_lt: dict) -> dict:
    """_entries _summary_

    Args:
        node (dict): diccionario que representa el nodo actual del árbol
        low (Any): llave mínima del rango
        high (Any): llave máxima del rango
        cmp_func (Callable): funcion de comparacion para los elementos del árbol
        entries_lt (dict): lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]

    Returns:
        dict: lista con los nodos del árbol binario balanceado hacia la izquierda (LLRBT) que están dentro del rango [low, high]
    """
    # TODO check if i generate an in-order traversal of the tree
    try:

        return entries_lt
    except Exception as exp:
        err("llrbt", "_entries()", exp)


def _flip_colors_node(node: dict) -> None:
    """_flip_colors_node _summary_

    Args:
        node (dict): _description_

    Returns:
        _type_: _description_
    """
    try:
        __flip_colors_node(node)
        __flip_colors_node(node["left"])
        __flip_colors_node(node["right"])
    except Exception as exp:
        err("llrbt", "_flip_colors()", exp)


def __flip_colors_node(node: dict) -> None:
    try:
        if node is not None:
            if node["color"] == trn.RED:
                node["color"] = trn.BLACK
            else:
                node["color"] = trn.RED
    except Exception as exp:
        err("llrbt", "__flip_colors_node()", exp)


def _rotate_left(node: dict) -> dict:
    """_rotate_left _summary_

    Args:
        node (dict): _description_

    Returns:
        _type_: _description_
    """
    try:
        # actualizar el nodo izquierdo
        # caso base, el arbol esta vacio
        temp = node["right"]
        node["right"] = temp["left"]
        temp["left"] = node
        temp["color"] = node["color"]
        node["color"] = trn.RED
        # actualizar el tamaño de los nodos
        temp["size"] = node["size"]
        node["size"] = _size(node["left"]) + _size(node["right"]) + 1
        # retornar el nodo izquierdo
        return temp
    except Exception as exp:
        err("llrbt", "_rotate_left()", exp)


def _rotate_right(node: dict) -> dict:
    try:
        # actualizar el nodo derecho
        # caso base, el arbol esta vacio
        temp = node["left"]
        node["left"] = temp["right"]
        temp["right"] = node
        temp["color"] = node["color"]
        node["color"] = trn.RED
        # actualizar el tamaño de los nodos
        temp["size"] = node["size"]
        node["size"] = _size(node["left"]) + _size(node["right"]) + 1
        # retornar el nodo derecho
        return temp
    except Exception as exp:
        err("llrbt", "_rotate_right()", exp)


def _is_red(node: dict) -> bool:
    """_is_red _summary_

    Args:
        node (dict): _description_

    Returns:
        bool: _description_
    """
    try:
        if node is None:
            return False
        return node["color"] == trn.RED
    except Exception as exp:
        err("llrbt", "_is_red()", exp)


def _move_red_right(node: dict) -> dict:
    """_move_red_right _summary_

    Args:
        node (dict): _description_

    Returns:
        _type_: _description_
    """
    try:
        # cambiar el color del nodo
        _flip_colors_node(node)
        # si el hijo izquierdo es rojo, rotar a la derecha
        if _is_red(node["left"]["left"]):
            node = _rotate_right(node)
            # cambiar el color del nodo
            _flip_colors_node(node)
        return node
    except Exception as exp:
        err("llrbt", "_move_red_right()", exp)


def _move_red_left(node: dict) -> dict:
    """_move_red_left _summary_

    Args:
        node (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        # cambiar el color del nodo
        _flip_colors_node(node)
        # si el hijo derecho es rojo, rotar a la izquierda
        if _is_red(node["right"]["left"]):
            node["right"] = _rotate_right(node["right"])
            node = _rotate_left(node)
            # cambiar el color del nodo
            _flip_colors_node(node)
        return node
    except Exception as exp:
        err("llrbt", "_move_red_left()", exp)


def _balance(node: dict) -> dict:
    """_balance _summary_

    Args:
        node (dict): _description_

    Returns:
        _type_: _description_
    """
    try:
        # si el hijo derecho es rojo, rotar a la izquierda
        if _is_red(node["right"]):
            node = _rotate_left(node)
        # si el hijo izquierdo es rojo y el hijo izquierdo del hijo izquierdo es rojo, rotar a la derecha
        if _is_red(node["left"]) and _is_red(node["left"]["left"]):
            node = _rotate_right(node)
        # si el hijo izquierdo es rojo y el hijo derecho es rojo, cambiar el color del nodo
        if _is_red(node["left"]) and _is_red(node["right"]):
            __flip_colors_node(node)
        # actualizar el tamaño del nodo
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        node["size"] = _left_n + _right_n + 1
        # retornar el nodo balanceado
        return node
    except Exception as exp:
        err("llrbt", "_balance()", exp)
