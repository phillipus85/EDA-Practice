# import python modules
import random as rd
from typing import Any

# import modules for data structures index + bucket
from Src.Func.DataStructs.List import arlt     # as idx
from Src.Func.DataStructs.List import sllt     # as bucket

# import error handler
from Src.Func.Utils.error import error_handler as err

# import map entry
from Src.Func.DataStructs.Tables import entry as me

# import prime number generator
from Src.Func.Utils import numbers as num


def default_mp_entry_cmp(key: Any, entry: Any) -> int:
    if (key == entry['key']):
        return 0
    elif (key > entry['key']):
        return 1
    return -1


def new_probing_mp(n_elements: int = 17,
                   prime: int = 109345121,
                   load_factor: float = 0.5,
                   cmp_function=None,
                   key: str = "id") -> dict:
    try:
        capacity = num.next_prime(n_elements // load_factor)
        scale = rd.randint(1, prime - 1)
        shift = rd.randint(0, prime - 1)
        new_table = dict(
            n_elements=n_elements,
            prime=prime,
            limit_factor=load_factor,
            cur_factor=0,
            capacity=capacity,
            scale=scale,
            shift=shift,
            table=None,
            size=0,
            type="LINEAR_PROBING",
            cmp_function=None,
            key=key
        )
        if cmp_function is None:
            new_table["cmp_function"] = default_mp_entry_cmp
        else:
            new_table["cmp_function"] = cmp_function
        new_table["table"] = arlt.new_array_lt(new_table["cmp_function"],
                                               new_table["key"])
        i = 0
        while i < capacity:
            entry = me.new_map_entry(None, None)
            arlt.add_last(new_table["table"], entry)
            i += 1
        return new_table
    except Exception as exp:
        err("probing", "new_map()", exp)


def put(mp: dict, key: object, value: object) -> dict:
    try:
        _hash = num.hash_compress(key,
                                  mp['prime'],
                                  mp['scale'],
                                  mp['shift'],
                                  mp['capacity'])
        entry = me.new_map_entry(key, value)
        idx = find_slot(mp, key, _hash)
        arlt.update(mp['table'], abs(idx), entry)
        if idx < 0:
            mp["size"] += 1
            mp["cur_factor"] = mp["size"] / mp["capacity"]
        if mp["cur_factor"] > mp["limit_factor"]:
            rehash(mp)
        return mp
    except Exception as exp:
        err("probing", "put()", exp)


def get(mp: dict, key: Any) -> dict:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        _slot = find_slot(mp, key, _hash, mp["cmp_function"])
        if _slot > -1:
            entry = arlt.get_element(mp["table"], _slot)
            return entry
        return None
    except Exception as exp:
        err("probing", "get()", exp)


def remove(mp: dict, key: Any) -> dict:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        _slot = find_slot(mp, key, _hash, mp["cmp_function"])
        if _slot > -1:
            dummy = me.new_map_entry("__EMPTY__", None)
            arlt.update(mp["table"], _slot, dummy)
            mp["size"] -= 1
        return mp
    except Exception as exp:
        err("probing", "remove()", exp)


def contains(mp: dict, key: Any) -> bool:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        _slot = find_slot(mp, key, _hash, mp["cmp_function"])
        if _slot > -1:
            return True
        return False
    except Exception as exp:
        err("probing", "contains()", exp)


def size(mp: dict) -> int:
    return mp.get("size")


def is_empty(mp: dict) -> bool:
    try:
        empty = True
        _idx = 0
        while _idx < arlt.size(mp["table"]) and empty:
            entry = arlt.get_element(mp["table"], _idx)
            # if entry["key"] is not None and entry["key"] != "__EMPTY__":
            if entry["key"] not in (None, "__EMPTY__"):
                empty = False
            _idx += 1
        return empty
    except Exception as exp:
        err("chaining", "is_empty()", exp)


def keys(mp: dict) -> dict:
    try:
        keys_lt = sllt.new_single_lt(cmp_function=mp["cmp_function"],
                                     key=mp["key"])
        _idx = 0
        while _idx < arlt.size(mp["table"]):
            entry = arlt.get_element(mp["table"], _idx)
            # if entry["key"] is not None and entry["key"] != "__EMPTY__":
            if entry["key"] not in (None, "__EMPTY__"):
                sllt.add_last(keys_lt, entry["key"])
            _idx += 1
        return keys_lt
    except Exception as exp:
        err("chaining", "keys()", exp)


def values(mp: dict) -> dict:
    try:
        values_lt = sllt.new_single_lt(cmp_function=mp["cmp_function"],
                                       key=mp["key"])
        _idx = 0
        while _idx < arlt.size(mp["table"]):
            entry = arlt.get_element(mp["table"], _idx)
            # if entry["key"] is not None and entry["key"] != "__EMPTY__":
            if entry["key"] not in (None, "__EMPTY__"):
                sllt.add_last(values_lt, entry["value"])
            _idx += 1
        return values_lt
    except Exception as exp:
        err("chaining", "values()", exp)


######################################
#       Important Functions          #
######################################


def rehash(mp: dict) -> None:
    try:
        return mp
    except Exception as exp:
        err("probing", "rehash()", exp)


def is_available(mp: dict, slot: int) -> bool:
    try:
        entry = arlt.get_element(mp["table"], slot)
        if entry["key"] is None or entry["key"] == "__EMPTY__":
            return True
        return False
    except Exception as exp:
        err("probing", "is_available()", exp)


def find_slot(mp: dict, key: Any, _hash: int, cmp_function: Any) -> int:
    try:
        available = -1
        _pos = 0
        hash_table = mp["table"]
        while _pos != _hash:
            if _pos == 0:
                _pos = _hash
            if is_available(mp, _pos):
                elm = arlt.get_element(hash_table, _pos)
                if available == -1:
                    available = _pos
                if elm["key"] is None:
                    break
            else:
                elm = arlt.get_element(hash_table, _pos)
                if cmp_function(key, elm) == 0:
                    return _pos
            _pos = (_pos + 1) % mp["capacity"]
        return -(available)
    except Exception as exp:
        err("probing", "find_slot()", exp)
