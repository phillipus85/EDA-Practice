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
from DISClib.DataStructures import edge as e
from DISClib.ADT import list as lt
from DISClib.ADT import indexminpq as iminpq
from DISClib.ADT import map as map
from DISClib.ADT import graph as g
from DISClib.ADT import stack
from DISClib.Utils import error as error
import math
assert config


def Dijkstra(graph, source):
    """
    Implementa el algoritmo de Dijkstra
    Args:
        graph: El grafo de busqueda
        source: El vertice de inicio

    Returns:
        Un nuevo grafo vacío
    Raises:
        Exception
    """
    try:
        search = initSearch(graph, source)
        while not iminpq.isEmpty(search['iminpq']):
            v = iminpq.delMin(search['iminpq'])
            edges = g.adjacentEdges(graph, v)
            if edges is not None:
                for edge in lt.iterator(edges):
                    relax(search, edge)
        return search
    except Exception as exp:
        error.reraise(exp, 'dks:dijkstra')


def relax(search, edge):
    """
    Relaja el peso de los arcos del grafo con la
    nueva de un nuevo arco
    Args:
        search: La estructura de busqueda
        edge: El nuevo arco
    Returns:
        El grafo con los arcos relajados
    Raises:
        Exception
    """
    try:
        v = e.either(edge)
        w = e.other(edge, v)
        visited_v = map.get(search['visited'], v)['value']
        visited_w = map.get(search['visited'], w)['value']
        distw = visited_w['distTo']
        distv = visited_v['distTo'] + e.weight(edge)
        if (visited_w is None) or (distw > distv):
            distow = visited_v['distTo'] + e.weight(edge)
            map.put(search['visited'],
                    w,
                    {'marked': True, 'edgeTo': edge, 'distTo': distow}
                    )
            if iminpq.contains(search['iminpq'], w):
                iminpq.decreaseKey(search['iminpq'], w, distow)
            else:
                iminpq.insert(search['iminpq'], w, distow)
        return search
    except Exception as exp:
        error.reraise(exp, 'dks:relax')


def distTo(search, vertex):
    """
    Retorna el costo para llegar del vertice
    source al vertice vertex.
    Args:
        search: La estructura de busqueda
        vertex: El vertice destino
    Returns:
        El costo total para llegar de source a
        vertex. Infinito si no existe camino
    Raises:
        Exception
    """
    try:
        visited_v = map.get(search['visited'], vertex)
        if visited_v is None:
            return math.inf
        return visited_v['value']['distTo']
    except Exception as exp:
        error.reraise(exp, 'dks:disto')


def hasPathTo(search, vertex):
    """
    Indica si hay camino entre source
    y vertex
    Args:
        search: La estructura de busqueda
        vertex: El vertice de destino
    Returns:
        True si existe camino
    Raises:
        Exception
    """
    try:
        visited = map.get(search['visited'], vertex)
        if visited is not None and visited['value']['marked']:
            return True
        return False
    except Exception as exp:
        error.reraise(exp, 'dks:haspathto')


def pathTo(search, vertex):
    """
    Retorna el camino entre source y vertex
    en una pila.
    Args:
        search: La estructura de busqueda
        vertex: El vertice de destino
    Returns:
        Una pila con el camino entre source y vertex
    Raises:
        Exception
    """
    try:
        if hasPathTo(search, vertex) is False:
            return None
        path = stack.newStack()
        while vertex != search['source']:
            visited_v = map.get(search['visited'], vertex)['value']
            edge = visited_v['edgeTo']
            stack.push(path, edge)
            vertex = e.either(edge)
        return path
    except Exception as exp:
        error.reraise(exp, 'dks:pathto')


# ----------------------------------------------
#         Funciones Auxiliares
# ----------------------------------------------


def initSearch(graph, source):
    """
    Inicializa la estructura de busqueda y deja
    todos los arcos en infinito.
    Se inserta en la cola indexada el vertice source
    Args:
        graph: El grafo a examinar
        source: El vertice fuente
    Returns:
        Estructura de busqueda inicializada
    Raises:
        Exception
    """
    try:
        search = {
               'source': source,
               'visited': None,
               'iminpq': None
             }

        search['visited'] = map.newMap(numelements=g.numVertices(graph),
                                       maptype='PROBING',
                                       cmpfunction=graph['cmpfunction']
                                       )
        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            map.put(search['visited'],
                    vert,
                    {'marked': False, 'edgeTo': None, 'distTo': math.inf}
                    )
        map.put(search['visited'],
                source,
                {'marked': True, 'edgeTo': None, 'distTo': 0}
                )
        pq = iminpq.newIndexMinPQ(
                                  cmpfunction=graph['cmpfunction']
                                  )
        search['iminpq'] = pq
        iminpq.insert(search['iminpq'], source, 0)
        return search
    except Exception as exp:
        error.reraise(exp, 'dks:init')
