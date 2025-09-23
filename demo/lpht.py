# demo for implementing minimal linear probing hash table

# import python libraries

# import dataclasses
from dataclasses import dataclass, field
# import typing
from typing import Any, List, Optional, Callable
# random
import random as rd

# import math stuff
import numbers


# create a dataclass for the hash table entry
@dataclass
class MapEntry:
    """ _summary_
    """
    key: Any
    value: Any
    used: bool = False  # To handle deleted entries


# create a dataclass for the linear probing hash table
@dataclass
class LinearProbing:
    """ _summary_
    """
    capacity: int = 11  # initial size of the hash table
    table: List[Optional[MapEntry]] = field(default_factory=list)
    size: int = 0
    prime: int = 109345121
    alpha: float = 0.5
    scale: int = -1
    shift: int = -1
    cmp_function: Callable = None
    # number of active entries


def default_mp_entry_cmp(key: Any,
                         entry: MapEntry) -> int:
    """default_mp_entry_cmp _summary_

    Args:
        key (Any): _description_
        entry (MapEntry): _description_

    Returns:
        int: _description_
    """
    if (key == entry.key):
        return 0
    elif (key > entry.key):
        return 1
    return -1


def new_map(mp: LinearProbing,
            cmp_function: Callable = None) -> LinearProbing:
    """new_map funcion para crear una nueva tabla de hash con sondeo lineal.

    Args:
        mp (LinearProbing): mapa de sondeo lineal a inicializar, hecho con dataclass
        cmp_function (Callable, optional): función de comparación personalizada para las entradas del mapa. Defaults to None.

    Raises:
        Exception: si ocurre un error durante la creación del mapa.

    Returns:
        LinearProbing: mapa de sondeo lineal inicializado.
    """
    # try:
    if cmp_function is None:
        mp.cmp_function = default_mp_entry_cmp
    else:
        mp.cmp_function = cmp_function

    # inizializar capacidad
    mp.capacity = numbers.next_prime(int(mp.capacity // mp.alpha))
    mp.scale = rd.randint(1, mp.prime - 1)
    mp.shift = rd.randint(0, mp.prime - 1)

    i = 0
    while i < mp.capacity:
        entry = MapEntry(None, None)
        mp.table.append(entry)
        i += 1
    return mp
    # raise Exception as exp:
    #     print("Error in new_map():", exp)


def put(mp: LinearProbing,
        key: Any,
        value: Any) -> LinearProbing:
    new_entry = MapEntry(key, value, True)
    idx = numbers.hash_compress(key,
                                mp.scale,
                                mp.shift,
                                mp.prime,
                                mp.capacity)
    mp.table[idx] = new_entry
    return mp


entrada = MapEntry(None, None)
print("\n===========\n", entrada, type(entrada))

lpht = LinearProbing()
print("\n===========\n", lpht, type(lpht))


lpht = new_map(lpht)
print("\n===========\n", lpht, type(lpht))

lpht = put(lpht, "pepito", "ODIA EDA!!!!")

for entry in lpht.table:
    print(entry)
