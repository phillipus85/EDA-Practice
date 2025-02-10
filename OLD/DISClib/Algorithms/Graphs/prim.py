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
from DISClib.ADT import indexminpq as pq
from DISClib.ADT import queue as q
from DISClib.ADT import map as map
from DISClib.ADT import graph as g
from DISClib.Utils import error as error
import math
assert config


def PrimMST(graph, origin=None):
    """
    Implementa el algoritmo de Prim
    Args:
        graph: El grafo de busqueda

    Returns:
        La estructura search con los MST
    Raises:
        Exception
    """
    try:
        search = initSearch(graph)
        vertices = g.vertices(graph)
        if origin is not None:
            pos = lt.isPresent(vertices, origin)
            if pos != 0:
                lt.exchange(vertices, 1, pos)
        for vert in lt.iterator(vertices):
            if not map.get(search['marked'], vert)['value']:
                prim(graph, search, vert)
        return search
    except Exception as exp:
        error.reraise(exp, 'prim:PrimMST')


def prim(graph, search, v):
    """
    Args:
        search: La estructura de busqueda
        v: Vertice desde donde se relajan los pesos
    Returns:
        El grafo con los arcos relajados
    Raises:
        Exception
    """
    try:
        map.put(search['distTo'], v, 0.0)
        pq.insert(search['pq'], v, 0.0)
        while (not pq.isEmpty(search['pq'])):
            min = pq.delMin(search['pq'])
            scan(graph, search, min)
        return search
    except Exception as exp:
        error.reraise(exp, 'prim:prim')


def scan(graph, search, vertex):
    """
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
        map.put(search['marked'], vertex, True)
        edges = g.adjacentEdges(graph, vertex)
        for edge in lt.iterator(edges):
            w = e.other(edge, vertex)
            if (not map.get(search['marked'], w)['value']):
                if (e.weight(edge) < map.get(search['distTo'], w)['value']):
                    map.put(search['distTo'], w, e.weight(edge))
                    map.put(search['edgeTo'], w, edge)
                    if (pq.contains(search['pq'], w)):
                        pq.decreaseKey(search['pq'], w,
                                       map.get(search['distTo'], w)['value'])
                    else:
                        pq.insert(search['pq'], w,
                                  map.get(search['distTo'], w)['value'])
        return search
    except Exception as exp:
        error.reraise(exp, 'prim:scan')


def edgesMST(graph, search):
    """
    Args:
        search: La estructura de busqueda
        vertex: El vertice de destino
    Returns:
        Una pila con el camino entre source y vertex
    Raises:
        Exception
    """
    try:
        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            e = map.get(search['edgeTo'], vert)
            if (e is not None):
                q.enqueue(search['mst'], e['value'])
        return search
    except Exception as exp:
        error.reraise(exp, 'prim:edgesMST')


def weightMST(graph, search):
    weight = 0.0
    edgesMST(graph, search)
    edges = search['mst']
    for edge in lt.iterator(edges):
        weight = weight + e.weight(edge)
    return weight


def initSearch(graph):
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
               'edgeTo': None,
               'distTo': None,
               'marked': None,
               'pq': None,
               'mst': None
             }

        search['edgeTo'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      cmpfunction=graph['cmpfunction']
                                      )

        search['distTo'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      cmpfunction=graph['cmpfunction'])

        search['marked'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      cmpfunction=graph['cmpfunction']
                                      )

        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            map.put(search['distTo'], vert, math.inf)
            map.put(search['marked'], vert, False)

        search['pq'] = pq.newIndexMinPQ(cmpfunction=graph['cmpfunction'])
        search['mst'] = q.newQueue()

        return search

    except Exception as exp:
        error.reraise(exp, 'prim:init')
