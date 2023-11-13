"""
 * Copyright 2022, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 * Jhostin Sánchez
 *
 """

import config
from DISClib.ADT import list as lt
from DISClib.Utils import error as error
import sys
from DISClib.DataStructures import heap as he
assert config

"""
  Los algoritmos de este libro están basados en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""
sys.setrecursionlimit(1000000)

def upHeap(heap, pos, end):
    """Mete el elemento en la posición correcta, compara los hijos y si hay uno mayor que el padre
    los intercambia

    Args:
        heap (ADT.HeapTree): Arbol en array
        pos (Int): Posición del padre
        end (Int): Hasta donde se evalúa del arbol
    Raises:
        Exception
    """
    try:
        while ((2*pos <= end)):
            j = 2*pos
            if (j < end):
                if not he.greater(heap, lt.getElement(heap['elements'], j),
                           lt.getElement(heap['elements'], (j+1))):
                    j += 1
            if (he.greater(heap, lt.getElement(heap['elements'], pos),
                            lt.getElement(heap['elements'], j))):
                break
            he.exchange(heap, pos, j)
            pos = j
    except Exception as exp:
        error.reraise(exp, 'heap:upHead')


def maxPQ(heap, n):
    """Se asegura de que la raíz es el elemento más grande en el Heap

    Args:
        heap (ADT.HeapTree):  Arbol en array
        n (Int): Elemento a colocar en la posición correcta
    Raises:
        Exception
    """
    try:
        if n>0:
            upHeap(heap, n, he.size(heap))
            maxPQ(heap, n-1)          
    except Exception as exp:
        error.reraise(exp, "heap:maxPQ")


def minPQ(heap, n):
    """Intercambiamos la raíz con la última posición del árbol y colocamos la nueva raíz en la posición correcta

    Args:
        heap (ADT.HeapTree):  Arbol en array
        n (Int): Elemento a colocar en la posición correcta
    Raises:
        Exception
    """
    try:
        if n>0:
            he.exchange(heap, 1 , n)
            upHeap(heap, 1, n-1)
            minPQ(heap, n-1)          
    except Exception as exp:
        error.reraise(exp, "heap:minPQ")

def heapSort(heap:he.newHeap)->None:
    """Algoritmo de ordenamiento de Heapsort

    Args:
        heap (ADT.HeapTree): Arbol(ARRAY) a ordenar
    """
    try:
        middle=he.size(heap)//2
        maxPQ(heap, middle)
        minPQ(heap, he.size(heap))
    except Exception as exp:
        error.reraise(exp, "heap:heapSort")

