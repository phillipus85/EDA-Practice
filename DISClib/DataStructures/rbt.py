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

import config
from DISClib.DataStructures import rbtnode as node
from DISClib.Utils import error as error
from DISClib.ADT import list as lt
assert config


"""
Implementación de una tabla de simbolos ordenada, mediante un arbol binario
balanceado Red-Black.

Este código está basados en la implementación
propuesta por R.Sedgewick y Kevin Wayne en su libro
Algorithms, 4th Edition
"""

# ________________________________________________________________________
#                     API  RBT
# ________________________________________________________________________


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
        rbt = {'root': None,
               'cmpfunction': None,
               'type': omaptype,
               'datastructure': datastructure}

        if(cmpfunction is None):
            rbt['cmpfunction'] = defaultfunction
        else:
            rbt['cmpfunction'] = cmpfunction

        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBT:NewMap')


def put(rbt, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        map: La tabla de simbolos ordenada
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
    Returns:
        La tabla de simbolos
    Raises:
        Exception
    """
    try:
        rbt['root'] = insertNode(rbt['root'], key, value, rbt['cmpfunction'])
        rbt['root']['color'] = node.BLACK
        return rbt
    except Exception as exp:
        error.reraise(exp, 'Bst:Put')


def get(rbt, key):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.

    Args:
        rbt: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        La pareja llave-valor en caso de que haya sido encontrada
    Raises:
        Exception
    """
    try:
        return getNode(rbt['root'], key, rbt['cmpfunction'])
    except Exception as exp:
        error.reraise(exp, 'RBR:get')


def remove(rbt, key):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        rbt: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Exception
    """
    try:
        root = rbt['root']
        if ((not isRed(root['left'])) and (not isRed(root['right']))):
            root['color'] = node.RED

        rbt['root'] = removeKey(root, key, rbt['cmpfunction'])
        if (not isEmpty(rbt)):
            rbt['root']['color'] = node.BLACK
        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBR:remove')


def contains(rbt, key):
    """
    Retorna True si la llave key se encuentra en la tabla
    o False en caso contrario.
    Es necesario proveer la función de comparación entre llaves.

    Args:
        rbt: El arbol de búsqueda
        key: La llave a buscar
    Returns:
        True si la llave se encuentra en la tabla
    Raises:
        Exception
    """
    try:
        if (rbt['root'] is None):
            return False
        else:
            return (get(rbt, key) is not None)
    except Exception as exp:
        error.reraise(exp, 'RBT: contains')


def size(rbt):
    """
    Retorna el número de entradas en la tabla de simbolos
    Args:
        rbt: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    try:
        return sizeTree(rbt['root'])
    except Exception as exp:
        error.reraise(exp, 'Bst:size')


def isEmpty(rbt):
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
        return (rbt['root'] is None)
    except Exception as exp:
        error.reraise(exp, 'Bst:isempty')


def keySet(rbt):
    """
    Retorna una lista con todas las llaves de la tabla
    Args:
        rbt: La tabla de simbolos
    Returns:
        Una lista con todas las llaves de la tabla
    Raises:
        Exception
    """
    try:
        klist = lt.newList('SINGLE_LINKED', rbt['cmpfunction'])
        klist = keySetTree(rbt['root'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'RBT:KeySet')


def valueSet(rbt):
    """
    Construye una lista con los valores de la tabla
    Args:
        rbt: La tabla con los elementos
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    try:
        vlist = lt.newList('SINGLE_LINKED', rbt['cmpfunction'])
        vlist = valueSetTree(rbt['root'], vlist)
        return vlist
    except Exception as exp:
        error.reraise(exp, 'RBT:valueSet')


def minKey(rbt):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        rbt: El arbol de búsqueda
    Returns:
        Retorna la menor llave de la tabla
    Raises:
        Exception
    """
    minkey = None
    if (rbt is not None):
        minkey = minKeyTree(rbt['root'])['key']
    return minkey


def maxKey(rbt):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        rbt: El arbol de búsqueda
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
    """
    maxkey = None
    if (rbt is not None):
        maxkey = maxKeyTree(rbt['root'])['key']
    return maxkey


def deleteMin(rbt):
    """
    Encuentra y remueve la menor  llave de la tabla de simbolos
    y su valor asociado

    TODO: No implementada en esta versión

    rbt: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        root = rbt['root']
        if (root is not None):
            if ((not isRed(root['left'])) and ((not isRed(root['right'])))):
                root['color'] = node.RED
            root = deleteMinTree(root)
            if (root is not None):
                root['color'] = node.BLACK
        rbt['root'] = root
        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMin')


def deleteMax(rbt):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado

    TODO: No implementada en esta versión

    Args:
        rbt: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Exception
    """
    try:
        root = rbt['root']
        if (root is not None):
            if ((not isRed(root['left'])) and ((not isRed(root['right'])))):
                root['color'] = node.RED
            root = deleteMaxTree(root)
            if (root is not None):
                root['color'] = node.BLACK
        rbt['root'] = root
        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMin')


def floor(rbt, key):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o
    igual a la llave key

    Args:
        rbt: El arbol de búsqueda
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
    """
    try:
        node = floorKey(rbt['root'], key, rbt['cmpfunction'])
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'RBT:floor')


def ceiling(rbt, key):
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
        node = ceilingKey(rbt['root'], key, rbt['cmpfunction'])
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'RBT:ceiling')


