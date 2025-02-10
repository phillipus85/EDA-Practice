"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * Dario Correal
 *
 """


def newNode(key, value, size):
    """ Crea un nuevo nodo para un árbol binario y lo retorna
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    node = {'key': key,
            'value': value,
            'size': size,
            'left': None,
            'right': None,
            'type': 'BST'}
    return node


def getValue(node):
    """ Retorna el valor asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        El valor almacenado en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return(node['value'])
    return node


def getKey(node):
    """ Retorna la llave asociado a una pareja llave valor
    Args:
        node: El nodo con la pareja llave-valor
    Returns:
        La llave almacenada en el nodo
    Raises:
        Exception
    """
    if (node is not None):
        return(node['key'])
    return node
