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


def dfo(grf: dict) -> dict:
    """*dfo()* funcion para construir un recorrido DFS en un grafo

    Args:
        grf (dict): diccionario que representa el grafo

    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del orden topologico
    """
    try:
        _search = dict(
            marked=None,
            pre=None,
            post=None,
            reversepost=None,
            algorithm="DFSort",
            _type=grf["_type"],)
        _search["pre"] = q.new_queue()
        _search["post"] = q.new_queue()
        _search["reversepost"] = st.new_stack()
        _search["marked"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        vxt_lt = g.vertices(grf)
        for v in lt.iterator(vxt_lt):
            if not mp.contains(_search["marked"], v):
                _dfo(grf, v, _search)
        return _search
    except Exception as exp:
        err("DFSort", "dfo", exp)


def _dfo(grf: dict, vtx: Any, search: dict) -> dict:
    """_dfo funcion auxiliar para calcular el orden topologico de un grafo DFO (DFS)

    Args:
        grf (dict): diccionario que representa el grafo
        vtx (Any): vertice de inspeccion del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el orden topologico

    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del orden topologico
    """
    try:
        q.enqueue(search["pre"], vtx)
        mp.put(search["marked"], vtx, True)
        adj_vtx = g.adjacent_vertices(grf, vtx)
        for w in lt.iterator(adj_vtx):
            if not mp.contains(search["marked"], w):
                _dfo(grf, w, search)
        q.enqueue(search["post"], vtx)
        st.push(search["reversepost"], vtx)
        return search
    except Exception as exp:
        err("DFSort", "_dfo", exp)
