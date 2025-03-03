# import python modules
import random as rd

# import modules for data structures index + bucket
from Src.Func.DataStructs.List import arlt     # as idx

# import error handler
from Src.Func.Utils.error import error_handler as err

# import map entry
from Src.Func.DataStructs.Tables import entry as me

# import prime number generator
from Src.Func.Utils import numbers as num


def default_mp_entry_cmp(key: object, entry: dict) -> int:
    if (key == entry['key']):
        return 0
    elif (key > entry['key']):
        return 1
    return -1


def new_probing_mp(n_elements: int = 17,
                   prime: int = 109345121,
                   load_factor: float = 0.5,
                   cmp_function=None) -> dict:
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
        )
        if cmp_function is None:
            new_table["cmp_function"] = default_mp_entry_cmp
        else:
            new_table["cmp_function"] = cmp_function
        new_table["table"] = arlt.new_array_lt(new_table["cmp_function"])
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


def find_slot(mp: dict, key: object, _hash: int) -> int:
    try:
        i = 0
    except Exception as exp:
        err("probing", "find_slot()", exp)


def rehash(mp: dict) -> None:
    try:
        old_table = mp["table"]
        old_capacity = mp["capacity"]
        mp["capacity"] = num.next_prime(mp["capacity"] * 2)
        mp["size"] = 0
        mp["cur_factor"] = 0
        mp["table"] = arlt.new_array_lt(mp["cmp_function"])
        i = 0
        while i < mp["capacity"]:
            entry = me.new_map_entry(None, None)
            arlt.add_last(mp["table"], entry)
            i += 1
        i = 0
        while i < old_capacity:
            entry = arlt.get_element(old_table, i)
            if entry.get("key") is not None:
                put(mp, entry.get("key"), entry.get("value"))
            i += 1
    except Exception as exp:
        err("probing", "rehash()", exp)
