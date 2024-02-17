"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config
from DISClib.ADT import list as lt
from DISClib.Utils import error as error
assert config

"""
Implementación de un heap basado en arreglo.

Este código está basados en la implementación
propuesta por R.Sedgewick y Kevin Wayne en su libro
Algorithms, 4th Edition
"""


def newHeap(cmpfunction):
    """
    Crea un nuevo heap basado en un arreglo, cuyo primer elemento
    es inicializado en None y no será utilizado

    Args:
        cmpfunction: La funcion de comparacion
        size: El numero de elementos
    Returns:
       El heap
    Raises:
        Exception
    """
    try:
        heap = {'elements': None,
                'size': 0,
                'cmpfunction': cmpfunction
                }

        heap['elements'] = lt.newList(datastructure='ARRAY_LIST',
                                      cmpfunction=cmpfunction)
        return heap
    except Exception as exp:
        error.reraise(exp, 'newHeap')


def size(heap):
    """
    Retorna el número de elementos en el heap

    Args:
        heap: El arreglo con la informacion
    Returns:
       El tamaño del heap
    Raises:
        Exception
    """
    try:
        return (heap['size'])
    except Exception as exp:
        error.reraise(exp, 'heap:size')


def isEmpty(heap):
    """
    Indica si el heap está vacío

    Args:
        heap: El arreglo con la informacion
    Returns:
      True si el heap es vacio
    Raises:
        Exception
    """
    try:
        return (heap['size'] == 0)
    except Exception as exp:
        error.reraise(exp, 'heap:isEmpty')


def min(heap):
    """
    Retorna el primer elemento del heap, es decir el menor elemento

    Args:
        heap: El arreglo con la informacion
    Returns:
      El menor elemento del heap
    Raises:
        Exception
    """
    try:
        if (heap['size'] > 0):
            return lt.getElement(heap['elements'], 1)
        return None
    except Exception as exp:
        error.reraise(exp, 'heap:min')


def insert(heap, element):
    """
    Guarda la pareja llave-valor en el heap. Lo guarda en la última
    posición y luego hace swim del elemento

    Args:
        heap: El arreglo con la informacion
        element: El elemento a guardar
    Returns:
        El heap con el nuevo elemento
    Raises:
        Exception
    """
    try:
        heap['size'] += 1
        lt.insertElement(heap['elements'], element, heap['size'])
        swim(heap, heap['size'])
        return heap
    except Exception as exp:
        error.reraise(exp, 'heap:insert')


def delMin(heap):
    """
    Retorna el menor elemento del heap y lo elimina.
    Se reemplaza con el último elemento y se hace sink.

    Args:
        heap: El arreglo con la informacion

    Returns:
        El menor elemento eliminado
    Raises:
        Exception
    """
    try:
        if (heap['size'] > 0):
            min = lt.getElement(heap['elements'], 1)
            last = lt.getElement(heap['elements'], heap['size'])
            lt.changeInfo(heap['elements'], 1, last)
            lt.changeInfo(heap['elements'], heap['size'], None)
            heap['size'] -= 1
            sink(heap, 1)
            return min
        return None
    except Exception as exp:
        error.reraise(exp, 'heap:delMin')


# _____________________________________________________________________________
#       Funciones Helper
# _____________________________________________________________________________


def swim(heap, pos):
    """
    Ubica en el lugar indicado un elemento adicionado
    en la última posición

    Args:
        heap: El arreglo con la informacion
        pos: posicion en el arreglo a revisar

    Returns:
        El arreglo en forma de heap
    Raises:
        Exception
    """
    try:
        while (pos > 1):
            parent = lt.getElement(heap['elements'], int((pos/2)))
            element = lt.getElement(heap['elements'], int(pos))
            if greater(heap, parent, element):
                exchange(heap, pos, int(pos/2))
            pos = pos//2
    except Exception as exp:
        error.reraise(exp, 'heap:swim')


def sink(heap, pos):
    """
    Ubica en la posición correcta un elemento ubicado en la raíz del heap

    Args:
        heap: El arreglo con la informacion
        pos: posicion en el arreglo a revisar

    Returns:
        El arreglo en forma de heap
    Raises:
        Exception
    """
    try:
        size = heap['size']
        while ((2*pos <= size)):
            j = 2*pos
            if (j < size):
                if greater(heap, lt.getElement(heap['elements'], j),
                           lt.getElement(heap['elements'], (j+1))):
                    j += 1
            if (not greater(heap, lt.getElement(heap['elements'], pos),
                            lt.getElement(heap['elements'], j))):
                break
            exchange(heap, pos, j)
            pos = j
    except Exception as exp:
        error.reraise(exp, 'heap:sink')


def greater(heap, element1, element2):
    """
    Indica si el elemento 1 es mayor que el elemento 2
    """
    try:
        cmp = heap['cmpfunction'](element1, element2)
        if cmp > 0:
            return True
        return False
    except Exception as exp:
        error.reraise(exp, 'heap:greater')


def exchange(heap, posa, posb):
    """
    Intercambia los elementos en las posiciones posa y posb del heap
    """
    try:
        lt.exchange(heap['elements'], posa, posb)
    except Exception as exp:
        error.reraise(exp, 'heap:exchange')
