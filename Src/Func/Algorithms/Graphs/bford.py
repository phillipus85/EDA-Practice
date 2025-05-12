"""
Module to execute a depth-first search (DFS) in a graph represented as an adjacency list.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

from typing import Any
import math
from Src.Func.DataStructs.Graphs import adjlt as g
from Src.Func.DataStructs.Graphs import edge as edg
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.Utils.error import error_handler as err
from Src.Func.DataStructs.List import stack as stk
from Src.Func.DataStructs.List import queue as q
from Src.Func.Algorithms.Graphs import cy as c


def bellman_ford(grf: dict, src: Any) -> dict:
    """*bellman_ford()* funcion principal para encontrar el camino mas corto desde un vertice a todos los demas vertices con el algoritmo de Bellman-Ford
    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del algoritmo de Bellman-Ford
    """
    try:
        _search = _cfg_search(grf)
        mp.put(_search["dist_to"], src, 0.0)
        q.enqueue(_search["qvtx"], src)
        mp.put(_search["onque"], src, True)
        while not q.is_empty(_search["qvtx"]) and not _has_negative_cycle(_search):
            vtx = q.dequeue(_search["qvtx"])
            mp.put(_search["onque"], vtx, False)
            _relax(grf, vtx, _search)
        return _search
    except Exception as exp:
        err("BFord", "bellman_ford", exp)


def _relax(grf: dict, vtx: Any, search: dict) -> None:
    """*_relax()* funcion auxiliar para relajar un arco en el algoritmo de Bellman-Ford

    Args:
        grf (dict): grafo representado como un diccionario
        v (Any): vertice a relajar
        search (dict): estructura (linear probing HT) para almacenar el recorrido del algoritmo de Bellman-Ford
    """
    try:
        edges = g.adjacent_edges(grf, vtx)
        if edges is not None:
            for e in lt.iterator(edges):
                v = edg.either(e)
                w = edg.other(e, v)
                dist_v = mp.get(search["dist_to"], v)["value"]
                dist_w = mp.get(search["dist_to"], w)["value"]
                dweight = dist_v + edg.weight(e)
                if dist_w > dweight:
                    mp.put(search["dist_to"], w, dweight)
                    mp.put(search["edge_to"], w, e)
                    if not mp.get(search["onque"], w)["value"]:
                        mp.put(search["onque"], w, True)
                        q.enqueue(search["qvtx"], w)
                cost = search["cost"]
                if cost % g.size(grf) == 0:
                    _find = _find_negative_cycle(grf, search)
                    if _has_negative_cycle(_find):
                        return
                search["cost"] += 1
        return search
    except Exception as exp:
        err("BFord", "_relax", exp)


def dist_to(vtx: Any, search: dict) -> float:
    """*dist_to()* funcion auxiliar para obtener la distancia minima a un vertice

    Args:
        vertex (Any): vertice de inicio del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS

    Returns:
        float: distancia minima al vertice
    """
    try:
        _dist = math.inf
        _v_vtx = mp.get(search["dist_to"], vtx)
        if _v_vtx is not None:
            _dist = _v_vtx["value"]
        return _dist
    except Exception as exp:
        err("BFord", "dist_to", exp)


def has_path_to(vtx: Any, search: dict) -> bool:
    """has_path_to funcion auxiliar para verificar si existe un camino a un vertice

    Args:
        vertex (Any): vertice de inicio del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS

    Returns:
        bool: True si existe un camino al vertice, False en caso contrario
    """
    try:
        has_path = False
        _dist = mp.get(search["dist_to"], vtx)["value"]
        if not _has_negative_cycle(search) and _dist < math.inf:
            has_path = True
        return has_path
    except Exception as exp:
        err("BFord", "has_path_to", exp)


def path_to(vtx: Any, search: dict) -> list:
    """path_to funcion auxiliar para obtener el camino a un vertice

    Args:
        vertex (Any): vertice de inicio del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS

    Returns:
        list: lista con el camino al vertice
    """
    try:
        path = None
        if has_path_to(vtx, search):
            _path = stk.new_stack()
            while vtx != search["src"]:
                e = mp.get(search["edge_to"], vtx)["value"]
                stk.push(_path, e)
                vtx = edg.either(e)
        return path
    except Exception as exp:
        err("BFord", "path_to", exp)


# ----------------------------------------------
#         Funciones Auxiliares
# ----------------------------------------------


def _cfg_search(grf: dict, src: Any) -> dict:
    """_cfg_search funcion auxiliar para configurar la estructura de busqueda
    Args:
        grf (dict): grafo representado como un diccionario
        src (Any): vertice de inicio del recorrido DFS
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        _search = dict(
            src=src,
            edge_to=None,
            dist_to=None,
            onque=None,
            spt=None,
            qvtx=None,
            cost=0,
            cycle=False
        )
        _search["edge_to"] = mp.new_mmp(g.size(grf),
                                        cmp_function=grf["cmp_func"])
        _search["dist_to"] = mp.new_mmp(g.size(grf),
                                        cmp_function=grf["cmp_func"])
        _search["onque"] = mp.new_mmp(g.size(grf),
                                      cmp_function=grf["cmp_func"])
        _search["spt"] = g.new_graph(g.size(grf),
                                     grf["cmp_func"],
                                     grf["directed"],
                                     grf["_type"])
        vertices = g.vertices(grf)
        for v in lt.iterator(vertices):
            mp.put(_search["dist_to"], v, math.inf)
            mp.put(_search["onque"], v, False)
            g.add_vertex(_search["spt"], v)
        _search["qvtx"] = q.new_queue()
        return _search
    except Exception as exp:
        err("BFord", "_cfg_search", exp)


def _find_negative_cycle(grf: dict, search: dict) -> bool:
    """_find_negative_cycle funcion auxiliar para verificar si existe un ciclo negativo en el grafo

    Args:
        grf (dict): grafo representado como un diccionario
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS

    Returns:
        bool: True si existe un ciclo negativo, False en caso contrario
    """
    try:
        vertices = g.vertices(grf)
        for v in lt.iterator(vertices):
            edge = mp.get(search["edge_to"], v)
            if edge is not None:
                edge = edge["value"]
                g.add_edge(search["spt"],
                           edg.either(edge),
                           edg.other(edge, edg.either(edge)),
                           edg.weight(edge))
        finder = c._dfs(search["spt"])
        search["cycle"] = not stk.is_empty(c.cycle(finder))
        return search["cycle"]
    except Exception as exp:
        err("BFord", "_find_negative_cycle", exp)


def _has_negative_cycle(search: dict) -> bool:
    """_has_negative_cycle funcion auxiliar para verificar si existe un ciclo negativo en el grafo
    Args:
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS
    Returns:
        bool: True si existe un ciclo negativo, False en caso contrario
    """
    try:
        return search["cycle"]
    except Exception as exp:
        err("BFord", "_has_negative_cycle", exp)
