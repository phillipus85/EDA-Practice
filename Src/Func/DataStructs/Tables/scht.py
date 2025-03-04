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


def new_chaining_mp(entries: int = 17,
                    prime: int = 109345121,
                    alpha: float = 4.0,
                    cmp_function=None,
                    key: str = None,
                    rehashable: bool = True) -> dict:
    try:
        capacity = num.next_prime(entries // alpha)
        scale = rd.randint(1, prime - 1)
        shift = rd.randint(0, prime - 1)
        new_table = dict(
            entries=entries,
            prime=prime,
            max_alpha=alpha,
            cur_alpha=0,
            capacity=capacity,
            scale=scale,
            shift=shift,
            table=None,
            rehashable=rehashable,
            size=0,
            type="SEPARATE_CHAINING",
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
            bucket = sllt.new_single_lt(new_table["cmp_function"],
                                        new_table["key"])
            arlt.add_last(new_table["table"], bucket)
            i += 1
        return new_table
    except Exception as exp:
        err("chaining", "new_map()", exp)


def put(mp: dict, key: Any, value: Any) -> None:
    try:
        entry = me.new_map_entry(key, value)
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        bucket = arlt.get_element(mp["table"], _hash)
        _idx = sllt.is_present(bucket, key)
        if _idx > -1:
            sllt.update(bucket, _idx, entry)
        else:
            sllt.add_last(bucket, entry)
            mp["size"] += 1
            mp["cur_alpha"] = mp["size"] / mp["capacity"]

        if mp["cur_alpha"] >= mp["max_alpha"]:
            rehash(mp)
        # return mp
    except Exception as exp:
        err("chaining", "put()", exp)


def get(mp: dict, key: Any) -> dict:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        bucket = arlt.get_element(mp["table"], _hash)
        _idx = sllt.is_present(bucket, key)
        if _idx > -1:
            return sllt.get_element(bucket, _idx)
        return None
    except Exception as exp:
        err("chaining", "get()", exp)


def remove(mp: dict, key: Any) -> dict:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        bucket = arlt.get_element(mp["table"], _hash)
        if bucket is not None:
            _idx = sllt.is_present(bucket, key)
            if _idx > -1:
                sllt.remove_element(bucket, _idx)
                mp["size"] -= 1
                mp["cur_alpha"] = mp["size"] / mp["capacity"]
        return mp
    except Exception as exp:
        err("chaining", "remove()", exp)


def contains(mp: dict, key: Any) -> bool:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        bucket = arlt.get_element(mp["table"], _hash)
        _idx = sllt.is_present(bucket, key)
        if _idx > -1:
            return True
        return False
    except Exception as exp:
        err("chaining", "contains()", exp)


def size(mp: dict) -> int:
    return mp.get("size")


def is_empty(mp: dict) -> bool:
    try:
        bucket = None
        empty = True
        _idx = 0
        while _idx < arlt.size(mp["table"]) and empty:
            bucket = arlt.get_element(mp["table"], _idx)
            if not sllt.is_empty(bucket):
                empty = False
            _idx += 1
        return empty
    except Exception as exp:
        err("chaining", "is_empty()", exp)


def keys(mp: dict) -> dict:
    try:
        keys_lt = sllt.new_single_lt(cmp_function=mp["cmp_function"],
                                     key=mp["key"])
        bucket = None
        _idx = 0
        while _idx < arlt.size(mp["table"]):
            bucket = arlt.get_element(mp["table"], _idx)
            if not sllt.is_empty(bucket):
                pos = 0
                while pos < sllt.size(bucket):
                    entry = sllt.get_element(bucket, pos)
                    sllt.add_last(keys_lt, entry["key"])
                    pos += 1
            _idx += 1
        return keys_lt
    except Exception as exp:
        err("chaining", "keys()", exp)


def values(mp: dict) -> dict:
    try:
        values_lt = sllt.new_single_lt(cmp_function=mp["cmp_function"],
                                       key=mp["key"])
        bucket = None
        _idx = 0
        while _idx < arlt.size(mp["table"]):
            bucket = arlt.get_element(mp["table"], _idx)
            if not sllt.is_empty(bucket):
                pos = 0
                while pos < sllt.size(bucket):
                    entry = sllt.get_element(bucket, pos)
                    sllt.add_last(values_lt, entry["value"])
                    pos += 1
            _idx += 1
        return values_lt
    except Exception as exp:
        err("chaining", "values()", exp)


######################################
#       Important Functions          #
######################################


def rehash(mp: dict) -> dict:
    try:
        if mp["rehashable"] is True:
            _new_cap = num.next_prime(mp["capacity"] * 2)
            mp["size"] = 0
            mp["cur_alpha"] = 0
            mp["capacity"] = _new_cap
            _new_table = arlt.new_array_lt(mp["cmp_function"],
                                           mp["key"])
            _old_table = mp["table"]
            _idx = 0
            while _idx < _new_cap:
                bucket = sllt.new_single_lt(mp["cmp_function"],
                                            mp["key"])
                arlt.add_last(_new_table, bucket)
                _idx += 1
            mp["table"] = _new_table
            _idx = 0
            while _idx < arlt.size(_old_table):
                bucket = arlt.get_element(_old_table, _idx)
                if not sllt.is_empty(bucket):
                    pos = 0
                    while pos < sllt.size(bucket):
                        entry = sllt.get_element(bucket, pos)
                        put(mp, entry["key"], entry["value"])
                        pos += 1
                _idx += 1
        return mp
    except Exception as exp:
        err("chaining", "rehash()", exp)