def select(rbt, pos):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        rbt: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    try:
        node = selectKey(rbt['root'], pos)
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:Select')


def rank(rbt, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        rbt: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        El nuemero de llaves encontradas
    Raises:
        Exception
    """
    try:
        return rankKeys(rbt['root'], key, rbt['cmpfunction'])
    except Exception as exp:
        error.reraise(exp, 'BST:rank')


def height(rbt):
    """
    Retorna la altura del arbol

    Args:
        rbt: El arbol con las parejas
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    try:
        return heightTree(rbt['root'])
    except Exception as exp:
        error.reraise(exp, 'RBT:height')


def keys(rbt, keylo, keyhi):
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
        lstkeys = lt.newList('SINGLE_LINKED', rbt['cmpfunction'])
        lstkeys = keysRange(rbt['root'], keylo, keyhi, lstkeys,
                            rbt['cmpfunction'])
        return lstkeys
    except Exception as exp:
        error.reraise(exp, 'RBT:keys')


def values(rbt, keylo, keyhi):
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
        lstvalues = lt.newList('SINGLE_LINKED', rbt['cmpfunction'])
        lstvalues = valuesRange(rbt['root'], keylo, keyhi, lstvalues,
                                rbt['cmpfunction'])
        return lstvalues
    except Exception as exp:
        error.reraise(exp, 'RBT:Values')


# _____________________________________________________________________________
#       Funciones Helper
# _____________________________________________________________________________


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
        error.reraise(exp, 'RBT:valueSetTree')


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


def rotateLeft(rbt):
    """
    rotación izquierda para compensar dos enlaces rojos consecutivos
    """
    try:
        x = rbt['right']
        rbt['right'] = x['left']
        x['left'] = rbt
        x['color'] = x['left']['color']
        x['left']['color'] = node.RED
        x['size'] = rbt['size']
        rbt['size'] = sizeTree(rbt['left']) + sizeTree(rbt['right']) + 1
        return x
    except Exception as exp:
        error.reraise(exp, 'RBT:rotateLeft')


def rotateRight(rbt):
    """
    Rotación a la derecha para compensar un hijo rojo a la derecha
    Args:
        rbt: El arbol a rotar
    Returns:
        El arbol rotado
    Raises:
        Exception
    """
    try:
        x = rbt['left']
        rbt['left'] = x['right']
        x['right'] = rbt
        x['color'] = x['right']['color']
        x['right']['color'] = node.RED
        x['size'] = rbt['size']
        rbt['size'] = sizeTree(rbt['left']) + sizeTree(rbt['right']) + 1
        return x
    except Exception as exp:
        error.reraise(exp, 'RBT:rotateRight')


def flipNodeColor(rbnode):
    """
    Cambia el color de un nodo
    Args:
        rbnode: El nodo a cambiar
    Returns:
        El nodo con el color opuesto
    Raises:
        Exception
    """
    try:
        if (rbnode is not None):
            if (rbnode['color'] == node.RED):
                rbnode['color'] = node.BLACK
            else:
                rbnode['color'] = node.RED
    except Exception as exp:
        error.reraise(exp, 'RBT:flipNodeColors')


def flipColors(rbnode):
    """
    Cambia el color de un nodo y de sus dos hijos
    Args:
        maptype: El tipo de map ordenado a utilizar
                 'BST' o 'RBT'
    Returns:
       La tabla de símbolos ordenada sin elementos
    Raises:
        Exception
    """
    try:
        flipNodeColor(rbnode)
        flipNodeColor(rbnode['left'])
        flipNodeColor(rbnode['right'])
    except Exception as exp:
        error.reraise(exp, 'RBT:flipColors')


def isRed(rbnode):
    """
    Indica si un nodo del arbol es rojo
    Args:
       rbnode:  El nodo a examinar
    Returns:
       True / False
    Raises:
        Exception
    """
    try:
        if (rbnode is None):
            return False
        else:
            return (rbnode['color'] == node.RED)
    except Exception as exp:
        error.reraise(exp, 'RBT:isRed')


def sizeTree(root):
    """
    Retorna el número de entradas en la a partir un punto dado
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
        error.reraise(exp, 'RBT:sizeTree')


def insertNode(root, key, value, comparefunction):
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
        if root is None:     # Se trata de la raíz del árbol
            root = node.newNode(key, value, 1, node.RED)
            return root

        cmp = comparefunction(key, root['key'])

        if (cmp < 0):     # La llave a insertar es menor que la raiz
            root['left'] = insertNode(root['left'],  key, value,
                                      comparefunction)
        elif (cmp > 0):    # La llave a insertar es mayor que la raíz
            root['right'] = insertNode(root['right'], key, value,
                                       comparefunction)
        else:              # La llave ya se encuentra en la tabla
            root['value'] = value

        # Se ajusta el balanceo del arbol

        if (isRed(root['right']) and not (isRed(root['left']))):
            root = rotateLeft(root)
        if (isRed(root['left']) and isRed(root['left']['left'])):
            root = rotateRight(root)
        if (isRed(root['left']) and isRed(root['right'])):
            flipColors(root)
        root['size'] = sizeTree(root['left']) + sizeTree(root['right']) + 1

        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:insertNode')


def heightTree(root):
    """
    Retorna la altura del arbol

    Args:
        root: El arbol con las parejas
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    try:
        if (root is None):
            return -1
        else:
            return 1 + max(heightTree(root['left']), heightTree(root['right']))
    except Exception as exp:
        error.reraise(exp, 'RBT:heightTree')


def getNode(root, key, comparefunction):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    Es necesario proveer una función de comparación para las llaves.

    Args:
        root: El arbol rojo-negro
        key: La llave de busqueda
        comparefunction: funcion de comparación
    Returns:
        La pareja llave-valor
    Raises:
        Exception
    """
    try:
        element = None
        if (root is not None):
            cmp = comparefunction(key, root['key'])
            if (cmp < 0):
                element = getNode(root['left'], key, comparefunction)
            elif (cmp > 0):
                element = getNode(root['right'], key, comparefunction)
            else:
                element = root
        return element

    except Exception as exp:
        error.reraise(exp, 'RBT:getNode')


def minKeyTree(root):
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
                min = minKeyTree(root['left'])
        return min
    except Exception as exp:
        error.reraise(exp, 'BST:minKeyNode')


def maxKeyTree(root):
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
                max = maxKeyTree(root['right'])
        return max
    except Exception as exp:
        error.reraise(exp, 'BST:maxKeyNode')


def floorKey(root, key, cmpfunction):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o
    igual a la llave key

    Args:
        rbt: El arbol de búsqueda
        key: La llave
        comparefunction: Funcion de comparacion
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
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
        error.reraise(exp, 'RBT:floorKey')


def ceilingKey(root, key, cmpfunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key

    Args:
        rbt: El arbol de búsqueda
        key: La llave
        comparefunction: Funcion de comparacion
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
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


def rankKeys(root, key, comparefunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        rbt: La tabla de simbolos
        key: La llave de busqueda
    Returns:
       El numero de llaves
    Raises:
        Exception
    """
    try:
        if (root is None):
            return 0
        cmp = comparefunction(key, root['key'])
        if (cmp < 0):
            return rankKeys(root['left'], key, comparefunction)
        elif (cmp > 0):
            lsize = sizeTree(root['left'])
            rank = rankKeys(root['right'], key, comparefunction)
            return 1 + lsize + rank
        else:
            return sizeTree(root['left'])
    except Exception as exp:
        error.reraise(exp, 'RBT:ranKeys')


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
        Exception
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
        error.reraise(exp, 'RBT:keysRange')


def valuesRange(root, keylo, keyhi, lstvalues, cmpfunction):
    """
    Retorna todas los valores del arbol en un rango dado por
    [keylo, keyhi]
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superior
    Returns:
        Las llaves en el rango especificado
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


def selectKey(root, key):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        root: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
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


def deleteMinTree(root):
    """
    Encuentra y remueve la menor  llave de la tabla de simbolos
    y su valor asociado

    root: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        if (root['left'] is None):
            return None
        if ((not isRed(root['left'])) and ((not isRed(root['left']['left'])))):
            root = moveRedLeft(root)
        root['left'] = deleteMinTree(root['left'])
        root = balance(root)
        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMinTree')


def deleteMaxTree(root):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado

    root: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        if (isRed(root['left'])):
            root = rotateRight(root)

        if (root['right'] is None):
            return None

        if ((not isRed(root['right'])) and
           ((not isRed(root['right']['left'])))):

            root = moveRedRight(root)

        root['right'] = deleteMaxTree(root['right'])
        root = balance(root)
        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMinTree')


def moveRedRight(root):
    """
    Cambio de color durante el proceso de eliminacion
    root: La tabla de simbolos
    Returns:
        El arbol con un hijo iquierdo de root en negro
    Raises:
        Exception
    """
    try:
        flipColors(root)
        if (isRed(root['left']['left'])):
            root = rotateRight(root)
            flipColors(root)
        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:moveRedLeft')


def moveRedLeft(root):
    """
    Cambio de color durante el proceso de eliminacion
    root: La tabla de simbolos
    Returns:
        El arbol con un hijo iquierdo de root en negro
    Raises:
        Exception
    """
    try:
        flipColors(root)
        if (isRed(root['right']['left'])):
            root['right'] = rotateRight(root['right'])
            root = rotateLeft(root)
            flipColors(root)
        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:moveRedLeft')


def balance(root):
    """
    Balancea el arbol
    root: Raiz del arbol a balancear
    Returns:
        El arbol balanceado
    Raises:
        Exception
    """
    try:
        if (isRed(root['right'])):
            root = rotateLeft(root)

        if (isRed(root['left']) and isRed(root['left']['left'])):
            root = rotateRight(root)

        if (isRed(root['left']) and isRed(root['right'])):
            flipNodeColor(root)

        lsize = sizeTree(root['left'])
        rsize = sizeTree(root['right'])
        root['size'] = 1 + lsize + rsize

        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:moveRedLeft')


def removeKey(root, key, cmpfunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        root: El arbol de búsqueda
        key: La llave asociada a la pareja
        cmpfunction : La funcion de comparacion
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Exception
    """
    try:
        if (cmpfunction(key, root['key']) < 0):
            if ((not isRed(root['left'])) and
               (not isRed(root['left']['left']))):
                root = moveRedLeft(root)
            root['left'] = removeKey(root['left'], key, cmpfunction)
        else:
            if (isRed(root['left'])):
                root = rotateRight(root)

            if ((cmpfunction(key, root['key']) == 0) and
               (root['right'] is None)):
                return None

            if ((not isRed(root['right']) and
               (not isRed(root['right']['left'])))):
                root = moveRedRight(root)

            if ((cmpfunction(key, root['key']) == 0)):
                temp = minKeyTree(root['right'])
                root['key'] = temp['key']
                root['value'] = temp['value']
                root['right'] = deleteMinTree(root['right'])
            else:
                root['right'] = removeKey(root['right'], key, cmpfunction)
        root = balance(root)
        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:removeKey')


def defaultfunction(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1
