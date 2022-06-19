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
from DISClib.DataStructures import adjlist as g
from DISClib.ADT import list as lt
from DISClib.ADT import map as map
from DISClib.ADT import stack as stk
from DISClib.Utils import error as error
assert config


def DepthFirstSearch(graph, source):
    """
    Genera un recorrido DFS sobre el grafo graph
    Args:
        graph:  El grafo a recorrer
        source: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    try:
        search = {
                  'source': source,
                  'visited': None,
                  }

        search['visited'] = map.newMap(numelements=g.numVertices(graph),
                                       maptype='PROBING',
                                       comparefunction=graph['comparefunction']
                                       )

        map.put(search['visited'], source, {'marked': True, 'edgeTo': None})
        dfsVertex(search, graph, source)
        return search
    except Exception as exp:
        error.reraise(exp, 'dfs:DFS')


def dfsVertex(search, graph, vertex):
    """
    Funcion auxiliar para calcular un recorrido DFS
    Args:
        search: Estructura para almacenar el recorrido
        vertex: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    try:
        adjlst = g.adjacents(graph, vertex)
        for w in lt.iterator(adjlst):
            visited = map.get(search['visited'], w)
            if visited is None:
                map.put(search['visited'],
                        w, {'marked': True, 'edgeTo': vertex})
                dfsVertex(search, graph, w)
        return search
    except Exception as exp:
        error.reraise(exp, 'dfs:dfsVertex')


def hasPathTo(search, vertex):
    """
    Indica si existe un camino entre el vertice source
    y el vertice vertex
    Args:
        search: Estructura de recorrido DFS
        vertex: Vertice destino
    Returns:
        True si existe un camino entre source y vertex
    Raises:
        Exception
    """
    try:
        element = map.get(search['visited'], vertex)
        if element and element['value']['marked'] is True:
            return True
        return False
    except Exception as exp:
        error.reraise(exp, 'dfs:hasPathto')


def pathTo(search, vertex):
    """
    Retorna el camino entre el vertices source y el
    vertice vertex
    Args:
        search: La estructura con el recorrido
        vertex: Vertice de destingo
    Returns:
        Una pila con el camino entre el vertices source y el
        vertice vertex
    Raises:
        Exception
    """
    try:
        if hasPathTo(search, vertex) is False:
            return None
        path = stk.newStack()
        while vertex != search['source']:
            stk.push(path, vertex)
            vertex = map.get(search['visited'], vertex)['value']['edgeTo']
        stk.push(path, search['source'])
        return path
    except Exception as exp:
        error.reraise(exp, 'dfs:pathto')
