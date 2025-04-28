"""
Module to execute a depth-first search (DFS) in a graph represented as an adjacency list.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
from typing import Callable, Any

from Src.Func.DataStructs.Graphs import edge as e
from Src.Func.DataStructs.Graphs import adjlt as g
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.List import stack as st
from Src.Func.DataStructs.List import queue as q
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.Utils.error import error_handler as err


def dfs(grf: dict, src: Any) -> dict:
    """*dfs()* funcion para construir un recorrido DFS en un grafo

    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido DFS

    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices conectados a source
    """
    try:
        _search = dict(
            algorithm="DFS",
            _type=grf["_type"],
            source=src,
            visited=None,)
        _search["visited"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        tgt = dict(marked=True, edgeto=None)
        mp.put(_search["visited"], tgt)
        _dfs(grf, src, _search)
        return _search
    except Exception as exp:
        err("DFS", "dfs", exp)


def _dfs(grf: dict, src: Any, search: dict) -> dict:
    """*_dfs()* funcion auxiliar para calcular un recorrido DFS

    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS

    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices conectados a src
    """
    try:
        adj_st = g.adjacent_vertices(grf, src)
        for w in lt.iterator(adj_st):
            visited_w = mp.get(search["visited"], w)
            if visited_w is None:
                tgt = dict(marked=True, edgeto=src)
                mp.put(search["visited"], tgt)
                _dfs(grf, w, search)
        return search
    except Exception as exp:
        err("DFS", "_dfs", exp)
