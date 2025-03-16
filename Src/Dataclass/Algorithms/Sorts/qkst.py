"""
Implementación del algoritmo de ordenamiento rapido (quick sort) para listas genéricas que incluyen los tipos de listas soportadas por el ADT **List**: Arraylist, SingleLinked, DoubleLinked, Queue y Stack.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import modules for defining the list types
from typing import Callable
# import inspect for getting the name of the current function
import inspect

# custom modules
from Src.Dataclass.DataStructs import List
from Src.Dataclass.Utils.error import error_handler as err
from Src.Dataclass.Utils.default import T

# checking custom modules
assert List
assert err
assert T


def sort(lt: List, sort_crit: Callable[[T, T], bool]) -> List:
    try:
        # TODO complete the function
        quicksort(lt, 0, lt.size()-1, sort_crit)
        return lt
    except Exception as e:
        # get current module and function name
        _context = __name__.split(".")[-1]
        _func = inspect.currentframe().f_code.co_name
        # handle the error
        err(_context, _func, e)


def quicksort(lt, lo, hi, sort_crit):
    if (lo >= hi):
        return
    pivot = partition(lt, lo, hi, sort_crit)
    quicksort(lt, lo, pivot-1, sort_crit)
    quicksort(lt, pivot + 1, hi, sort_crit)

def partition(lt, lo, hi, sort_crit):
    follower = leader = lo
    while leader < hi:
        if sort_crit(lt.get_element(leader),
                     lt.get_element(hi)):
            lt.exchange(follower, leader)
            follower += 1
        leader += 1
    lt.exchange(follower, hi)
    return follower