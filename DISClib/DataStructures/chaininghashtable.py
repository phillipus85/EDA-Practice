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
Implementación de una tabla de hash, utilizando Separate Chaining como
mecanismo de manejo de colisiones.  Esta implementación crea una lista
de tamaño capacity.  En cada posición de la lista, se crea una lista
vacia.

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
        loadfactor: Factor de carga inicial de la tabla
        cmpfunc: Funcion de comparación entre llaves
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
                     'size': 0,
                     'limitfactor': loadfactor,
                     'currentfactor': 0,
                     'type': 'CHAINING',
                     'datastructure': datastructure}
        if(cmpfunction is None):
            cmpfunc = defaultcompare
        else:
            cmpfunc = cmpfunction
        hashtable['cmpfunction'] = cmpfunc
        hashtable['table'] = lt.newList(datastructure='ARRAY_LIST',
                                        cmpfunction=cmpfunc)
        for _ in range(capacity):
            bucket = lt.newList(datastructure='SINGLE_LINKED',
                                cmpfunction=hashtable['cmpfunction'])
            lt.addLast(hashtable['table'], bucket)
        return hashtable
    except Exception as exp:
        error.reraise(exp, 'Chain:newMap')


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
        bucket = lt.getElement(map['table'], hash)
        pos = lt.isPresent(bucket, key)
        if pos > 0:
            return True
        else:
            return False
    except Exception as exp:
        error.reraise(exp, 'Chain:contains')


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
        hash = hashValue(map, key)
        bucket = lt.getElement(map['table'], hash)
        entry = me.newMapEntry(key, value)
        pos = lt.isPresent(bucket, key)
        if pos > 0:    # La pareja ya exista, se reemplaza el valor
            lt.changeInfo(bucket, pos, entry)
        else:
            lt.addLast(bucket, entry)   # La llave no existia
            map['size'] += 1
            map['currentfactor'] = map['size'] / map['capacity']

        if (map['currentfactor'] >= map['limitfactor']):
            rehash(map)

        return map
    except Exception as exp:
        error.reraise(exp, 'Chain:put')


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
        bucket = lt.getElement(map['table'], hash)
        pos = lt.isPresent(bucket, key)
        if pos > 0:
            return lt.getElement(bucket, pos)
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'Chain:get')


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
        bucket = lt.getElement(map['table'], hash)
        if (bucket is not None):
            pos = lt.isPresent(bucket, key)
            if pos > 0:
                lt.deleteElement(bucket, pos)
                map['size'] -= 1
        return map
    except Exception as exp:
        error.reraise(exp, 'Chain:remove')


def size(map):
    """  Retorna  el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    return map['size']


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
        bucket = lt.newList()
        empty = True
        for pos in range(lt.size(map['table'])):
            bucket = lt.getElement(map['table'], pos+1)
            if lt.isEmpty(bucket) is False:
                empty = False
                break
        return empty
    except Exception as exp:
        error.reraise(exp, 'Chain:isempty')


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
        ltset = lt.newList('SINGLE_LINKED', map['cmpfunction'])
        for pos in range(lt.size(map['table'])):
            bucket = lt.getElement(map['table'], pos+1)
            if(not lt.isEmpty(bucket)):
                for element in range(lt.size(bucket)):
                    entry = lt.getElement(bucket, element+1)
                    lt.addLast(ltset, entry['key'])
        return ltset
    except Exception as exp:
        error.reraise(exp, 'Chain:keyset')


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
        ltset = lt.newList('SINGLE_LINKED', map['cmpfunction'])
        for pos in range(lt.size(map['table'])):
            bucket = lt.getElement(map['table'], pos+1)
            if (not lt.isEmpty(bucket)):
                for element in range(lt.size(bucket)):
                    entry = lt.getElement(bucket, element+1)
                    lt.addLast(ltset, entry['value'])
        return ltset
    except Exception as exp:
        error.reraise(exp, 'Chain, valueset')


# __________________________________________________________________
#       Helper Functions
# __________________________________________________________________


def rehash(map):
    """
    Se aumenta la capacida de la tabla al doble y se hace
    rehash de todos los elementos de la tabla
    """
    try:
        newtable = lt.newList('ARRAY_LIST', map['cmpfunction'])
        capacity = nextPrime(map['capacity']*2)
        oldtable = map['table']
        for _ in range(capacity):
            bucket = lt.newList(datastructure='SINGLE_LINKED',
                                cmpfunction=map['cmpfunction'])
            lt.addLast(newtable, bucket)
        map['size'] = 0
        map['currentfactor'] = 0
        map['table'] = newtable
        map['capacity'] = capacity
        for pos in range(1, lt.size(oldtable)+1):
            bucket = lt.getElement(oldtable, pos)
            if (lt.size(bucket) > 0):
                for posbucket in range(1, lt.size(bucket)+1):
                    entry = lt.getElement(bucket, posbucket)
                    put(map, entry['key'], entry['value'])
        return map
    except Exception as exp:
        error.reraise(exp, "Chain:rehash")


def hashValue(table, key):
    """
    Calcula un hash para una llave, utilizando el método
    MAD : hashValue(y) = ((ay + b) % p) % M.
    Donde:
    M es el tamaño de la tabla, primo
    p es un primo mayor a M,
    a y b enteros aleatoreos dentro del intervalo [0,p-1], con a>0
    """
    h = (hash(key))
    a = table['scale']
    b = table['shift']
    p = table['prime']
    m = table['capacity']
    value = int((abs(a*h + b) % p) % m) + 1
    return value


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
