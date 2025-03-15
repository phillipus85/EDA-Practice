"""
Implementación del algoritmo de ordenamiento por mezcla (merge sort) para listas genéricas que incluyen los tipos de listas soportadas por el ADT **List**: Arraylist, SingleLinked, DoubleLinked, Queue y Stack.

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
    """*sort()* ordena una lista de elementos utilizando el algoritmo de ordenamiento por mezcla (merge sort).

    Args:
        lt (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento cumple con el criterio, y *False* en caso contrario.

    Returns:
        List: La lista ordenada.
    """
    try:

        # recuperar el tamaño de la lista
        _size = lt.size()
        # si la lista es mayor a 1, es decir no es trivial
        if _size > 1:
            # DIVIDIR
            # encontrar el punto medio de la lista, redondeando hacia abajo
            mid = int(_size / 2)
            # dividir la lista en dos sublistas izquierda y derecha
            _left = lt.sublist(0, mid - 1)
            _right = lt.sublist(mid, _size - 1)
            # ordenar recursivamente las sublistas izquierda y derecha
            # CONQUISTAR
            sort(_left, sort_crit)
            sort(_right, sort_crit)
            # RECOMBINAR
            # recomponer las sublistas izquierda y derecha en la original
            lt = _merge(_left, _right, lt, sort_crit)

        return lt
    except Exception as e:
        # get current module and function name
        _context = __name__.split(".")[-1]
        _func = inspect.currentframe().f_code.co_name
        # handle the error
        err(_context, _func, e)


def _merge(_left: List,
           _right: List,
           lt: List,
           sort_crit: Callable[[T, T], bool]) -> List:
    """*_merge()* recombina las sublistas izquierda y derecha en una sola lista ordenada dentro del algoritmo de ordenamiento por mezcla (merge sort).

    Args:
        _left (List): sublista izquierda creada recursivamente.
        _right (List): sublista derecha creada recursivamente.
        lt (List): La lista a ordenar. Puede ser *ArrayList*, *LinkedList*, *DoubleLinkedList*, *Queue* o *Stack*. Es la lista original que se va a ordenar.
        sort_crit (Callable[[T, T], bool]): Es una función definida por el usuario que representa el criterio de ordenamiento. Recibe dos elementos pertenecientes al ADT **List** y retorna *True* si el primer elemento cumple con el criterio, y *False* en caso contrario.

    Returns:
        List: la lista ordenada
    """
    # iteradores para la lista izquierda, derecha y original
    i = 0
    j = 0
    k = 0
    # __len__ y size() son funciones de python y DataStruct equivalentes
    # mientras se este en el rango de la lista original
    while k < lt.size():
        # si se esta dentro del rango de la lista izquierda y derecha
        if i < _left.size() and j < _right.size():
            # recuperar los elementos de ambas listas
            e_left = _left.get_element(i)
            e_right = _right.get_element(j)
            # comparar los elementos de ambas listas
            if sort_crit(e_left, e_right):
                # actualizar la lista original con el elemento de la lista izquierda
                lt.update(e_left, k)
                i += 1
            # si no se cumple la condicion anterior
            else:
                # actualizar la lista original con el elemento de la lista derecha
                lt.update(e_right, k)
                j += 1
        # COMPARAR LOS ELEMENTOS QUE NO ESTAN EN AMBAS LISTAS
        # si se esta dentro del rango de la lista izquierda
        elif i < len(_left):
            # actualizar la lista original con el elemento de la lista izquierda
            e_left = _left.get_element(i)
            lt.update(e_left, k)
            i += 1
        # si se esta dentro del rango de la lista derecha
        elif j < len(_right):
            # actualizar la lista original con el elemento de la lista derecha
            e_right = _right.get_element(j)
            lt.update(e_right, k)
            j += 1
        k += 1
    return lt
