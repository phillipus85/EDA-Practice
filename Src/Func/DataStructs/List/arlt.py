# import python libs
from typing import Any
# import csv
# import project libs
# from Src.Func.DataStructs.List import arl
# import project errors
from Src.Func.Utils.error import error_handler as err


"""
Module to handle a dynamic array or ADT array list functionally.
This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


def default_lt_elm_cmp(id1: Any, id2: Any) -> int:
    """default_lt_elm_cmp is the default comparison function for elements in the array list.

    Args:
        id1 (Any): first element to compare.
        id2 (Any): second element to compare.

    Returns:
        int: returns 1 if id1 > id2, -1 if id1 < id2, 0 if id1 == id2
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0


def new_array_lt(cmp_function=None, key: str = "id") -> dict:
    """new_array_lt _summary_

    Args:
        cmp_function (func, optional): function to compare elements. Defaults to None, uses default_lt_elm_cmp.
        key (str, optional): key to compare elements in structure. Defaults to "id".

    Returns:
        dict: _description_
    """
    new_lt = dict(
        elements=[],
        size=0,
        type="ARRAYLIST",
        cmp_function=cmp_function,
        key=key,
    )
    if new_lt["cmp_function"] is None:
        new_lt["cmp_function"] = default_lt_elm_cmp
    else:
        new_lt["cmp_function"] = cmp_function
    return new_lt


def is_empty(lt: dict) -> bool:
    """is_empty checks if the array list is empty.

    Args:
        lt (dict): array list to check.

    Returns:
        bool: returns True if the array list is empty, False otherwise.
    """
    try:
        return lt.get("size") == 0
    except Exception as exp:
        err("arraylist", "is_empty()", exp)


def size(lt: dict) -> int:
    """size returns the number of elements in the array list.

    Args:
        lt (dict): array list to check.

    Returns:
        int: returns the number of elements in the array list.
    """
    try:
        return lt.get("size")
    except Exception as exp:
        err("arraylist", "size()", exp)


def add_first(lt: dict, element: Any) -> None:
    """add_first adds an element to the first position of the array list.

    Args:
        lt (dict): array list to add the element.
        element (Any): element to add to the array list.
    """
    try:
        lt.get("elements").insert(0, element)
        lt["size"] += 1
    except Exception as exp:
        err("arraylist", "add_first()", exp)


def add_last(lt: dict, element: Any) -> None:
    """add_last adds an element to the last position of the array list.

    Args:
        lt (dict): array list to add the element.
        element (Any): element to add to the array list.
    """
    try:
        lt.get("elements").append(element)
        lt["size"] += 1
    except Exception as exp:
        err("arraylist", "add_last()", exp)


def add_element(lt: dict, pos: int, element: Any) -> None:
    """add_element adds an element to a specific position in the array list.

    Args:
        lt (dict): array list to add the element.
        pos (int): position to add the element.
        element (Any): element to add to the array list.
    """
    try:
        lt.get("elements").insert(pos, element)
        lt["size"] += 1
    except Exception as exp:
        err("arraylist", "add_element()", exp)


def get_first(lt: dict) -> Any:
    """get_first returns the first element in the array list.

    Args:
        lt (dict): array list to get the first element.

    Returns:

        Any: returns the first element in the array list.
    """
    try:
        if lt.get("size") > 0:
            return lt.get("elements")[0]
        return None
    except Exception as exp:
        err("arraylist", "get_first()", exp)


def get_last(lt: dict) -> Any:
    """get_last returns the last element in the array list.

    Args:
        lt (dict): array list to get the last element.

    Returns:
        Any: returns the last element in the array list.
    """
    try:
        if lt.get("size") > 0:
            return lt.get("elements")[lt.get("size") - 1]
        return None
    except Exception as exp:
        err("arraylist", "get_last()", exp)


def get_element(lt: dict, pos: int) -> Any:
    """get_element returns the element in a specific position in the array list.

    Args:
        lt (dict): array list to get the element.
        pos (int): position to get the element.

    Returns:
        Any: returns the element in the specific position of the array list.
    """
    try:
        if pos < 0 or pos >= lt.get("size"):
            return None
        return lt.get("elements")[pos]
    except Exception as exp:
        err("arraylist", "get_element()", exp)


def remove_first(lt: dict) -> Any:
    """remove_first removes the first element in the array list.

    Args:
        lt (dict): array list to remove the first element.

    Returns:
        Any: returns the array list without the first element.
    """
    try:
        if lt.get("size") == 0:
            return None
        elm = lt.get("elements").pop(0)
        lt["size"] -= 1
        return elm
    except Exception as exp:
        err("arraylist", "remove_first()", exp)


