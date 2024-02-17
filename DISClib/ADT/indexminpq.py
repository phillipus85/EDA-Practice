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
* Contribución de:
 *
 * Dario Correal
 *
 """


import config
from DISClib.DataStructures import indexheap as h
assert config

"""
Implementación de una cola de prioridad indexada orientada a menor

Este código está basados en la implementación
propuesta por R.Sedgewick y Kevin Wayne en su libro
Algorithms, 4th Edition
"""


def newIndexMinPQ(cmpfunction):
    """
    Crea un cola de prioridad indexada orientada a menor

    Args:
        cmpfunction: La funcion de comparacion
    Returns:
       Una nueva cola de prioridad indexada
    Raises:
        Exception
    """
    return h.newIndexHeap(cmpfunction)


def isEmpty(iminpq):
    """
    Informa si una cola de prioridad indexada es vacia

    Args:
        iminpq: La cola de prioridad indexada a revisar
    Returns:
       True si esta vacia
    Raises:
        Exception
    """
    return(h.isEmpty(iminpq))


def size(iminpq):
    """
    Retorna el número de elementos en la cola de prioridad indexada

    Args:
        iminpq: La cola de prioridad indexada a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return(h.size(iminpq))


def insert(iminpq, key, index):
    """
    Inserta la llave key con prioridad index

    Args:
        iheap: La cola de prioridad
    Returns:
       La cola de prioridad con la nueva paraja indexada
    Raises:
        Exception
    """
    return h.insert(iminpq, key, index)


def delMin(iminpq):
    """
    Elimina el elemento de mayor prioridad

    Args:
        iheap: El heap a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return (h.delMin(iminpq))


def decreaseKey(iminpq, key, newindex):
    """
    Decrementa el indice de un llave

    Args:
        iheap: El heap a revisar
        key: la llave a decrementar
        newindex: El nuevo indice de la llave
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.decreaseKey(iminpq, key, newindex)


def increaseKey(iminpq, key, newindex):
    """
    Incrementa el indice de un llave

    Args:
        iheap: El heap a revisar
        key: la llave a incrementar
        newindex: El nuevo indice de la llave
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.increaseKey(iminpq, key, newindex)


def min(iminpq):
    """
    Retorna la llave de mayor prioridad

    Args:
        iheap: El heap a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.min(iminpq)


def contains(iminpq, element):
    """
    Indica si la llave key se encuentra en el heap

    Args:
        iheap: El heap a revisar
    Returns:
       El numero de elementos
    Raises:
        Exception
    """
    return h.contains(iminpq, element)
