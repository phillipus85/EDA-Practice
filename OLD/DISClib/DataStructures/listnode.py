"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
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

"""
  Estructura que contiene la información a guardar en una lista encadenada
"""


def newSingleNode(element):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    """
    node = {'info': element, 'next': None}
    return(node)


def getElement(node):
    """
    Retorna la información de un nodo
    Args:
      node: El nodo a examinar
    Returns:
      La información almacenada en el nodo
    """
    return node['info']


def newDoubleNode(element):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    doblemente
    """
    node = {'info': element,
            'next': None,
            'prev': None
            }
    return node
