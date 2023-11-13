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
from DISClib.Utils import error as error
import csv
assert config

"""
  Este módulo implementa una estructura de datos lineal,
  como un arreglo de apuntadores a los nodos de la lista.


  Este código está basado en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Un diccionario que representa la estructura de datos de una lista

    Raises:

    """
    newlist = {'elements': [],
               'size': 0,
               'type': 'ARRAY_LIST',
               'cmpfunction': cmpfunction,
               'key': key,
               'datastructure': module
               }

    if(cmpfunction is None):
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if (filename is not None):
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=delim)
        for line in input_file:
            addLast(newlist, line)
    return (newlist)


def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, se incrementa
    el tamaño de la lista en uno.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el proceso
        fue exitoso

    Raises:
        Exception
    """
    try:
        lst['elements'].insert(0, element)
        lst['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->addFirst: ')


def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
    el apuntador a la útima posición. Se incrementa el tamaño de la lista en 1

    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        lst['elements'].append(element)
        lst['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->addLast: ')


def isEmpty(lst):
    """ Indica si la lista está vacía

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['size'] == 0
    except Exception as exp:
        error.reraise(exp, 'arraylist->isEmpty: ')


def size(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['size']
    except Exception as exp:
        error.reraise(exp, 'arraylist->size: ')


def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['elements'][0]
    except Exception as exp:
        error.reraise(exp, 'arraylist->firstElement: ')


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['elements'][lst['size']-1]
    except Exception as exp:
        error.reraise(exp, 'arraylist->lastElement: ')


def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser mayor
    que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        return lst['elements'][pos-1]
    except Exception as exp:
        error.reraise(exp, 'arraylist->getElement: ')


def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor  o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista.
    La lista no puede estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        lst['elements'].pop(pos-1)
        lst['size'] -= 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->deleteElement: ')


def removeFirst(lst):
    """ Remueve el primer elemento de la lista.

    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.  Si la lista
    es vacía se retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        element = lst['elements'].pop(0)
        lst['size'] -= 1
        return element
    except Exception as exp:
        error.reraise(exp, 'arraylist->removeFirst: ')


def removeLast(lst):
    """ Remueve el último elemento de la lista.

    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        element = lst['elements'].pop(lst['size']-1)
        lst['size'] -= 1
        return element
    except Exception as exp:
        error.reraise(exp, 'arraylist->remoLast: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.
    Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        lst['elements'].insert(pos-1, element)
        lst['size'] += 1
    except Exception as exp:
        error.reraise(exp, 'arraylist->insertElement: ')


def isPresent(lst, e):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.
    Si esta presente, retorna la posición en la que se encuentra
    o cero (0) si no esta presente. Se utiliza la función de comparación
    utilizada durante la creación de la lista para comparar los elementos,
    la cual debe retornan cero si los elementos son iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        size = lst['size']
        if size > 0:
            keyexist = False
            for keypos in range(1, size+1):
                info = lst['elements'][keypos-1]
                if (compareElements(lst, e, info) == 0):
                    keyexist = True
                    break
            if keyexist:
                return keypos
        return 0
    except Exception as exp:
        error.reraise(exp, 'arraylist->isPresent: ')


def changeInfo(lst, pos, newinfo):
    """ Cambia la informacion contenida en el nodo de la lista
        que se encuentra en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el
        nodo de la posición pos

    Raises:
        Exception
    """
    try:
        lst['elements'][pos-1] = newinfo
    except Exception as exp:
        error.reraise(exp, 'arraylist->changeInfo: ')


def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    try:
        infopos1 = getElement(lst, pos1)
        infopos2 = getElement(lst, pos2)
        changeInfo(lst, pos1, infopos2)
        changeInfo(lst, pos2, infopos1)
        return lst
    except Exception as exp:
        error.reraise(exp, 'arraylist->exchange: ')


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la posicion
    pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        sublst = {'elements': [],
                  'size': 0,
                  'type': 'ARRAY_LIST',
                  'key': lst['key'],
                  'datastructure': lst['datastructure'],
                  'cmpfunction': lst['cmpfunction']}
        elem = pos-1
        cont = 1
        while cont <= numelem:
            sublst['elements'].append(lst['elements'][elem])
            sublst['size'] += 1
            elem += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'arraylist->subList: ')


def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    try:
        if(lst is not None):
            for pos in range(0, lst['size']):
                yield lst['elements'][pos]
    except Exception as exp:
        error.reraise(exp, 'arraylist->Iterator')


def compareElements(lst, element, info):
    """ Compara dos elementos

    Se utiliza la función de comparación por defecto si key es None
    o la función provista por el usuario en caso contrario
    Args:
        lst: La lista con los elementos
        element:  El elemento que se esta buscando en la lista
        info: El elemento de la lista que se está analizando

    Returns:  0 si los elementos son iguales, 1 si element > info, -1 si element < info

    Raises:
        Exception
    """
    if(lst['key'] is not None):
        return lst['cmpfunction'](element[lst['key']], info[lst['key']])
    else:
        return lst['cmpfunction'](element, info)


def defaultfunction(id1, id2):
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0
