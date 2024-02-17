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
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config
from DISClib.DataStructures import bstnode
from DISClib.Utils import error as error
from DISClib.ADT import list as lt
assert config


"""
  Este código está basado en la implementación
  propuesta por R.Sedgewick y Kevin Wayne en su libro
  Algorithms, 4th Edition
"""

#  ------------------------------------------------------------
#                       API TAD_BST
#  ------------------------------------------------------------


def newMap(omaptype, cmpfunction, datastructure):
    """
    Crea una tabla de simbolos ordenada.
    Args:
        compfunction: La funcion de comparacion
    Returns:
        La tabla de símbolos ordenada sin elementos
    Raises:
        Exception
    """
    try:
        bst = {'root': None,
               'cmpfunction': cmpfunction,
               'type': omaptype,
               'datastructure': datastructure}

        if(cmpfunction is None):
            bst['cmpfunction'] = defaultfunction
        else:
            bst['cmpfunction'] = cmpfunction

        return bst

    except Exception as exp:
        error.reraise(exp, 'BST:NewMap')


def put(bst, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        bst: El BST
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
    Returns:
        El arbol con la nueva pareja
    Raises:
        Exception
    """
    try:
        bst['root'] = insertNode(bst['root'], key, value, bst['cmpfunction'])
        return bst
    except Exception as exp:
        error.reraise(exp, 'Bst:Put')


def get(bst, key):
    """
    Retorna la pareja lleve-valor con llave igual  a key
    Args:
        bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        La pareja llave-valor en caso de que haya sido encontrada
    Raises:
        Exception
    """
    try:
        node = getNode(bst['root'], key, bst['cmpfunction'])
        return node
    except Exception as exp:
        error.reraise(exp, 'Bst:get')


def remove(bst, key):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Exception
    """
    try:
        bst['root'] = removeNode(bst['root'], key, bst['cmpfunction'])
        return bst
    except Exception as exp:
        error.reraise(exp, 'Bst:Remove')


def contains(bst, key):
    """
    Informa si la llave key se encuentra en la tabla de hash
    Args:
        bst: El arbol de búsqueda
        key: La llave a buscar
    Returns:
        True si la llave está presente False en caso contrario
    Raises:
        Exception
    """
    try:
        return (get(bst, key) is not None)
    except Exception as exp:
        error.reraise(exp, 'Bst:Contains')


def size(bst):
    """
    Retorna el número de entradas en la tabla de simbolos
    Args:
        bst: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    try:
        return sizeTree(bst['root'])
    except Exception as exp:
        error.reraise(exp, 'Bst:size')


def isEmpty(bst):
    """
    Informa si la tabla de simbolos se encuentra vacia
    Args:
        bst: El arbol de búsqueda
    Returns:
        True si la tabla es vacía, False en caso contrario
    Raises:
        Exception
    """
    try:
        return (bst['root'] is None)
    except Exception as exp:
        error.reraise(exp, 'BST:isempty')


def keySet(bst):
    """
    Retorna una lista con todas las llaves de la tabla
    Args:
        bst: La tabla de simbolos
    Returns:
        Una lista con todas las llaves de la tabla
    Raises:
        Exception
    """
    try:
        klist = lt.newList('SINGLE_LINKED', bst['cmpfunction'])
        klist = keySetTree(bst['root'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'BST:KeySet')


def valueSet(bst):
    """
    Construye una lista con los valores de la tabla
    Args:
        bst: La tabla con los elementos
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    try:
        vlist = lt.newList('SINGLE_LINKED', bst['cmpfunction'])
        vlist = valueSetTree(bst['root'], vlist)
        return vlist
    except Exception as exp:
        error.reraise(exp, 'BST:valueSet')


def minKey(bst):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        bst: La tabla de simbolos
    Returns:
        La menor llave de la tabla
    Raises:
        Exception
    """
    try:
        node = minKeyNode(bst['root'])
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:minKey')


def maxKey(bst):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        bst: La tabla de simbolos
    Returns:
        La mayor llave de la tabla
    Raises:
        Exception
    """
    try:
        node = maxKeyNode(bst['root'])
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:maxKey')


def deleteMin(bst):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos
    y su valor asociado
    Args:
        bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        return deleteMinTree(bst['root'])
    except Exception as exp:
        error.reraise(exp, 'BST:deleteMin')


def deleteMax(bst):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    Args:
        bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Exception
    """
    try:
        return deleteMaxTree(bst['root'])
    except Exception as exp:
        error.reraise(exp, 'BST:deleteMax')


def floor(bst, key):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        La llave más grande menor o igual a key
    Raises:
        Exception
    """
    try:
        node = floorKey(bst['root'], key, bst['cmpfunction'])
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:floor')


def ceiling(bst, key):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    try:
        node = ceilingKey(bst['root'], key, bst['cmpfunction'])
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:ceiling')


def select(bst, pos):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        bst: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    try:
        node = selectKey(bst['root'], pos)
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:Select')


def rank(bst, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        bst: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        El nuemero de llaves encontradas
    Raises:
        Exception
    """
    try:
        return rankKeys(bst['root'], key, bst['cmpfunction'])
    except Exception as exp:
        error.reraise(exp, 'BST:rank')


def height(bst):
    """
    Retorna la altura del arbol de busqueda
    Args:
        bst: La tabla de simbolos
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    try:
        return heightTree(bst['root'])
    except Exception as exp:
        error.reraise(exp, 'BST:height')


def keys(bst, keylo, keyhi):
    """
    Retorna todas las llaves del arbol que se encuentren entre
    [keylo, keyhi]

    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    try:
        lstkeys = lt.newList('SINGLE_LINKED', bst['cmpfunction'])
        lstkeys = keysRange(bst['root'], keylo, keyhi, lstkeys,
                            bst['cmpfunction'])
        return lstkeys
    except Exception as exp:
        error.reraise(exp, 'BST:keys')


def values(bst, keylo, keyhi):
    """
    Retorna todas los valores del arbol que se encuentren entre
    [keylo, keyhi]

    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    try:
        lstvalues = lt.newList('SINGLE_LINKED', bst['cmpfunction'])
        lstvalues = valuesRange(bst['root'], keylo, keyhi, lstvalues,
                                bst['cmpfunction'])
        return lstvalues
    except Exception as exp:
        error.reraise(exp, 'BST:Values')

# _____________________________________________________________________
#            Funciones Helper
# _____________________________________________________________________


def insertNode(root, key, value, cmpfunction):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        root: La raiz del arbol
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
        cmpfunction : Función de comparación
    Returns:
        El arbol con la nueva pareja
    Raises:
        Exception
    """
    try:
        if (root is None):
            root = bstnode.newNode(key, value, 1)
        else:
            cmp = cmpfunction(key, root['key'])
            if (cmp < 0):           # La llave a insertar es menor que la raiz
                root['left'] = insertNode(root['left'], key, value,
                                          cmpfunction)

            elif (cmp > 0):        # La llave a insertar es mayor que la raiz
                root['right'] = insertNode(root['right'], key, value,
                                           cmpfunction)

            else:                  # La llave a insertar es igual que la raiz
                root['value'] = value
        leftsize = sizeTree(root['left'])
        rightsize = sizeTree(root['right'])
        root['size'] = 1 + leftsize + rightsize
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:insertNode')


def getNode(root, key, cmpfunction):
    """
    Retorna la pareja lleve-valor con llave igual  a key
    Args:
        root: El arbol de búsqueda
        key: La llave asociada a la pareja
        cmpfunction: Función de comparación
    Returns:
        El arbol con la nueva pareja
    Raises:
        Exception
    """
    try:
        node = None
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp == 0):
                node = root
            elif (cmp < 0):
                node = getNode(root['left'], key, cmpfunction)
            else:
                node = getNode(root['right'], key, cmpfunction)
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:getNode')


def removeNode(root, key, cmpfunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        bst: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Exception
    """
    try:
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp == 0):  # La llave es la que se busca
                if (root['right'] is None):   # No tiene hijo derecho
                    return root['left']
                elif (root['left'] is None):  # No tiene hijo izquierdo
                    return root['right']
                else:      # se cambia por el menor de los mayores
                    elem = root
                    root = minKeyNode(elem['right'])
                    root['right'] = deleteMinTree(elem['right'])
                    root['left'] = elem['left']
            elif (cmp < 0):
                root['left'] = removeNode(root['left'], key, cmpfunction)
            else:
                root['right'] = removeNode(root['right'], key, cmpfunction)
            root['size'] = 1 + sizeTree(root['left']) + sizeTree(root['right'])
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:removeNode')


def sizeTree(root):
    """
    Retornar el número de entradas en la a partir un punto dado
    Args:
        root: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    try:
        if (root is None):
            return 0
        else:
            return root['size']
    except Exception as exp:
        error.reraise(exp, 'BST:sizeTree')


def valueSetTree(root, klist):
    """
    Construye una lista con los valorers de la tabla
    Args:
        root: El arbol con los elementos
        klist: La lista de respuesta
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    try:
        if (root is not None):
            valueSetTree(root['left'], klist)
            lt.addLast(klist, root['value'])
            valueSetTree(root['right'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'BST:valueSetTree')


def keySetTree(root, klist):
    """
    Construye una lista con las llaves de la tabla
    Args:
        root: El arbol con los elementos
        klist: La lista de respuesta
    Returns:
        Una lista con todos las llaves
    Raises:
        Exception
    """
    try:
        if (root is not None):
            keySetTree(root['left'], klist)
            lt.addLast(klist, root['key'])
            keySetTree(root['right'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'BST:keySetTree')


def minKeyNode(root):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        root: La raiz del arbol de busqueda
    Returns:
        El elemento mas izquierdo del arbol
    Raises:
        Exception
    """
    try:
        min = None
        if (root is not None):
            if (root['left'] is None):
                min = root
            else:
                min = minKeyNode(root['left'])
        return min
    except Exception as exp:
        error.reraise(exp, 'BST:minKeyNode')


def maxKeyNode(root):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        bst: La tabla de simbolos
    Returns:
        El elemento mas derecho del árbol
    Raises:
        Exception
    """
    try:
        max = None
        if (root is not None):
            if (root['right'] is None):
                max = root
            else:
                max = maxKeyNode(root['right'])
        return max
    except Exception as exp:
        error.reraise(exp, 'BST:maxKeyNode')


def deleteMinTree(root):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos
    y su valor asociado
    Args:
        root: La raiz del arbol de busqueda
    Returns:
        El arbol de busqueda
    Raises:
        Excep
    """
    try:
        if (root is not None):
            if (root['left'] is None):
                return root['right']
            else:
                root['left'] = deleteMinTree(root['left'])
            root['size'] = sizeTree(root['left']) + sizeTree(root['right']) + 1
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:deleteMinTree')


def deleteMaxTree(root):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    Args:
        root: el arbol de busqueda
    Returns:
        El árbol de búsqueda sin la mayor llave
    Raises:
        Excep
    """
    try:
        if (root is not None):
            if (root['right'] is None):
                return root['left']
            else:
                root['right'] = deleteMaxTree(root['right'])
            root['size'] = sizeTree(root['left']) + sizeTree(root['right']) + 1
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:deleteMaxTree')


def floorKey(root, key, cmpfunction):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    Args:
        bst: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Excep
    """
    try:
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp == 0):
                return root
            if (cmp < 0):
                return floorKey(root['left'], key, cmpfunction)
            t = floorKey(root['right'], key, cmpfunction)
            if (t is not None):
                return t
            else:
                return root
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:floorKey')


def ceilingKey(root, key, cmpfunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    try:
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp == 0):
                return root
            if (cmp < 0):
                t = ceilingKey(root['left'], key, cmpfunction)
                if (t is not None):
                    return t
                else:
                    return root
            return ceilingKey(root['right'], key, cmpfunction)
        return None
    except Exception as exp:
        error.reraise(exp, 'BST:ceilingKey')


def selectKey(root, key):
    """
    Retorna la k-esima llave mas pequeña de la tabla
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Excep
    """
    try:
        if (root is not None):
            cont = sizeTree(root['left'])
            if (cont > key):
                return selectKey(root['left'], key)
            elif (cont < key):
                return selectKey(root['right'], key-cont-1)
            else:
                return root
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:selectKey')


def rankKeys(root, key, cmpfunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        bst: La tabla de simbolos
        key: la llave de busqueda
    Returns:
        El numero de llaves
    Raises:
        Exception
    """
    try:
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp < 0):
                return rankKeys(root['left'], key, cmpfunction)
            elif (cmp > 0):
                leftsize = sizeTree(root['left'])
                rank = rankKeys(root['right'], key, cmpfunction)
                total = 1 + leftsize + rank
                return total
            else:
                return sizeTree(root['left'])
        return 0
    except Exception as exp:
        error.reraise(exp, 'BST:ranKeys')


def heightTree(root):
    """
    Retorna la altura del arbol de busqueda
    Args:
        root: La tabla de simbolos
    Returns:
        La altura del arbol
    Raises:
        Excep
    """
    try:
        if (root is None):
            return -1
        else:
            return 1 + max(heightTree(root['left']),
                           heightTree(root['right']))
    except Exception as exp:
        error.reraise(exp, 'BST:heihgTree')


def keysRange(root, keylo, keyhi, lstkeys, cmpfunction):
    """
    Retorna todas las llaves del arbol en un rango dado
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Excep
    """
    try:
        if (root is not None):
            complo = cmpfunction(keylo, root['key'])
            comphi = cmpfunction(keyhi, root['key'])

            if (complo < 0):
                keysRange(root['left'], keylo, keyhi, lstkeys, cmpfunction)
            if ((complo <= 0) and (comphi >= 0)):
                lt.addLast(lstkeys, root['key'])
            if (comphi > 0):
                keysRange(root['right'], keylo, keyhi, lstkeys, cmpfunction)
        return lstkeys
    except Exception as exp:
        error.reraise(exp, 'BST:keysRange')


def valuesRange(root, keylo, keyhi, lstvalues, cmpfunction):
    """
    Retorna todas los valores del arbol en un rango dado por
    [keylo, keyhi]
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superior
    Returns:
        Las llaves en el rago especificado
    Raises:
        Excep
    """
    try:
        if (root is not None):
            complo = cmpfunction(keylo, root['key'])
            comphi = cmpfunction(keyhi, root['key'])

            if (complo < 0):
                valuesRange(root['left'], keylo, keyhi, lstvalues,
                            cmpfunction)
            if ((complo <= 0) and (comphi >= 0)):
                lt.addLast(lstvalues, root['value'])
            if (comphi > 0):
                valuesRange(root['right'], keylo, keyhi, lstvalues,
                            cmpfunction)
        return lstvalues
    except Exception as exp:
        error.reraise(exp, 'BST:valuesrange')


def defaultfunction(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1
