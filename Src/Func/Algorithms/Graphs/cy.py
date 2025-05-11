"""
Module to execute a depth-first search (DFS) in a graph represented as an adjacency list.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
from typing import Any
from Src.Func.DataStructs.Graphs import adjlt as g
from Src.Func.DataStructs.Graphs import edge as edg
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.List import stack as stk
from Src.Func.DataStructs.List import queue as q
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.Utils.error import error_handler as err


def directed_cycle(grf: dict) -> bool:
    """*directed_cycle()* funcion para detectar ciclos en un grafo dirigido

    Args:
        grf (dict): diccionario que representa el grafo

    Returns:
        bool: True si el grafo tiene ciclos, False en caso contrario
    """
    try:
        _search = _cfg_search(grf)
        _vertices = g.vertices(grf)
        for v in lt.iterator(_vertices):
            if not mp.get(_search["marked"], v)["value"]:
                _dfs(grf, v, _search)
        return _search
    except Exception as exp:
        err("Cycle", "directed_cycle", exp)


def _dfs(grf: dict, vtx: Any, search: dict) -> None:
    """_dfs funcion auxiliar para detectar ciclos en un grafo dirigido

    Args:
        grf (dict): diccionario que representa el grafo
        vtx (Any): vertice de inspeccion del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el orden topologico
    """
    try:
        mp.put(search["marked"], vtx, True)
        mp.put(search["on_stack"], vtx, True)
        adj = g.adjacent_edges(grf, vtx)
        for e in lt.iterator(adj):
            w = edg.other(e, vtx)
            if not stk.is_empty(search["cycle"]):
                return search
            elif not mp.get(search["marked"], w)["value"]:
                mp.put(search["edge_to"], w, e)
                _dfs(grf, w, search)
            elif mp.get(search["on_stack"], w)["value"]:
                f = e
                while edg.either(f) != w:
                    stk.push(search["cycle"], f)
                    f = mp.get(search["edge_to"], edg.either(f))["value"]
                stk.push(search["cycle"], f)
                return search
        mp.put(search["on_stack"], vtx, False)
    except Exception as exp:
        err("Cycle", "_dfs", exp)


def has_cycle(grf: dict) -> bool:
    """*has_cycle()* funcion para detectar ciclos en un grafo dirigido

    Args:
        grf (dict): diccionario que representa el grafo

    Returns:
        bool: True si el grafo tiene ciclos, False en caso contrario
    """
    try:
        return not stk.is_empty(grf["cycle"])
    except Exception as exp:
        err("Cycle", "has_cycle", exp)


def cycle(grf: dict) -> list:
    """*cycle()* funcion para detectar ciclos en un grafo dirigido

    Args:
        grf (dict): diccionario que representa el grafo

    Returns:
        list: lista de vertices que forman el ciclo
    """
    return grf["cycle"]


def _cfg_search(grf: dict) -> dict:
    """*cfg_search()* funcion para crear la estructura de busqueda para el algoritmo de DFS

    Args:
        grf (dict): diccionario que representa el grafo

    Returns:
        dict: estructura (linear probing HT) para almacenar el recorrido DFS
    """
    try:
        _search = dict(
            marked=None,
            edge_to=None,
            on_stack=None,
            cycle=None,
            has_cycle=False,
            algorithm="Cycle",
            _type=grf["_type"],
        )
        _search["marked"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        _search["edge_to"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        _search["on_stack"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        _search["cycle"] = stk.new_stack()
        return _search
    except Exception as exp:
        err("Cycle", "cfg_search", exp)
