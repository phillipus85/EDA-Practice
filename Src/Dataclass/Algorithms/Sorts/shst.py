"""
Implementación del algoritmo de ordenamiento de Shell (Shell sort) para listas genéricas que incluyen los tipos de listas soportadas por el ADT **List**: Arraylist, SingleLinked, DoubleLinked, Queue y Stack.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
    # Se utiliza la secuencia de incrementos 3x+1: 1, 4, 13, 40, 121, 364, 109, (D. Knuth); Sedgewick: 1,5,19,41,109,209,929,2161,...
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
        _size = lt.size()    # tamaño de la lista
        h = 0
        while h < _size / 3:
            h = 3 * h + 1
        while h >= 1:
            i = h
            while i < _size:
                j = i
                while j >= h and sort_crit(lt.get_element(j),
                                           lt.get_element(j - h)):
                    lt.exchange(j, j - h)
                    j -= h
                i += 1
            h //= 3
        return lt
    except Exception as e:
        # get current module and function name
        _context = __name__.split(".")[-1]
        _func = inspect.currentframe().f_code.co_name
        # handle the error
        err(_context, _func, e)
