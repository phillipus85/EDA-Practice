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
from DISClib.ADT import stack as st
from DISClib.ADT import map as map
from DISClib.ADT import graph as g
from DISClib.Utils import error as error
assert config


def DirectedCycle(graph):
    """
    Detecta ciclos en un grafo dirigido
    Args:
        graph: El grafo de busqueda

    Returns:
        El ciclo si existe
    Raises:
        Exception
    """
    try:
        search = initStructures(graph)

        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            if (not map.get(search['marked'], vert)['value']):
                dfs(graph, search, vert)
        return search

    except Exception as exp:
        error.reraise(exp, 'directedcycle')


def dfs(graph, search, v):
    """
    DFS
    Args:
        search: La estructura de busqueda
        v: Vertice desde donde se relajan los pesos
    Returns:
        El grafo
    Raises:
        Exception
    """
    try:
        map.put(search['marked'], v, True)
        map.put(search['onStack'], v, True)
        edges = g.adjacentEdges(graph, v)
        for edge in lt.iterator(edges):
            w = e.other(edge, v)
            if (not st.isEmpty(search['cycle'])):
                return search
            elif ((not map.get(search['marked'], w)['value'])):
                map.put(search['edgeTo'], w, edge)
                dfs(graph, search, w)
            elif (map.get(search['onStack'], w)['value']):
                f = edge
                while (e.either(f) != w):
                    st.push(search['cycle'], f)
                    f = map.get(search['edgeTo'], e.either(f))['value']
                st.push(search['cycle'], f)
                return search
        map.put(search['onStack'], v, False)
    except Exception as exp:
        error.reraise(exp, 'cycle:dfs')


def hasCycle(search):
    return not st.isEmpty(search['cycle'])


def cycle(search):
    return search['cycle']


def initStructures(graph):
    """

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
               'marked': None,
               'onStack': None,
               'cycle': None
             }

        search['edgeTo'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      cmpfunction=graph['cmpfunction']
                                      )

        search['marked'] = map.newMap(numelements=g.numVertices(graph),
                                      maptype='PROBING',
                                      cmpfunction=graph['cmpfunction'])

        search['onStack'] = map.newMap(numelements=g.numVertices(graph),
                                       maptype='PROBING',
                                       cmpfunction=graph['cmpfunction']
                                       )

        search['cycle'] = st.newStack()

        vertices = g.vertices(graph)
        for vert in lt.iterator(vertices):
            map.put(search['marked'], vert, False)
            map.put(search['onStack'], vert, False)

        return search

    except Exception as exp:
        error.reraise(exp, 'cycle:init')
