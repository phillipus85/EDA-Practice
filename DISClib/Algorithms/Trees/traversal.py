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
from DISClib.ADT import list as lt
assert config


def inorder(omap):
    """
    Implementa un recorrido inorder de un arbol binario
    """
    lst = lt.newList('SINGLE_LINKED', omap['cmpfunction'])
    if (omap is not None):
        lst = inorderTree(omap['root'], lst)
    return lst


def preorder(omap):
    """
    Implementa un recorrido preorder de un arbol binario
    """
    lst = lt.newList('SINGLE_LINKED', omap['cmpfunction'])
    if (omap is not None):
        lst = preorderTree(omap['root'], lst)
    return lst


def postorder(omap):
    """
    Implementa un recorrido postorder de un arbol binario
    """
    lst = lt.newList('SINGLE_LINKED', omap['cmpfunction'])
    if (omap is not None):
        lst = postorderTree(omap['root'], lst)
    return lst


# _____________________________________________________________________
#            Funciones Helper
# _____________________________________________________________________


def inorderTree(root, lst):
    if (root is None):
        return None
    else:
        inorderTree(root['left'], lst)
        lt.addLast(lst, root['value'])
        inorderTree(root['right'], lst)
    return lst


def postorderTree(root, lst):
    if (root is None):
        return None
    else:
        postorderTree(root['left'], lst)
        postorderTree(root['right'], lst)
        lt.addLast(lst, root['value'])
    return lst


def preorderTree(root, lst):
    if (root is None):
        return None
    else:
        lt.addLast(lst, root['value'])
        preorderTree(root['left'], lst)
        preorderTree(root['right'], lst)
    return lst
