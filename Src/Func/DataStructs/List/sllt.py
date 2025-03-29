# import python libs
from typing import Any
# import csv
# import project libs
from Src.Func.DataStructs.List import ltnode as node
# import project errors
from Src.Func.Utils.error import error_handler as err


def dflt_elm_cmp_lt(id1: Any, id2: Any) -> int:
    """dflt_elm_cmp_lt is the default comparison function for elements in the array list.

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


def new_list(cmp_function=None, key: str = "id") -> dict:
    """new_list creates a new single linked list.

    Args:
        cmp_function (_type_, optional): function to compare elements. Defaults to None, uses dflt_elm_cmp_lt.
        key (str, optional): key to compare elements in structure. Defaults to "id".

    Returns:
        dict: returns a new single linked list.
    """
    new_lt = dict(
        first=None,
        last=None,
        size=0,
        type="SINGLELINKED",
        cmp_function=cmp_function,
        key=key,
    )
    if cmp_function is None:
        new_lt["cmp_function"] = dflt_elm_cmp_lt
    else:
        new_lt["cmp_function"] = cmp_function
    new_lt["first"] = new_lt["last"]
    return new_lt


def is_empty(lt: dict) -> bool:
    """is_empty checks if the single linked list is empty.

    Args:
        lt (dict): single linked list to check.

    Returns:
        bool: returns True if the single linked list is empty, False otherwise.
    """
    try:
        return lt.get("size") == 0
    except Exception as e:
        err("singlelist", "is_empty()", e)


def size(lt: dict) -> int:
    """size returns the size of the single linked list.

    Args:
        lt (dict): single linked list to check.

    Returns:
        int: returns the size of the single linked list.
    """
    try:
        return lt.get("size")
    except Exception as e:
        err("singlelist", "size()", e)


def add_first(lt: dict, element: Any) -> None:
    """add_first adds an element to the first position of the single linked list.

    Args:
        lt (dict): single linked list to add the element.
        element (Any): element to add to the single linked list.
    """
    try:
        new_node = node.new_single_node(element)
        new_node["next"] = lt["first"]
        lt["first"] = new_node
        if lt.get("size") == 0:
            lt["last"] = lt["first"]
        lt["size"] += 1
    except Exception as e:
        err("singlelist", "add_first()", e)


def add_last(lt: dict, element: Any) -> None:
    """add_last adds an element to the last position of the single linked list.

    Args:
        lt (dict): single linked list to add the element.
        element (Any): element to add to the single linked list.
    """
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
    """add_element adds an element to the single linked list in the specified position.

    Args:
        lt (dict): single linked list to add the element.
        pos (int): position to add the element.
        element (Any): element to add to the single linked list.
    """
    try:
        new_node = node.new_single_node(element)
        if lt.get("size") == 0:
            lt["first"] = new_node
            lt["last"] = new_node
        elif lt.get("size") > 0 and pos == 0:
            new_node["next"] = lt["first"]
            lt["first"] = new_node
        else:
            cont = 0
            prev = lt["first"]
            cur = lt["first"]
            while cont < pos:
                prev = cur
                cur = cur["next"]
                cont += 1
            new_node["next"] = cur
            prev["next"] = new_node
        lt["size"] += 1
        return lt
    except Exception as e:
        err("singlelist", "add_element()", e)


def get_first(lt: dict) -> Any:
    """get_first returns the first element of the single linked list.

    Args:
        lt (dict): single linked list to get the first element.

    Returns:
        Any: returns the first element of the single linked list. None if the list is empty.
    """
    try:
        if lt.get("first") is not None:
            return lt["first"]["data"]
        return None
    except Exception as e:
        err("singlelist", "get_first()", e)


def get_last(lt: dict) -> Any:
    """get_last returns the last element of the single linked list.

    Args:
        lt (dict): single linked list to get the last element.

    Returns:
        Any: returns the last element of the single linked list. None if the list is empty.
    """
    try:
        if lt.get("last") is not None:
            return lt.get("last")["data"]
        return None
    except Exception as e:
        err("singlelist", "get_last()", e)


def get_element(lt: dict, pos: int) -> Any:
    """get_element returns the element in the specified position of the single linked list.

    Args:
        lt (dict): single linked list to get the element.
        pos (int): position to get the element.

    Returns:
        Any: returns the element in the specified position of the single linked list. None if the list is empty or the position is invalid.
    """
    try:
        idx = 0
        cur = lt.get("first")
        if pos < 0 or pos > lt.get("size") - 1:
            return None
        while idx < pos:
            cur = cur["next"]
            idx += 1
        return cur.get("data")
    except Exception as e:
        err("singlelist", "get_element()", e)


def remove_first(lt: dict) -> Any:
    """remove_first removes the first element of the single linked list.

    Args:
        lt (dict): single linked list to remove the first element.

    Returns:
        Any: returns the first element of the single linked list. None if the list is empty.
    """
    try:
        if lt.get("first") is not None:
            node = lt["first"]
            lt["first"] = node.get("next")
            lt["size"] -= 1
            if lt.get("size") == 0:
                lt["last"] = lt["first"]
            return lt
        return None
    except Exception as e:
        err("singlelist", "remove_first()", e)


def remove_last(lt: dict) -> Any:
    """remove_last removes the last element of the single linked list.

    Args:
        lt (dict): single linked list to remove the last element.

    Returns:
        Any: returns the last element of the single linked list. None if the list is empty.
    """
    try:
        if lt.get("last") is not None:
            if lt["first"] == lt.get("last"):
                lt["last"] = None
                lt["first"] = None
            else:
                cur = lt["first"]
                while cur.get("next") != lt.get("last"):
                    cur = cur["next"]
                lt["last"] = cur
                lt["last"]["next"] = None
            lt["size"] -= 1
            return lt
        return None
    except Exception as e:
        err("singlelist", "remove_last()", e)


def remove_element(lt: dict, pos: int) -> Any:
    """remove_element removes the element in the specified position of the single linked list.

    Args:
        lt (dict): single linked list to remove the element.
        pos (int): position to remove the element.

    Returns:
        Any: returns the element in the specified position of the single linked list. None if the list is empty or the position is invalid.
    """
    try:
        cur = lt["first"]
        prev = lt["first"]
        idx = 0
        if pos >= 0 and pos < lt.get("size"):
            if pos == 0:
                lt["first"] = cur["next"]
            elif pos > 0:
                while idx < pos:
                    idx += 1
                    prev = cur
                    cur = cur["next"]
                prev["next"] = cur["next"]
                if cur == lt.get("last"):
                    lt["last"] = prev
            lt["size"] -= 1
            return lt
        print("got to None in rmv element sllt")
        return None
    except Exception as e:
        err("singlelist", "remove_element()", e)


def update(lt: dict, pos: int, element: Any) -> None:
    """update updates the element in the specified position of the single linked list.

    Args:
        lt (dict): single linked list to update the element.
        pos (int): position to update the element.
        element (Any): element to update in the single linked list.
    """
    try:
        node = lt["first"]
        idx = 0
        while idx < pos:
            node = node.get("next")
            idx += 1
        node["data"] = element
    except Exception as e:
        err("singlelist", "update()", e)


def exchange(lt: dict, pos1: int, pos2: int) -> None:
    """exchange exchanges the elements in the specified positions of the single linked list.

    Args:
        lt (dict): single linked list to exchange the elements.
        pos1 (int): first position to exchange.
        pos2 (int): second position to exchange.
    """
    try:
        elm1 = get_element(lt, pos1)
        elm2 = get_element(lt, pos2)
        update(lt, pos2, elm1)
        update(lt, pos1, elm2)
    except Exception as e:
        err("singlelist", "exchange()", e)


def compare(lt: dict, elm1: Any, elm2: Any) -> bool:
    """compare compares two elements in the single linked list.

    Args:
        lt (dict): single linked list to compare the elements.
        elm1 (Any): first element to compare.
        elm2 (Any): second element to compare.

    Returns:
        bool: returns True if the elements are equal, False otherwise.
    """
    try:
        _cmp = lt.get("cmp_function")
        if lt.get("key") is not None:
            k = lt.get("key")
            return _cmp(elm1[k], elm2[k]) == 0
        else:
            return _cmp(elm1, elm2) == 0
    except Exception as e:
        err("singlelist", "compare()", e)


def find(lt: dict, element: Any) -> int:
    """find checks if an element is present in the single linked list.

    Args:
        lt (dict): single linked list to check.
        element (dict): element to check if is present in the array list.

    Returns:
        int: returns the position of the element in the array list if it is present, -1 otherwise.
    """
    try:
        found = False
        idx = -1
        i = 0
        while not found and i < lt.get("size"):
            cur = get_element(lt, i)
            if compare(lt, element, cur):
                found = True
                idx = i
            i += 1
        return idx
    except Exception as e:
        err("singlelist", "find()", e)


def sub_list(lt: dict, start: int, end: int) -> dict:
    """sub_list returns a sub list of the single linked list from the start position to the end position.

    Args:
        lt (dict): single linked list to get the sub list.
        start (int): start position of the sub list, inclusive, greater or equal to 0.
        end (int): end position of the sub list, exclusive, less than the size of the array list.

    Returns:
        dict: returns a sub list of the single linked list from the start to the end.
    """
    try:
        sub = new_list(lt.get("cmp_function"),
                       lt.get("key"))
        i = start
        while i < end:
            add_last(sub, get_element(lt, i))
            i += 1
        return sub
    except Exception as e:
        err("singlelist", "sub_list()", e)


def concat(lt1: dict, lt2: dict) -> dict:
    """concat concatenates two single linked lists.

    Args:
        lt1 (dict): first single linked list to concatenate.
        lt2 (dict): second single linked list to concatenate.

    Returns:
        dict: returns a new single linked list with the concatenation of the two single linked lists.
    """
    try:
        new_lt = new_list(lt1.get("cmp_function"), lt1.get("key"))
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


def clone(lt: dict) -> dict:
    """clone clones a single linked list. We don't name the function as copy to avoid confusion with the python copy module.

    Args:
        lt (dict): single linked list to clone.

    Returns:
        dict: cloned single linked list.
    """
    try:
        new_lt = new_list(lt.get("cmp_function"),
                          lt.get("key"))
        for elm in iterator(lt):
            add_last(new_lt, elm)
        return new_lt
    except Exception as exp:
        err("arraylist", "clone()", exp)


def iterator(lt: dict) -> object:
    """iterator returns an iterator for the single linked list.

    Args:
        lt (dict): single linked list to iterate.

    Returns:
        object: returns an iterator for the single linked list.

    Yields:
        Iterator[object]: returns the next element in the single linked list.
    """
    try:
        cur = lt["first"]
        while cur is not None:
            yield cur.get("data")
            cur = cur["next"]
    except Exception as e:
        err("singlelist", "iterator()", e)
