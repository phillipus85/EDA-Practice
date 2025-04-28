"""
Module to handle aan Adjacency list in a graph.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# import python modules
from typing import Any, Callable

# import modules for data structures lists + maps
# sllt y lpht ahorran espacio y tiempo en la busqueda de elementos
from Src.Func.DataStructs.List import sllt
from Src.Func.DataStructs.Tables import lpht

# import error handler
from Src.Func.Utils.error import error_handler as err

# import edge module
from Src.Func.DataStructs.Graphs import edge as edg


def dflt_graph_edge_cmp(key1: Any, key2: Any) -> int:
    """dflt_graph_edge_cmp funcion de comparacion de llaves para el grafo

    Args:
        key1 (Any): primera llave del nodo a comparar
        key2 (Any): segunda llave del nodo a comparar

    Returns:
        int: -1 si key1 < key2, 0 si key1 == key2, 1 si key1 > key2
    """
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


def new_graph(cmp_func: Callable = dflt_graph_edge_cmp,
              directed: bool = False,
              size: int = 10) -> dict:
    try:
        _new_al = dict(
            vertices=lpht.new_lpht(size, cmp_func),
            edges=sllt.new_sllt(size, cmp_func),
            size=0,     # number of vertices
            order=0,    # number of edges
            directed=directed,  # directed or undirected graph
            cmp_func=cmp_func,
            _type="adj_lt",
        )
        if not directed:
            _new_al["degrees"] = lpht.new_lpht(size, cmp_func)
        elif directed:
            _new_al["indegrees"] = lpht.new_lpht(size, cmp_func)
            _new_al["outdegrees"] = lpht.new_lpht(size, cmp_func)
        return _new_al
    except Exception as exp:
        err("AL", "new_graph()", exp)


def add_vertex(grf: dict, vtx: Any) -> None:
    try:
        pass
    except Exception as exp:
        err("AL", "add_vertex()", exp)


def remove_vertex(grf: dict, vtx: Any) -> None:
    try:
        pass
    except Exception as exp:
        err("AL", "remove_vertex()", exp)


def get_vertex(grf: dict, vtx: Any) -> dict:
    try:
        return lpht.get(grf["vertices"], vtx)
    except Exception as exp:
        err("AL", "get_vertex()", exp)


def add_edge(grf: dict, vtx_a: Any, vtx_b: Any, weight: int = 0) -> None:
    try:
        pass
    except Exception as exp:
        err("AL", "add_edge()", exp)


def remove_edge(grf: dict, vtx_a: Any, vtx_b: Any) -> None:
    try:
        pass
    except Exception as exp:
        err("AL", "remove_edge()", exp)


def get_edge(grf: dict, vtx_a: Any, vtx_b: Any) -> dict:
    try:
        pass
    except Exception as exp:
        err("AL", "get_edge()", exp)


def size(grf: dict) -> int:
    try:
        return grf["size"]
    except Exception as exp:
        err("AL", "size()", exp)


def order(grf: dict) -> int:
    try:
        return grf["order"]
    except Exception as exp:
        err("AL", "order()", exp)


def is_directed(grf: dict) -> bool:
    try:
        return grf["directed"]
    except Exception as exp:
        err("AL", "is_directed()", exp)


def is_empty(grf: dict) -> bool:
    try:
        return grf["size"] == 0
    except Exception as exp:
        err("AL", "is_empty()", exp)


def is_weighted(grf: dict) -> bool:
    try:
        pass
    except Exception as exp:
        err("AL", "is_weighted()", exp)


def edges(grf: dict) -> list:
    try:
        return grf["edges"]
    except Exception as exp:
        err("AL", "edges()", exp)


def vertices(grf: dict) -> list:
    try:
        return grf["vertices"]
    except Exception as exp:
        err("AL", "vertices()", exp)


def degree(grf: dict, vtx: Any) -> int:
    try:
        pass
    except Exception as exp:
        err("AL", "degree()", exp)


def contain_edge(grf: dict, vtx_a: Any, vtx_b: Any) -> bool:
    try:
        pass
    except Exception as exp:
        err("AL", "contain_edge()", exp)


def contain_vertex(grf: dict, vtx: Any) -> bool:
    try:
        return lpht.contains(grf["vertices"], vtx)
    except Exception as exp:
        err("AL", "contain_vertex()", exp)


def adjacent_vertices(grf: dict, vtx: Any) -> list:
    try:
        pass
    except Exception as exp:
        err("AL", "adjacent_vertices()", exp)


def adjacent_edges(grf: dict, vtx: Any) -> list:
    try:
        pass
    except Exception as exp:
        err("AL", "adjacent_edges()", exp)
