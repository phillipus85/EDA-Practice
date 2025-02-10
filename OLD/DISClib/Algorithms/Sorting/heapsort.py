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
 * Este módulo contiene la implementación del algoritmo de ordenamiento
 * por montículos (heap sort) un algoritmo creado por J.W.J. Williams que
 * utiliza el principio de dividir y conquistar para ordenar una
 * secuencia de elementos.
 * Contribución de:
 *
 * Jhostin Sánchez y Santiago Arteaga
 *
 """

import config
from DISClib.ADT import list as lt
assert config

"""
  Los algoritmos de este libro están basados en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


def sort(lst, sort_crit):
    """sort ordena una lista de elementos utilizando el algoritmo de
    ordenamiento por montículos (heapsort).

    Args:
        lst (list): La lista a ordenar.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.

    Returns:
        list: La lista ordenada.
    """
    # recuperar el tamaño de la lista
    size = lt.size(lst)
    # construir el montículo
    lst = heapify(lst, 1, size, sort_crit)
    i = size
    while i >= 1:
        # intercambiar el primer y el último elemento
        lt.exchange(lst, 1, i)
        # reconstruir el montículo
        sift(lst, 1, i, sort_crit)
        i -= 1
    return lst


def heapify(lst, low, high, sort_crit):
    """heapify construye el montículo inicial del algoritmo de
    ordenamiento. Utiliza el criterio de ordenamiento para ajustar la
    lista al montículo y poder garantizar que los elementos tienen hijos
    izquierdos y derechos según el índice de árbol binario lleno
    reconstruido en el indice i*2 y i*2+1 respectivamente.

    Args:
        lst (list): La lista a ordenar.
        low (int): límite inferior de la sublista a ordenar según el
        montículo.
        high (int): límite superior de la sublista a ordenar según el
        montículo.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.

    Returns:
        list: La lista ajustada al montículo (heap) según el criterio de
        ordenamiento.
    """
    # inidice del elemento medio
    i = int(high / 2)
    # buscar el elemento más grande
    while i >= low:
        sift(lst, i, high, sort_crit)
        i -= 1
    return lst


def sift(lst, low, high, sort_crit):
    """sift ajusta la lista al montículo según el criterio de
    ordenamiento (en: sift = spa: tamizar).

    Args:
        lst (list): La lista a ordenar.
        low (int): límite inferior de la sublista a ordenar según el
        montículo.
        high (int): límite superior de la sublista a ordenar según el
        montículo.
        sort_crit (func): Es una función definida por el usuario que
        representa el criterio de ordenamiento.
    """
    # indice temporal del padre
    parent = low
    # indice temporal del hijo izquierdo
    i_left = 2 * low
    # indice temporal del hijo derecho
    i_right = 2 * low + 1
    # si el hijo izquierdo es mayor que el padre
    if i_left < high and not sort_crit(lt.getElement(lst, i_left),
                                       lt.getElement(lst, parent)):
        parent = i_left
    # si el hijo derecho es mayor que el padre
    if i_right < high and not sort_crit(lt.getElement(lst, i_right),
                                        lt.getElement(lst, parent)):
        parent = i_right
    # si el padre no es el mayor
    if parent != low:
        # intercambiar el padre con el mayor de los hijos
        lt.exchange(lst, low, parent)
        # invocar recursivamente la función sift
        sift(lst, parent, high, sort_crit)