def remove_last(lt: dict) -> Any:
    """remove_last removes the last element in the array list.

    Args:
        lt (dict): array list to remove the last element.

    Returns:
        Any: returns the array list without the last element.
    """
    try:
        if lt.get("size") == 0:
            return None
        elm = lt.get("elements").pop(lt.get("size") - 1)
        lt["size"] -= 1
        return elm
    except Exception as exp:
        err("arraylist", "remove_last()", exp)


def remove_element(lt: dict, pos: int) -> Any:
    """remove_element removes an element in a specific position in the array list.

    Args:
        lt (dict): array list to remove the element.
        pos (int): position to remove the element.

    Returns:
        Any: returns the array list without the element in the specific position.
    """
    try:
        if pos < 0 or pos >= lt.get("size"):
            return None
        elm = lt.get("elements").pop(pos)
        lt["size"] -= 1
        return elm
    except Exception as exp:
        err("arraylist", "remove_element()", exp)


def update(lt: dict, pos: int, element: Any) -> None:
    """update updates an element in a specific position in the array list.

    Args:
        lt (dict): array list to update the element.
        pos (int): position to update the element.
        element (Any): element to update in the array list.
    """
    try:
        lt["elements"][pos] = element
        # lt.get("elements")[pos] = element
    except Exception as exp:
        err("arraylist", "update()", exp)


def exchange(lt: dict, pos1: int, pos2: int) -> None:
    """exchange exchanges two elements in the array list.

    Args:
        lt (dict): array list to exchange the elements.
        pos1 (int): first position to exchange.
        pos2 (int): second position to exchange.
    """
    try:
        elm1 = get_element(lt, pos1)
        elm2 = get_element(lt, pos2)
        update(lt, pos1, elm2)
        update(lt, pos2, elm1)
    except Exception as exp:
        err("arraylist", "exchange()", exp)


def cmp_elements(lt: dict, elm1: Any, elm2: Any) -> bool:
    """cmp_elements compares two elements in the array list.

    Args:
        lt (dict): array list to compare the elements.
        elm1 (Any): first element to compare.
        elm2 (Any): second element to compare.

    Returns:
        bool: returns True if the elements are equal, False otherwise.
    """
    try:
        _cmp = lt.get("cmp_function")
        if lt.get("key") is not None:
            k = lt.get("key")
            return _cmp(elm1.get(k), elm2.get(k)) == 0
        else:
            return _cmp(elm1, elm2) == 0
    except Exception as exp:
        err("arraylist", "cmp_elements()", exp)


def is_present(lt: dict, element: Any) -> int:
    """is_present checks if an element is present in the array list.

    Args:
        lt (dict): array list to check.
        element (dict): element to check if is present in the array list.

    Returns:
        int: returns the position of the element in the array list if it is present, -1 otherwise.
    """
    try:
        found = False
        idx = -1
        i = 0
        while not found and idx < lt.get("size"):
            temp = get_element(lt, i)
            if cmp_elements(lt, element, temp) is True:
                found = True
                idx = i
            idx += 1
        return idx
    except Exception as exp:
        err("arraylist", "is_present()", exp)


def sub_list(lt: dict, start: int, end: int) -> dict:
    """sub_list returns a sub list of the array list from start to end.

    Args:
        lt (dict): array list to get the sub list.
        start (int): start position of the sub list, inclusive, greater or equal to 0.
        end (int): end position of the sub list, exclusive, less than the size of the array list.

    Returns:
        dict: returns a new sub list from start to end
    """
    try:
        sub_lt = new_array_lt(lt.get("cmp_function"), lt.get("key"))
        i = 0
        while i < lt.get("size") - 1:
            if i >= start and i < end + 1:
                add_last(sub_lt, get_element(lt, i))
            i += 1
        return sub_lt
    except Exception as exp:
        err("arraylist", "sub_list()", exp)


def iterator(lt: dict) -> object:
    """iterator returns an iterator for the array list.

    Args:
        lt (dict): array list to iterate.

    Yields:
        arraylist: returns the elements in the array list.
    """
    try:
        for pos in range(0, lt.get("size")):
            yield lt.get("elements")[pos]
    except Exception as exp:
        err("arraylist", "iterator()", exp)


def concat(lt1: dict, lt2: dict) -> dict:
    """concat concatenates two array lists.

    Args:
        lt1 (dict): first array list to concatenate.
        lt2 (dict): second array list to concatenate.

    Returns:
        dict: returns a new array list with the elements of lt1 and lt2.
    """
    try:
        new_lt = new_array_lt(lt1.get("cmp_function"), lt1.get("key"))
        _elements = lt1.get("elements") + lt2.get("elements")
        new_lt.update({"elements": _elements})
        new_lt.update({"size": len(_elements)})
        return new_lt
    except Exception as exp:
        err("arraylist", "concat()", exp)
