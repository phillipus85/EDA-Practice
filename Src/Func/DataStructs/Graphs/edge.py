"""
Module to handle an edge in a graph.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


def new_edge(va, vb, weight=0):
    """
    Crea un nuevo arco entre los vértices `va` y `vb`.

    Args:
        va (object): Vértice A.
        vb (object): Vértice B.
        weight (int, optional): Peso del arco. Por defecto es 0.

    Returns:
        dict: Representación del arco.
    """
    return {"vtx_a": va, "vtx_b": vb, "weight": weight}


def weight(edge):
    """
    Retorna el peso de un arco.

    Args:
        edge (dict): Arco.

    Returns:
        int: Peso del arco.
    """
    return edge["weight"]


def either(edge):
    """
    Retorna el vértice A del arco.

    Args:
        edge (dict): Arco.

    Returns:
        object: Vértice A.
    """
    return edge["vtx_a"]


def other(edge, veither):
    """
    Retorna el otro vértice del arco distinto de `veither`.

    Args:
        edge (dict): Arco.
        veither (object): Vértice conocido.

    Returns:
        object: El otro vértice del arco.
    """
    return edge["vtx_b"] if veither == edge["vtx_a"] else edge["vtx_a"]


def set_weight(edge, weight):
    """
    Actualiza el peso de un arco.

    Args:
        edge (dict): Arco.
        weight (int): Nuevo peso del arco.
    """
    edge["weight"] = weight


def compare_edges(edge1, edge2):
    """
    Compara dos arcos.

    Args:
        edge1 (dict): Primer arco.
        edge2 (dict): Segundo arco.

    Returns:
        int: 0 si los arcos son iguales, 1 si `edge1 > edge2`, -1 si `edge1 < edge2`.
    """
    e1v, e2v = either(edge1), either(edge2)
    if e1v == e2v:
        return (0 if other(edge1, e1v) == other(edge2, e2v)
                else 1 if other(edge1, e1v) > other(edge2, e2v)
                else -1)
    return 1 if e1v > e2v else -1
