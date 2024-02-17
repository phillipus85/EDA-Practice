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
import importlib
assert config

"""
Este archivo contiene la implementación del TAD grafo no dirigido
"""


def newGraph(datastructure="ADJ_LIST",
             directed=False,
             size=10,
             cmpfunction=None
             ):
    """
    Crea un grafo vacio

    Args:
        size: Tamaño inicial del grafo
        cmpfunction: Funcion de comparacion
        directed: Indica si el grafo es dirigido o no
        datastructure: Estructura de datos utilizada
    Returns:
        Un nuevo grafo vacío
    Raises:
        Exception
    """
    gr = graphSelector(datastructure)
    return gr.newGraph(size, cmpfunction,  directed, datastructure, gr)


def insertVertex(graph, vertex):
    """
    Inserta el vertice vertex en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea insertar
    Returns:
        El grafo graph con el nuevo vertice
    Raises:
        Exception
    """
    return graph['datastructure'].insertVertex(graph, vertex)


def removeVertex(graph, vertex):
    """
    Remueve el vertice vertex del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea remover
    Returns:
        El grafo sin el vertice vertex
    Raises:
        Exception
    """
    return graph['datastructure'].removeVertex(graph, vertex)


def numVertices(graph):
    """
    Retorna el numero de vertices del  grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices del grafo
    Raises:
        Exception
    """
    return graph['datastructure'].numVertices(graph)


def numEdges(graph):
    """
    Retorna el numero de arcos en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices del grafo
    Raises:
        Exception
    """
    return graph['datastructure'].numEdges(graph)


def vertices(graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        La lista con los vertices del grafo
    Raises:
        Exception
    """
    return graph['datastructure'].vertices(graph)


def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        Una lista con los arcos del grafo
    Raises:
        Exception
    """
    return graph['datastructure'].edges(graph)


def degree(graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    return graph['datastructure'].degree(graph, vertex)


def outdegree(graph, vertex):
    """
    Retorna el numero de arcos que salen del grafo vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    return graph['datastructure'].outdegree(graph, vertex)


def indegree(graph, vertex):
    """
    Retorna el numero de arcos que llegan al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    return graph['datastructure'].indegree(graph, vertex)


def getEdge(graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice destino

    Returns:
        El arco que une los verices vertexa y vertexb
    Raises:
        Exception
    """
    return graph['datastructure'].getEdge(graph, vertexa, vertexb)


def addEdge(graph, vertexa, vertexb, weight=0):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
    Si el grafo es no dirigido se adiciona dos veces el mismo arco,
    en el mismo orden
    Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice de destino
        wight: peso del arco

    Returns:
       El grafo con el nuevo arco
    Raises:
        Exception
    """
    return graph['datastructure'].addEdge(graph, vertexa, vertexb, weight)


def containsVertex(graph, vertex):
    """
    Retorna si el vertice vertex esta presente en el grafo

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: Vertice que se busca

    Returns:
       True si el vertice esta presente
    Raises:
        Exception
    """
    return graph['datastructure'].containsVertex(graph, vertex)


def adjacents(graph, vertex):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de adyacencias
    Raises:
        Exception
    """
    return graph['datastructure'].adjacents(graph, vertex)


def adjacentEdges(graph, vertex):
    """
    Retorna una lista con todos los arcos asociados a los vértices
    adyacentes de vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de arcos adyacentes
    Raises:
        Exception
    """
    return graph['datastructure'].adjacentEdges(graph, vertex)


"""
Selector dinamico de la estructua de datos solicitada
"""

switch_module = {
    "ADJ_LIST": ".adjlist",
    "ADJ_MTX": ".adjlist",
}


def graphSelector(datastructure):
    """
    Carga dinamicamente el import de la estructura de datos
    seleccionada
    """
    ds = switch_module.get(datastructure)
    module = importlib.import_module(ds, package="DISClib.DataStructures")
    return module
