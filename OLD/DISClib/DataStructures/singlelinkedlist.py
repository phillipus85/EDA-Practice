"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * Dario Correal
 *
 """

import config
from DISClib.DataStructures import listnode as node
from DISClib.Utils import error as error
import csv
assert config

"""
  Este módulo implementa una estructura de datos lineal mediante una lista
  encadenada sencillamente para almacenar una colección de elementos.
  Los elementos se cuentan desde la posición 1.

  Este código está basado en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""


def newList(cmpfunction, module, key, filename, delim):
    """Crea una lista vacía.

    Se inicializan los apuntadores a la primera y última posición en None.
    El tipo de la lista se inicializa como SINGLE_LINKED
    Args:
        cmpfunction: Función de comparación para los elementos de la lista.
        Si no se provee una función de comparación, se utilizará la función
        de comparación por defecto pero se debe suministrar un valor para key

        key: Identificador que se debe utilizar para la comparación de
        elementos de la lista

        filename: Si se provee este valor, se creará una lista a partir de
        la información que se encuentra en el archivo CSV

        delimiter: Si se provee un archivo para crear la lista, indica el
        delimitador a usar para separar los campos del archivo CSV

    Returns:
        Un diccionario que representa la estructura de datos de una lista
        encadenada vacía.

    Raises:

    """
    newlist = {'first': None,
               'last': None,
               'size': 0,
               'key': key,
               'type': 'SINGLE_LINKED',
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
    return newlist


def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posición.

    Agrega un elemento en la primera posición de la lista, ajusta el apuntador
    al primer elemento e incrementa el tamaño de la lista.

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
        new_node = node.newSingleNode(element)
        new_node['next'] = lst['first']
        lst['first'] = new_node
        if (lst['size'] == 0):
            lst['last'] = lst['first']
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->addFirst: ')


def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
     el apuntador a la última posición.
    Se incrementa el tamaño de la lista en 1
    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)

        if lst['size'] == 0:
            lst['first'] = new_node
        else:
            lst['last']['next'] = new_node
        lst['last'] = new_node
        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->addLast: ')


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
        error.reraise(exp, 'singlelinkedlist->isEmpty: ')


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
        error.reraise(exp, 'singlelinkedlist->size: ')


def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
     No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['first'] is not None:
            return lst['first']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->firstElement: ')


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        if lst['last'] is not None:
            return lst['last']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->lastElement: ')


def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser
    mayor que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eliminarlo.
    La lista no puede ser vacía.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        searchpos = 1
        node = lst['first']
        while searchpos < pos:
            searchpos += 1
            node = node['next']
        return node['info']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->getElement: ')


def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
    Se decrementa en un uno el tamaño de la lista.
    La lista no puede estar vacía.

    Args:
        lst: La lista a retornar
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        node = lst['first']
        prev = lst['first']
        searchpos = 1
        if (pos == 1):
            lst['first'] = lst['first']['next']
            lst['size'] -= 1
        elif(pos > 1):
            while searchpos < pos:
                searchpos += 1
                prev = node
                node = node['next']
            prev['next'] = node['next']
            lst['size'] -= 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->deleteElement: ')


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
        if lst['first'] is not None:
            temp = lst['first']['next']
            node = lst['first']
            lst['first'] = temp
            lst['size'] -= 1
            if (lst['size'] == 0):
                lst['last'] = lst['first']
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->removeFirst: ')


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
        if lst['size'] > 0:
            if lst['first'] == lst['last']:
                node = lst['first']
                lst['last'] = None
                lst['first'] = None
            else:
                temp = lst['first']
                while temp['next'] != lst['last']:
                    temp = temp['next']
                node = lst['last']
                lst['last'] = temp
                lst['last']['next'] = None
            lst['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        new_node = node.newSingleNode(element)
        if (lst['size'] == 0):
            lst['first'] = new_node
            lst['last'] = new_node

        elif ((lst['size'] > 0) and (pos == 1)):
            new_node['next'] = lst['first']
            lst['first'] = new_node

        else:
            cont = 1
            prev = lst['first']
            current = lst['first']
            while cont < pos:
                prev = current
                current = current['next']
                cont += 1
            new_node['next'] = current
            prev['next'] = new_node

        lst['size'] += 1
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->insertElement: ')


def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.  Si esta presente,
    retorna la posición en la que se encuentra  o cero (0) si no esta presente.
    Se utiliza la función de comparación utilizada durante la creación
    de la lista para comparar los elementos.
    La cual debe retornar cero en caso de que los elementos sean iguales.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar

    Raises:
        Exception
    """
    try:
        size = lst['size']
        if size > 0:
            node = lst['first']
            keyexist = False
            for keypos in range(1, size+1):
                if (node is not None):
                    if (compareElements(lst, element, node['info']) == 0):
                        keyexist = True
                        break
                    node = node['next']
            if keyexist:
                return keypos
        return 0
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->isPresent: ')


def changeInfo(lst, pos, newinfo):
    """ Cambia la información contenida en el nodo de la lista que se encuentra
         en la posición pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de
        la posición pos

    Raises:
        Exception
    """
    try:
        current = lst['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return lst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->changeInfo: ')


def exchange(lst, pos1, pos2):
    """ Intercambia la información en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posición del segundo elemento

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
        error.reraise(exp, 'singlelinkedlist->exchange: ')


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posición pos,con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        sublst = {'first': None,
                  'last': None,
                  'size': 0,
                  'type': 'SINGLE_LINKED',
                  'key': lst['key'],
                  'datastructure': lst['datastructure'],
                  'cmpfunction': lst['cmpfunction']}
        cont = 1
        loc = pos
        while cont <= numelem:
            elem = getElement(lst, loc)
            addLast(sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->subList: ')


def iterator(lst):
    """ Retorna un iterador para la lista.
    Args:
        lst: La lista a iterar

    Raises:
        Exception
    """
    try:
        if(lst is not None):
            current = lst['first']
            while current is not None:
                yield current['info']
                current = current['next']
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->Iterator')


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
    try:
        if(lst['key'] is not None):
            return lst['cmpfunction'](element[lst['key']], info[lst['key']])
        else:
            return lst['cmpfunction'](element, info)
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->compareElements')


def defaultfunction(id1, id2):
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0
