"""
Module to execute a breadth-first search (BFS) in a graph represented as an adjacency list.

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


def bfs(grf: dict, src: Any) -> dict:
    """*bfs()* funcion para construir un recorrido BFS en un grafo

    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido BFS

    Returns:
        dict: estructura (linear probing HT) con el mapa de los vertices conectados a source
    """
    try:
        _search = dict(
            algorithm="BFS",
            _type=grf["_type"],
            source=src,
            visited=None,)
        _search["visited"] = mp.new_mp(g.size(grf), grf["cmp_func"])
        tgt = dict(marked=True, edgeto=None, dist=0)
        mp.put(_search["visited"], src, tgt)
        _bfs(grf, src, _search)
        return _search
    except Exception as exp:
        err("BFS", "bfs", exp)


def _bfs(grf: dict, src: Any, search: dict) -> None:
    """*_bfs()* funcion auxiliar para calcular un recorrido BFS
    Args:
        grf (dict): diccionario que representa el grafo
        src (Any): vertice de inicio del recorrido BFS
        search (dict): estructura (linear probing HT) para almacenar el recorrido BFS
    """
    try:
        adjq = q.new_q()
        q.enqueue(adjq, src)
        while not q.is_empty(adjq):
            vtx = q.dequeue(adjq)
            visited_vtx = mp.get(search["visited"], vtx)["value"]
            adj_lt = g.adjacents(grf, vtx)
            for w in lt.iterator(adj_lt):
                visited_w = mp.get(search["visited"], w)
                if visited_w is None:
                    dist_to_w = visited_vtx["dist"] + 1
                    tgt = dict(marked=True, edgeto=vtx, dist=dist_to_w)
                    mp.put(search["visited"], w, tgt)
                    q.enqueue(adjq, w)
    except Exception as exp:
        err("BFS", "_bfs", exp)
