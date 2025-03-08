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
    if (key == entry["key"]):
        return 0
    elif (key > entry["key"]):
        return 1
    return -1


def new_probing_mp(entries: int = 17,
                   prime: int = 109345121,
                   alpha: float = 0.5,
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


def put(mp: dict, key: Any, value: Any) -> None:
    try:
        entry = me.new_map_entry(key, value)
        _idx = num.hash_compress(key,
                                 mp["scale"],
                                 mp["shift"],
                                 mp["prime"],
                                 mp["capacity"])
        slot = find_slot(mp, key, _idx)
        print(f"put-k: {key}, slot: {slot}")
        # arlt.update(mp["table"], slot, entry)
        arlt.update(mp["table"], abs(slot), entry)
        if slot < 0:
            mp["size"] += 1
            mp["cur_alpha"] = mp["size"] / mp["capacity"]

        if mp["cur_alpha"] >= mp["max_alpha"]:
            rehash(mp)
        # return mp
    except Exception as exp:
        err("probing", "put()", exp)


def get(mp: dict, key: Any) -> dict:
    try:
        entry = None
        _idx = num.hash_compress(key,
                                 mp["scale"],
                                 mp["shift"],
                                 mp["prime"],
                                 mp["capacity"])
        _slot = find_slot(mp, key, _idx)
        print(f"get-k: {key}, slot: {_slot}")
        if _slot > 0:
            entry = arlt.get_element(mp["table"], _slot)
        return entry
    except Exception as exp:
        err("probing", "get()", exp)


def remove(mp: dict, key: Any) -> dict:
    try:
        _idx = num.hash_compress(key,
                                 mp["scale"],
                                 mp["shift"],
                                 mp["prime"],
                                 mp["capacity"])
        _slot = find_slot(mp, key, _idx, mp["cmp_function"])
        if _slot > -1:
            dummy = me.new_map_entry("__EMPTY__", "__EMPTY__")
            arlt.update(mp["table"], _slot, dummy)
            mp["size"] -= 1
        return mp
    except Exception as exp:
        err("probing", "remove()", exp)


def contains(mp: dict, key: Any) -> bool:
    try:
        _idx = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        _slot = find_slot(mp, key, _idx, mp["cmp_function"])
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
            if entry["value"] not in (None, "__EMPTY__"):
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
        if mp["rehashable"] is True:
            _new_capacity = num.next_prime(mp["capacity"] * 2)
            _new_table = arlt.new_array_lt(mp["cmp_function"], mp["key"])
            i = 0
            while i < _new_capacity:
                entry = me.new_map_entry(None, None)
                arlt.add_last(_new_table, entry)
                i += 1
            mp["capacity"] = _new_capacity
            mp["table"] = _new_table
            _idx = 0
            while _idx < arlt.size(mp["table"]):
                entry = arlt.get_element(mp["table"], _idx)
                if entry["key"] not in (None, "__EMPTY__"):
                    _idx = num.hash_compress(entry["key"],
                                            mp["scale"],
                                            mp["shift"],
                                            mp["prime"],
                                            _new_capacity)
                    _slot = find_slot(mp, entry["key"], _idx, mp["cmp_function"])
                    arlt.update(_new_table, abs(_slot), entry)
                _idx += 1
        return mp
    except Exception as exp:
        err("probing", "rehash()", exp)


def is_available(table: dict, _slot: int) -> bool:
    try:
        entry = arlt.get_element(table, _slot)
        if entry["key"] is None or entry["key"] == "__EMPTY__":
            return True
        return False
    except Exception as exp:
        err("probing", "is_available()", exp)


def find_slot(mp: dict, key: Any, _idx: int) -> int:
    try:
        _table = mp["table"]
        _cmp = mp["cmp_function"]
        _slot = 0
        _available_slot = -1
        while _slot != _idx:
            if _slot == 0:
                _slot = _idx
            if _slot == -1:
                _slot = 0
            if is_available(_table, _slot):
                entry = arlt.get_element(_table, _slot)
                if _available_slot == -1:
                    _available_slot = _slot
                if entry["key"] is None:
                    break
            else:
                entry = arlt.get_element(_table, _slot)
                print(f"k: {key}, entry: {entry}, idx: {_idx}, slot: {_slot}")
                if _cmp(key, entry) == 0:
                    return _slot
            
            if _slot == (mp["capacity"] - 1):
                _slot = -1
            else:
                _slot = ((_slot% mp["capacity"]) + 1)
        
                
        return -(_available_slot)
    except Exception as exp:
        err("probing", "new_find_slot()", exp)


# def find_slot(mp: dict, key: Any, _idx: int, cmp_function: Any) -> int:
#     try:
#         _slot = 0
#         _available_slot = -1
#         hash_table = mp["table"]

#         while _slot != _idx:
#             if _slot == 0:
#                 _slot = _idx
#             if is_available(hash_table, _slot):
#                 entry = arlt.get_element(hash_table, _slot)
#                 if _available_slot == -1:
#                     _available_slot = _slot
#                 if entry["key"] is None:
#                     # _available_slot = _slot
#                     break
#             else:
#                 entry = arlt.get_element(hash_table, _slot)
#                 # print(cmp_function(key, entry))
#                 if cmp_function(key, entry) == 0:
#                     return _slot
#             # print("round probing!!!", _slot)
#             _slot = _slot % mp["capacity"] + 1

#         return -(_available_slot)

        # avail = -1          # no se ha encontrado una posición aun
        # _slot = 0
        # table = mp["table"]
        # while (_slot != _idx):  # Se busca una posición
        #     if (_slot == 0):
        #         _slot = _idx
        #     if is_available(table, _slot):  # La posición esta disponible
        #         element = arlt.get_element(table, _slot)
        #         if avail == -1:
        #             avail = _slot            # primera posición disponible
        #         if element["key"] is None:       # nunca ha sido utilizada
        #             break
        #     else:                    # la posicion no estaba disponible
        #         element = arlt.get_element(table, _slot)
        #         if cmp_function(key, element) == 0:  # Es la llave
        #             print("find_slot", _slot)
        #             return _slot               # Se  retorna la posicion
        #     _slot = (((_slot) % mp["capacity"]) + 1)
        # return -(avail)    # numero negativo indica que el elemento no estaba
        
        # _max_probes = mp["capacity"]
        # found = False
        # available = False
        # pc = 0
        # j = -1
        # idx = -1
        # i = _idx
        # while not (found or available) and pc < _max_probes:
        #     entry = arlt.get_element(mp["table"], i)
        #     if is_available(mp["table"], i):
        #         if idx == -1:
        #             idx = i
        #         if entry["key"] is None:
        #             available = True
        #     else:
        #         if cmp_function(key, entry) == 0:
        #             j = i
        #             found = True
        #     i = int(i % mp["capacity"]) + 1
        #     if i >= mp["capacity"]:
        #         i = 0
        #     pc += 1
        # if found:
        #     return j
        # elif available:
        #     return idx
        # else:
        #     return _max_probes + 1

        # available = -1
        # _pos = 0
        # hash_table = mp["table"]
        # while _pos != _idx:
        #     if _pos == 0:
        #         _pos = _idx
        #     if is_available(hash_table, _pos):
        #         elm = arlt.get_element(hash_table, _pos)
        #         if available == -1:
        #             available = _pos
        #         if elm["key"] is None:
        #             break
        #     else:
        #         elm = arlt.get_element(hash_table, _pos)
        #         if cmp_function(key, elm) == 0:
        #             return _pos
        #     _pos = (((_pos) % mp["capacity"]) + 1)
        # return -(available)
    # except Exception as exp:
    #     err("probing", "find_slot()", exp)
