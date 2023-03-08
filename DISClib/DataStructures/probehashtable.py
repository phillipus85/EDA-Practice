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

import random as rd
import math
import config
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.Utils import error as error
assert config

"""
Implementación de una tabla de hash, utilizando linear probing como
mecanismo de manejo de colisiones.

Este código está basado en las implementaciones propuestas en:
- Algorithms, 4th Edition.  R. Sedgewick
- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich
"""


def newMap(numelements, prime, loadfactor, cmpfunction, datastructure):
    """Crea una tabla de simbolos (map) sin orden

    Crea una tabla de hash con capacidad igual a nuelements
    (primo mas cercano al doble de numelements).
    prime es un número primo utilizado para  el cálculo de los codigos
    de hash, si no es provisto se  utiliza el primo 109345121.

    Args:
        numelements: Tamaño inicial de la tabla
        prime: Número primo utilizado en la función MAD
        loadfactor: Factor de carga maximo de la tabla
        cmpfunction: Funcion de comparación entre llaves
        datastructure: estructura de datos seleccionada
    Returns:
        Un nuevo map
    Raises:
        Exception
    """
    try:
        capacity = nextPrime(numelements//loadfactor)
        scale = rd.randint(1, prime-1)
        shift = rd.randint(0, prime-1)
        hashtable = {'prime': prime,
                     'capacity': capacity,
                     'scale': scale,
                     'shift': shift,
                     'table': None,
                     'currentfactor': 0,
                     'limitfactor': loadfactor,
                     'cmpfunction': None,
                     'size': 0,
                     'type': 'PROBING',
                     'datastructure': datastructure}
        if(cmpfunction is None):
            cmpfunc = defaultcompare
        else:
            cmpfunc = cmpfunction
        hashtable['cmpfunction'] = cmpfunc
        hashtable['table'] = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpfunc)
        for _ in range(capacity):
            entry = me.newMapEntry(None, None)
            lt.addLast(hashtable['table'], entry)
        return hashtable
    except Exception as exp:
        error.reraise(exp, 'Probe:newMap')


def put(map, key, value):
    """ Ingresa una pareja llave,valor a la tabla de hash.
    Si la llave ya existe en la tabla, se reemplaza el valor

    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja
        value: el valor asociado a la pareja
    Returns:
        El map
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)      # Se obtiene el hashcode de la llave
        entry = me.newMapEntry(key, value)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        lt.changeInfo(map['table'], abs(pos), entry)
        if (pos < 0):           # Se reemplaza el valor con el nuevo valor
            map['size'] += 1
            map['currentfactor'] = map['size'] / map['capacity']

        if (map['currentfactor'] >= map['limitfactor']):
            rehash(map)
        return map
    except Exception as exp:
        error.reraise(exp, 'Probe:put')


def contains(map, key):
    """ Retorna True si la llave key se encuentra en el map
        o False en caso contrario.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        True / False
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        if (pos > 0):
            return True
        else:
            return False
    except Exception as exp:
        error.reraise(exp, 'Probe:contains')


def get(map, key):
    """ Retorna la pareja llave, valor, cuya llave sea igual a key
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        Una pareja <llave,valor>
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        if pos > 0:
            element = lt.getElement(map['table'], pos)
            return element
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'Probe:get')


def remove(map, key):
    """ Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        El map
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        pos = findSlot(map, key, hash, map['cmpfunction'])
        if pos > 0:
            entry = me.newMapEntry('__EMPTY__', '__EMPTY__')
            lt.changeInfo(map['table'], pos, entry)
            map['size'] -= 1
        return map
    except Exception as exp:
        error.reraise(exp, 'Probe:remove')


def size(map):
    """  Retorna  el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    try:
        return map['size']
    except Exception as exp:
        error.reraise(exp, 'Probe:size')


def isEmpty(map):
    """ Informa si la tabla de hash se encuentra vacia
    Args:
        map: El map
    Returns:
        True: El map esta vacio
        False: El map no esta vacio
    Raises:
        Exception
    """
    try:
        empty = True
        for pos in range(lt.size(map['table'])):
            entry = lt.getElement(map['table'], pos+1)
            if (entry['key'] is not None and entry['key'] != '__EMPTY__'):
                empty = False
                break
        return empty
    except Exception as exp:
        error.reraise(exp, 'Probe:isEmpty')


def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de llaves
    Raises:
        Exception
    """
    try:
        ltset = lt.newList()
        for pos in range(lt.size(map['table'])):
            entry = lt.getElement(map['table'], pos+1)
            if (entry['key'] is not None and entry['key'] != '__EMPTY__'):
                lt.addLast(ltset, entry['key'])
        return ltset
    except Exception as exp:
        error.reraise(exp, 'Probe:keyset')


