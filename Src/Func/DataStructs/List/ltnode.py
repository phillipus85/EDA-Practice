"""
Module to handle a single linked list nodes (slln) data structure.
This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


def new_single_node(elm: object) -> dict:
    """new_single_node _summary_

    Args:
        elm (object): _description_

    Returns:
        dict: _description_
    """
    node = dict(
        data=elm,
        next=None
    )
    return node


def new_double_node(elm: object) -> dict:
    """new_double_node _summary_

    Args:
        elm (object): _description_

    Returns:
        dict: _description_
    """
    node = dict(
        data=elm,
        next=None,
        prev=None
    )
    return node


def get_element(node: dict) -> object:
    """get_element _summary_

    Args:
        node (dict): _description_

    Returns:
        object: _description_
    """
    return node.get("data")


def set_element(node: dict, elm: object) -> dict:
    """set_element _summary_

    Args:
        node (dict): _description_
        elm (object): _description_

    Returns:
        dict: _description_
    """
    node["data"] = elm
    return node
