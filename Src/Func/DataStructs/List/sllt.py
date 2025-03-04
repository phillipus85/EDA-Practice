# import python libs
from typing import Any
# import csv
# import project libs
from Src.Func.DataStructs.List import ltnode as node
# import project errors
from Src.Func.Utils.error import error_handler as err


"""
Module to handle a single linked list sll data structure.
This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


def default_lt_elm_cmp(id1: Any, id2: Any) -> int:
    """default_lt_elm_cmp is the default comparison function for elements in the array list.

    Args:
        id1 (Any): first element to compare.
        id2 (Nay): second element to compare.

    Returns:
        int: returns 1 if id1 > id2, -1 if id1 < id2, 0 if id1 == id2
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0


def new_single_lt(cmp_function=None, key: str = "id") -> dict:
    new_lt = dict(
        first=None,
        last=None,
        size=0,
        type="SINGLELINKED",
        cmp_function=default_lt_elm_cmp,
        key=key,
    )
    if cmp_function is None:
        new_lt["cmp_function"] = default_lt_elm_cmp
    else:
        new_lt["cmp_function"] = cmp_function
    new_lt["first"] = new_lt["last"]
    return new_lt


def is_empty(lt: dict) -> bool:
    try:
        return lt.get("size") == 0
    except Exception as e:
        err("singlelist", "is_empty()", e)


def size(lt: dict) -> int:
    try:
        return lt.get("size")
    except Exception as e:
        err("singlelist", "size()", e)


def add_first(lt: dict, element: Any) -> None:
    try:
        new_node = node.new_single_node(element)
        new_node["next"] = lt.get("first")
        lt["first"] = new_node
        if lt.get("size") == 0:
            lt["last"] = lt["first"]
        lt["size"] += 1
    except Exception as e:
        err("singlelist", "add_first()", e)


def add_last(lt: dict, element: Any) -> None:
    try:
        new_node = node.new_single_node(element)
        if lt.get("size") == 0:
            lt["first"] = new_node
        else:
            lt["last"]["next"] = new_node
        lt["last"] = new_node
        lt["size"] += 1
    except Exception as e:
        err("singlelist", "add_last()", e)


def add_element(lt: dict, pos: int, element: Any) -> None:
    try:
        new_node = node.new_single_node(element)
        if lt.get("size") == 0:
            lt["first"] = new_node
            lt["last"] = new_node
        elif lt.get("size") > 0 and pos == 0:
            new_node["next"] = lt.get("first")
            lt["first"] = new_node
        else:
            cont = 0
            prev = lt.get("first")
            cur = lt.get("first")
            while cont < pos:
                prev = cur
                cur = cur.get("next")
                cont += 1
            new_node["next"] = cur
            prev["next"] = new_node
        lt["size"] += 1
    except Exception as e:
        err("singlelist", "add_element()", e)


def get_first(lt: dict) -> Any:
    try:
        if lt.get("first") is not None:
            return lt.get("first")["data"]
        return None
    except Exception as e:
        err("singlelist", "get_first()", e)


def get_last(lt: dict) -> Any:
    try:
        if lt.get("last") is not None:
            return lt.get("last")["data"]
        return None
    except Exception as e:
        err("singlelist", "get_last()", e)


def get_element(lt: dict, pos: int) -> Any:
    try:
        idx = 0
        cur = lt.get("first")
        if pos < 0 or pos >= lt.get("size"):
            return None
        while idx < pos:
            cur = cur.get("next")
            idx += 1
        return cur.get("data")
    except Exception as e:
        err("singlelist", "get_element()", e)


def remove_first(lt: dict) -> Any:
    try:
        if lt.get("first") is not None:
            node = lt.get("first")
            lt["first"] = node.get("next")
            lt["size"] -= 1
            if lt.get("size") == 0:
                lt["last"] = lt["first"]
            return node.get("data")
        return None
    except Exception as e:
        err("singlelist", "remove_first()", e)


def remove_last(lt: dict) -> Any:
    try:
        if lt.get("last") is not None:
            if lt.get("first") == lt.get("last"):
                node = lt.get("first")
                lt["last"] = None
                lt["first"] = None
            else:
                cur = lt.get("first")
                while cur.get("next") != lt.get("last"):
                    cur = cur.get("next")
                node = lt.get("last")
                lt["last"] = cur
                lt["last"]["next"] = None
            lt["size"] -= 1
            return node.get("data")
        return None
    except Exception as e:
        err("singlelist", "remove_last()", e)


def remove_element(lt: dict, pos: int) -> Any:
    try:
        cur = lt.get("first")
        prev = lt.get("first")
        idx = 0
        node = None
        if pos < 0 or pos >= lt.get("size"):
            if pos == 0:
                lt["first"] = cur.get("next")
                lt["size"] -= 1
            elif pos > 0:
                while idx < pos:
                    idx += 1
                    prev = node
                    node = node.get("next")
                prev["next"] = node.get("next")
                lt["size"] -= 1
            return node.get("data")
        return None
    except Exception as e:
        err("singlelist", "remove_element()", e)


def update(lt: dict, pos: int, element: Any) -> None:
    try:
        node = lt.get("first")
        idx = 0
        while idx < pos:
            node = node.get("next")
            idx += 1
        node["data"] = element
    except Exception as e:
        err("singlelist", "update()", e)


def exchange(lt: dict, pos1: int, pos2: int) -> None:
    try:
        elm1 = get_element(lt, pos1)
        elm2 = get_element(lt, pos2)
        update(lt, pos2, elm1)
        update(lt, pos1, elm2)
    except Exception as e:
        err("singlelist", "exchange()", e)


def cmp_elements(lt: dict, elm1: Any, elm2: Any) -> bool:
    try:
        _cmp = lt.get("cmp_function")
        if lt.get("key") is not None:
            k = lt.get("key")
            return _cmp(elm1[k], elm2[k]) == 0
        else:
            return _cmp(elm1, elm2) == 0
    except Exception as e:
        err("singlelist", "cmp_elements()", e)


def is_present(lt: dict, element: Any) -> int:
    try:
        found = False
        idx = -1
        i = 0
        while not found and i < lt.get("size"):
            cur = get_element(lt, i)
            if cmp_elements(lt, element, cur):
                found = True
                idx = i
            i += 1
        return idx
    except Exception as e:
        err("singlelist", "is_present()", e)


def sub_list(lt: dict, start: int, end: int) -> dict:
    try:
        sub = new_single_lt(lt.get("cmp_function"), lt.get("key"))
        i = 0
        while i < lt.get("size"):
            if i >= start and i < end + 1:
                add_last(sub, get_element(lt, i))
            i += 1
        return sub
    except Exception as e:
        err("singlelist", "sub_list()", e)


def iterator(lt: dict) -> object:
    try:
        cur = lt.get("first")
        while cur is not None:
            yield cur.get("data")
            cur = cur.get("next")
    except Exception as e:
        err("singlelist", "iterator()", e)


def concat(lt1: dict, lt2: dict) -> dict:
    try:
        new_lt = new_single_lt(lt1.get("cmp_function"), lt1.get("key"))
        i = 0
        while i < lt1.get("size"):
            add_last(new_lt, get_element(lt1, i))
            i += 1
        i = 0
        while i < lt2.get("size"):
            add_last(new_lt, get_element(lt2, i))
            i += 1
        return new_lt
    except Exception as e:
        err("singlelist", "concat()", e)