def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de valores
    Raises:
        Exception
    """
    try:
        ltset = lt.newList()
        for pos in range(lt.size(map['table'])):
            entry = lt.getElement(map['table'], pos+1)
            if (entry['value'] is not None and entry['value'] != '__EMPTY__'):
                lt.addLast(ltset, entry['value'])
        return ltset
    except Exception as exp:
        error.reraise(exp, 'Probe:valueset')


# __________________________________________________________________
#       Helper Functions
# __________________________________________________________________


def hashValue(table, key):
    """
    Calcula un hash para una llave, utilizando el método
    MAD : hashValue(y) = ((ay + b) % p) % M.
    Donde:
    M es el tamaño de la tabla, primo
    p es un primo mayor a M,
    a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0
    """
    try:
        h = (hash(key))
        a = table['scale']
        b = table['shift']
        p = table['prime']
        m = table['capacity']
        value = int((abs(a*h + b) % p) % m) + 1
        return value
    except Exception as exp:
        error.reraise(exp, 'Probe:hashvalue')


def findSlot(map, key, hashvalue, cmpfunction):
    """
    Encuentra una posición libre en la tabla de hash.
    map: la tabla de hash
    key: la llave
    hashvalue: La posición inicial de la llave
    cmpfunction: funcion de comparación para la búsqueda de la llave
    """
    try:
        avail = -1          # no se ha encontrado una posición aun
        searchpos = 0
        table = map['table']
        while (searchpos != hashvalue):  # Se busca una posición
            if (searchpos == 0):
                searchpos = hashvalue
            if isAvailable(table, searchpos):  # La posición esta disponible
                element = lt.getElement(table, searchpos)
                if (avail == -1):
                    avail = searchpos            # primera posición disponible
                if element['key'] is None:       # nunca ha sido utilizada
                    break
            else:                    # la posicion no estaba disponible
                element = lt.getElement(table, searchpos)
                if cmpfunction(key, element) == 0:  # Es la llave
                    return searchpos               # Se  retorna la posicion
            searchpos = (((searchpos) % map['capacity'])+1)
        return -(avail)    # numero negativo indica que el elemento no estaba
    except Exception as exp:
        error.reraise(exp, 'Probe:findslot')


def isAvailable(table, pos):
    """
    Informa si la posición pos esta disponible en la tabla de hash.
    Se entiende que una posición está disponible
    si su contenido es igual a None (no se ha usado esa posicion)
    o a __EMPTY__ (la posición fue liberada)
    """
    try:
        entry = lt.getElement(table, pos)
        if (entry['key'] is None or entry['key'] == '__EMPTY__'):
            return True
        return False
    except Exception as exp:
        error.reraise(exp, 'Probe:isAvailable')


def rehash(map):
    """
    Se aumenta la capacidad de la tabla al doble y se hace rehash de
    todos los elementos de la tabla.
    """
    try:
        newtable = lt.newList('ARRAY_LIST', map['cmpfunction'])
        capacity = nextPrime(map['capacity']*2)
        for _ in range(capacity):
            entry = me.newMapEntry(None, None)
            lt.addLast(newtable, entry)
        oldtable = map['table']
        map['size'] = 0
        map['currentfactor'] = 0
        map['table'] = newtable
        map['capacity'] = capacity
        for pos in range(lt.size(oldtable)):
            entry = lt.getElement(oldtable, pos+1)
            if (entry['key'] is not None and entry['key'] != '__EMPTY__'):
                hash = hashValue(map, entry['key'])
                loc = findSlot(map, entry['key'], hash, map['cmpfunction'])
                lt.changeInfo(map['table'], abs(loc), entry)
                if (loc < 0):
                    map['size'] += 1
                    map['currentfactor'] = map['size'] / map['capacity']
        return map
    except Exception as exp:
        error.reraise(exp, 'Probe:rehash')


# Function that returns True if n
# is prime else returns False
# This code is contributed by Sanjit_Prasad


def isPrime(n):
    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    if(n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False

    return True


# Function to return the smallest
# prime number greater than N
# # This code is contributed by Sanjit_Prasad
def nextPrime(N):
    # Base case
    if (N <= 1):
        return 2
    prime = int(N)
    found = False
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
        if(isPrime(prime) is True):
            found = True
    return int(prime)


def defaultcompare(key, element):
    if(key == element['key']):
        return 0
    elif(key > element['key']):
        return 1
    return -1
