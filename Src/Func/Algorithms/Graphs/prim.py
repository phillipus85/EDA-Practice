"""
Module to execute a depth-first search (DFS) in a graph represented as an adjacency list.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

from typing import Any
from Src.Func.DataStructs.Graphs import adjlt as g
from Src.Func.DataStructs.Graphs import edge as e
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.Utils.error import error_handler as err
import math
from Src.Func.DataStructs.Trees import idxheap as pq
from Src.Func.DataStructs.List import queue as q


def prim_mst(grf: dict, src: Any = None) -> dict:
    """*prim_mst()* funcion para construir un arbol de expansion minima (MST) en un grafo
    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido DFS
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        _search = _cfg_search(grf)
        _vertices = g.vertices(grf)
        if src is not None:
            pos = lt.find(_vertices, src)
            if pos > -1:
                lt.exchange(_vertices, 0, pos)
            for v in lt.iterator(_vertices):
                if not mp.get(_search["marked"], v)["value"]:
                    _prim_mst(grf, _search, v)
        return _search
    except Exception as exp:
        err("Prim", "prim_mst", exp)


def _prim_mst(grf: dict, search: dict, v: Any) -> dict:
    """_prim_mst() funcion para construir un arbol de expansion minima (MST) en un grafo
    Args:
        grf (dict): diccionario que representa el grafo
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS
        v (Any): vertice de inicio del recorrido DFS
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        mp.put(search["distTo"], v, 0.0)
        mp.put(search["pq"], v, 0.0)
        while not pq.is_empty(search["pq"]):
            _min = pq.del_min(search["pq"])
            _scan(grf, search, _min)
        return search
    except Exception as exp:
        err("Prim", "_prim_mst", exp)


def _scan(grf: dict, search: dict, vertex: Any) -> dict:
    """_scan() funcion para construir un arbol de expansion minima (MST) en un grafo
    Args:
        grf (dict): diccionario que representa el grafo
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS
        vertex (Any): vertice de inicio del recorrido DFS
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        mp.put(search["marked"], vertex, True)
        adj = g.adjacent_edges(grf, vertex)
        for ed in lt.iterator(adj):
            w = e.other(ed, vertex)
            if not mp.get(search["marked"], w)["value"]:
                if mp.get(search["distTo"], w)["value"] > e.weight(ed):
                    mp.put(search["distTo"], w, e.weight(ed))
                    mp.put(search["edgeto"], w, ed)
                    if pq.contains(search["pq"], w):
                        pq.decrease_key(search["pq"],
                                        w,
                                        e.weight(ed))
                    else:
                        pq.insert(search["pq"],
                                  w,
                                  mp.get(search["distTo"], w)["value"])
        return search
    except Exception as exp:
        err("Prim", "_scan", exp)


def _cfg_search(grf: dict) -> dict:
    """_cfg_search() funcion para inicializar la estructura de busqueda
    Args:
        grf (dict): diccionario que representa el grafo
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        _search = dict(
            algorithm="Prim",
            _type=grf["_type"],
            marked=None,
            distto=None,
            edgeto=None,
            pq=None,
            mst=None,
        )
        _search["marked"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        _search["distto"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        _search["edgeto"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        _search["pq"] = pq.new_heap(grf["cmp_func"])
        _search["mst"] = q.new_queue()

        for v in lt.iterator(g.vertices(grf)):
            mp.put(_search["marked"], v, False)
            mp.put(_search["distto"], v, math.inf)
            # mp.put(_search["edgeto"], v, None)
        return _search
    except Exception as exp:
        err("Prim", "_cfg_search", exp)
