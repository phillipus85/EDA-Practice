from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
    _sort(lt, 0, lst.size(lt) - 1, sort_crit, lst)
    return lt


def _sort(lt: dict,
          low: int,
          high: int,
          sort_crit: Callable,
          _mod: Callable) -> dict:
    if low >= high:
        return
    pivot = _partition(lt, low, high, sort_crit, _mod)
    _sort(lt, low, pivot - 1, sort_crit, _mod)
    _sort(lt, pivot + 1, high, sort_crit, _mod)
    # return lt


def _partition(lt: dict,
               low: int,
               high: int,
               sort_crit: Callable,
               _mod: Callable) -> int:
    follower = leader = low
    while leader < high:
        if sort_crit(_mod.get_element(lt, leader),
                     _mod.get_element(lt, high)):
            _mod.exchange(lt, follower, leader)
            follower += 1
        leader += 1
    _mod.exchange(lt, follower, high)
    return follower
