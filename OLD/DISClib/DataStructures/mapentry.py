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

"""
MapEntry representa una entrada (llave,valor) en un Map
"""


def newMapEntry(key, value):
    """
    Retorna una pareja llave valor para ser guardada
    en un Map
    Args:
        key: llave
        value: valor
    Returns:
        una entrada con la pareja llave-valor
    Raises:
        Exception
    """
    entry = {'key': key, 'value': value}
    return entry


def setKey(entry, key):
    """
    Asigna una llave a una pareja de un Map
    Args:
        entry: la pareja llave valor
        key: la nueva llave
    Returns:
        La pareja modificada
    Raises:
        Exception
    """
    entry['key'] = key
    return entry


def setValue(entry, value):
    """
    Asigna un nuevo valor a una pareja de un Map
    Args:
        entry: la pareja llave valor
        value: el nuevo valor
    Returns:
        La pareja modificada
    Raises:
        Exception
    """
    entry['value'] = value
    return entry


def getKey(entry):
    """
    Retorna la llave de una pareja de un Map
    Args:
        entry: la pareja llave valor
    Returns:
        La llave de la pareja
    Raises:
        Exception
    """
    return entry['key']


def getValue(entry):
    """
    Retorna el valor de una pareja de un Map
    Args:
        entry: la pareja llave valor
    Returns:
        La llave de la pareja
    Raises:
        Exception
    """
    return entry['value']
