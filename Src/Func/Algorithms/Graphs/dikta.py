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
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.Utils.error import error_handler as err
import math
from Src.Func.DataStructs.Trees import idxheap as pq
from Src.Func.DataStructs.List import stack as stk
# from Src.Func.DataStructs.List import queue as q


def dijkstra(grf: dict, src: Any) -> dict:
    """*dijkstra()* funcion para construir un arbol de expansion minima (MST) en un grafo
    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido DFS
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        _search = _cfg_search(grf)
        while not pq.is_empty(_search["minpq"]):
            v = pq.del_min(_search["minpq"])
            edges = g.adjacent_edges(grf, v)
            if edges is not None:
                for e in lt.iterator(edges):
                    _relax(e, _search)
        return _search
    except Exception as exp:
        err("Dijkstra", "dijkstra", exp)


def _relax(e: Any, search: dict) -> None:
    """_relax funcion auxiliar para relajar un arco en el algoritmo de Dijkstra

    Args:
        e (Any): arco a relajar
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS
    """
    try:
        v = edg.either(e)
        w = edg.other(e, v)
        _v_vtx = mp.get(search["visited"], v)
        _w_vtx = mp.get(search["visited"], w)
        dist_v = _v_vtx["value"]["dist_to"] + edg.weight(e)
        dist_w = _w_vtx["value"]["dist_to"]
        if _w_vtx is None or dist_w > dist_v:
            dist_w = _v_vtx["value"]["dist_to"] + edg.weight(e)
            mp.put(search["visited"],
                   w,
                   dict(marked=True, dist_to=dist_w, edge_to=e))
            if pq.contains(search["minpq"], w):
                pq.decrease_key(search["minpq"], w, dist_w)
            else:
                pq.insert(search["minpq"], w, dist_w)
        return search
    except Exception as exp:
        err("Dijkstra", "_relax", exp)


def dist_to(vtx: Any, search: dict) -> float:
    """dist_to funcion auxiliar para obtener la distancia minima a un vertice

    Args:
        vertex (Any): vertice de inicio del recorrido DFS
        search (dict): estructura (linear probing HT) para almacenar el recorrido DFS

    Returns:
        float: distancia minima al vertice
    """
    try:
        _dist = math.inf
        _v_vtx = mp.get(search["visited"], vtx)
        if _v_vtx is not None:
            _dist = _v_vtx["value"]["dist_to"]
        return _dist
    except Exception as exp:
        err("Dijkstra", "dist_to", exp)


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
        _visited = mp.get(search["visited"], vtx)["value"]
        if _visited is not None and _visited["marked"]:
            has_path = True
        return has_path
    except Exception as exp:
        err("Dijkstra", "has_path_to", exp)


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
                v_vtx = mp.get(search["visited"], vtx)["value"]
                e = v_vtx["edge_to"]
                stk.push(_path, e)
                vtx = edg.either(e)
        return path
    except Exception as exp:
        err("Dijkstra", "path_to", exp)


# ----------------------------------------------
#         Funciones Auxiliares
# ----------------------------------------------


def _cfg_search(grf: dict, src: Any) -> dict:
    """_cfg_search funcion auxiliar para configurar la estructura de busqueda

    Args:
        grf (dict): diccionario que representa el grafo

    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices del arbol de expansion minima
    """
    try:
        _search = dict(
            src=src,
            visited=None,
            minpq=None,
            algorithm="Dijkstra",
            _type=grf["_type"],)
        _search["visited"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        vertices = g.vertices(grf)
        for v in lt.iterator(vertices):
            mp.put(_search["visited"],
                   v,
                   dict(marked=False, dist_to=math.inf, edge_to=None))
        mp.put(_search["visited"],
               src,
               dict(marked=True, dist_to=0, edge_to=None))
        _search["minpq"] = pq.new_heap(grf["cmp_func"])
        pq.insert(_search["minpq"], src, 0)
        return _search
    except Exception as exp:
        err("Dijkstra", "_cfg_search", exp)
