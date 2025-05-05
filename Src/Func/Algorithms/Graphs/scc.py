"""
Module to execute a depth-first search (DFS) in a graph represented as an adjacency list.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

from typing import Any
from Src.Func.DataStructs.Graphs import adjlt as g
# from Src.Func.DataStructs.Graphs import edge as e
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.DataStructs.List import stack as stk
from Src.Func.Utils.error import error_handler as err
from Src.Func.Algorithms.Graphs import dfo


def kosaraju_scc(grf: dict) -> dict:
    """*kosaraju_scc()* funcion para construir un recorrido DFS en un grafo
    Args:
        grf (dict): diccionario que representa el grafo
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices conectados a source
    """
    try:
        scc = dict(
            idscc=None,
            marked=None,
            grmarked=None,
            components=0,
        )
        scc["idscc"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        scc["marked"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        scc["grmarked"] = mp.new_mp(g.size(grf), grf["cmp_func"])

        # Se calcula el grafo reverso de graph
        _grfr = reverse_graph(grf)

        # Se calcula el DFO del reverso de graph
        _dfor = dfo.dfo(_grfr)
        _grfr_post = _dfor["reversepost"]
        scc["components"] = 0
        while stk.is_empty(_grfr_post) is False:
            v = stk.pop(_grfr_post)
            if mp.contains(scc["marked"], v) is False:
                scc["components"] += 1
                _scc_count(grf, scc, v)
        return scc
    except Exception as exp:
        err("scc", "kosaraju_scc", exp)


def _scc_count(grf: dict, scc: dict, v: Any) -> None:
    """_scc_count() funcion auxiliar para calcular un recorrido DFS
    Args:
        grf (dict): diccionario que representa el grafo
        scc (dict): estructura (linear probing HT) para almacenar el recorrido DFS
        v (Any): vertice de inicio del recorrido DFS
    Returns:
        None: estructura (linear probing HT) con el mapa de los vertices conectados a src
    """
    try:
        mp.put(scc["marked"], v, True)
        mp.put(scc["idscc"], v, scc["components"])
        adj_st = g.adjacent_vertices(grf, v)
        for w in lt.iterator(adj_st):
            if mp.contains(scc["marked"], w) is False:
                _scc_count(grf, scc, w)
        return scc
    except Exception as exp:
        err("scc", "_scc_count", exp)


def reverse_graph(grf: dict) -> dict:
    """reverse_graph() funcion para calcular el grafo reverso de un grafo dirigido
    Args:
        grf (dict): diccionario que representa el grafo
    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices conectados a source
    """
    try:
        _grfr = g.new_graph(grf["cmp_func"],
                            grf["directed"],)
        # vertices = g.vertices(grf)
        for v in lt.iterator(g.vertices(grf)):
            g.add_vertex(_grfr, v)
            adj_st = g.adjacent_vertices(grf, v)
            for w in lt.iterator(adj_st):
                g.add_edge(_grfr, w, v)
        return _grfr
    except Exception as exp:
        err("scc", "reverse_graph", exp)


# --------------------------------------------------
#              Funciones Auxiliares
# --------------------------------------------------


def strongly_connected(scc: dict, v1: Any, v2: Any) -> bool:
    """strongly_connected() funcion para verificar si dos vertices son fuertemente conexos
    Args:
        scc (dict): estructura (linear probing HT) con el mapa de los vertices conectados
        v1 (Any): primer vertice a verificar por la conexidad
        v2 (Any): segundo vertice a verificar por la conexidad
    Returns:
        bool: True si los vertices son fuertemente conexos, False en caso contrario
    """
    try:
        # do i neet the 'value' ket?
        return mp.get(scc["idscc"], v1) == mp.get(scc["idscc"], v2)
    except Exception as exp:
        err("scc", "strongly_connected", exp)


def connected_components(scc: dict) -> dict:
    """connected_components() funcion para obtener los componentes conexos de un grafo
    Args:
        scc (dict): estructura (linear probing HT) con el mapa de los vertices conectados
    Returns:
        dict: diccionario (mapa) con los componentes conexos del grafo
    """
    try:

        return scc["components"]
    except Exception as exp:
        err("scc", "connected_components", exp)
