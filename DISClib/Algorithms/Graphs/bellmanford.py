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
from DISClib.ADT import queue as q
from DISClib.ADT import map as map
from DISClib.ADT import graph as g
from DISClib.ADT import stack as st
from DISClib.Algorithms.Graphs import cycles as c
from DISClib.Utils import error as error
import math
assert config


def BellmanFord(graph, source):
    """
    Implementa el algoritmo de Bellman-Ford
    Args:
        graph: El grafo de busqueda
        source: El vertice de inicio

    Returns:
        La estructura search con los caminos de peso mínimos
    Raises:
        Exception
    """
    try:
        search = initSearch(graph, source)

        map.put(search['distTo'], source, 0.0)
        q.enqueue(search['qvertex'], source)
        map.put(search['onQ'], source, True)

        while (not q.isEmpty(search['qvertex']) and
                            (not hasNegativecycle(search))):
            v = q.dequeue(search['qvertex'])
            map.put(search['onQ'], v, False)
            relax(graph, search, v)
        return search
    except Exception as exp:
        error.reraise(exp, 'bf:BellmanFord')


def relax(graph, search, v):
    """
    Relaja el peso de los arcos del grafo
    Args:
        search: La estructura de busqueda
        v: Vertice desde donde se relajan los pesos
    Returns:
        El grafo con los arcos relajados
    Raises:
        Exception
    """
    try:
        edges = g.adjacentEdges(graph, v)
        if edges is not None:
            for edge in lt.iterator(edges):
                v = e.either(edge)
                w = e.other(edge, v)
                distv = map.get(search['distTo'], v)['value']
                distw = map.get(search['distTo'], w)['value']
                distweight = distv + e.weight(edge)
                if (distw > distweight):
                    map.put(search['distTo'], w, distweight)
                    map.put(search['edgeTo'], w, edge)
                    if (not map.get(search['onQ'], w)['value']):
                        q.enqueue(search['qvertex'], w)
                        map.put(search['onQ'], w, True)
                cost = search['cost']
                if ((cost % g.numVertices(graph)) == 0):
                    findneg = findNegativeCycle(graph, search)
                    if (hasNegativecycle(findneg)):
                        return
                search['cost'] = cost + 1
        return search
    except Exception as exp:
        error.reraise(exp, 'bellman:relax')


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
        distance = map.get(search['distTo'], vertex)['value']
        if distance is None:
            return math.inf
        return distance
    except Exception as exp:
        error.reraise(exp, 'bellman:disto')


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
        distance = map.get(search['distTo'], vertex)['value']
        return not hasNegativecycle(search) and distance < math.inf

    except Exception as exp:
        error.reraise(exp, 'bellman:haspathto')


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
        path = st.newStack()
        while vertex != search['source']:
            edge = map.get(search['edgeTo'], vertex)['value']
            st.push(path, edge)
            vertex = e.either(edge)
        return path
    except Exception as exp:
        error.reraise(exp, 'bellman:pathto')


# ----------------------------------------------
#         Funciones Auxiliares
# ----------------------------------------------

def findNegativeCycle(graph, search):
    """
    Identifica ciclos negativos en el grafo
    """
    try:
        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            edge = map.get(search['edgeTo'], vert)
            if (edge is not None):
                edge = edge['value']
                g.addEdge(search['spt'], e.either(edge),
                          e.other(edge, e.either(edge)), e.weight(edge))
        finder = c.DirectedCycle(search['spt'])
        search['cycle'] = not st.isEmpty(c.cycle(finder))
        return search
    except Exception as exp:
        error.reraise(exp, 'bellman:pathto')


def hasNegativecycle(search):
    return search['cycle']


def initSearch(graph, source):
    """
    Inicializa la estructura de busqueda y deja
    todos los arcos en infinito.
    Se inserta en la cola el vertice source
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
               'edgeTo': None,
               'distTo': None,
               'qvertex': None,
               'onQ': None,
               'cost': 0,
               'spt': None,
               'cycle': False
             }

        search['edgeTo'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      comparefunction=graph['comparefunction']
                                      )

        search['distTo'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      comparefunction=graph['comparefunction'])

        search['onQ'] = map.newMap(numelements=g.numVertices(graph),
                                   maptype='PROBING',
                                   comparefunction=graph['comparefunction']
                                   )

        search['spt'] = g.newGraph(size=g.numVertices(graph),
                                   directed=True,
                                   comparefunction=graph['comparefunction']
                                   )

        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            map.put(search['distTo'], vert, math.inf)
            map.put(search['onQ'], vert, False)
            g.insertVertex(search['spt'], vert)

        newq = q.newQueue()
        search['qvertex'] = newq

        return search

    except Exception as exp:
        error.reraise(exp, 'bellman:init')
