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
from DISClib.ADT import map as map
from DISClib.ADT import list as lt
from DISClib.DataStructures import edge as e
from DISClib.Utils import error as error
assert config

"""
Este código está basado en las implementaciones propuestas en:
- Algorithms, 4th Edition.  R. Sedgewick
- Data Structures and Algorithms in Java, 6th Edition.  Michael Goodrich
"""


def newGraph(size, cmpfunction, directed, type, datastructure):
    """
    Crea un grafo vacio

    Args:
        size: Tamaño inicial del grafo
        cmpfunction: Funcion de comparacion
        directed: Indica si el grafo es dirigido o no
    Returns:
        Un nuevo grafo vacío
    Raises:
        Exception
    """
    try:
        graph = {'vertices': None,
                 'edges': 0,
                 'type': type,
                 'cmpfunction': cmpfunction,
                 'directed': directed,
                 'indegree': None,
                 'datastructure': datastructure
                 }
        graph['vertices'] = map.newMap(numelements=size,
                                       maptype='PROBING',
                                       cmpfunction=cmpfunction)
        if (directed):
            graph['indegree'] = map.newMap(numelements=size,
                                           maptype='PROBING',
                                           cmpfunction=cmpfunction)
        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:newgraph')


def insertVertex(graph, vertex):
    """
    Inserta el vertice vertex en el grafo graph SI no existe en el grafo
    NO se acepta un vertice repetido.

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea insertar
    Returns:
        El grafo graph con el nuevo vertice
    Raises:
        Exception
    """
    try:
        # Validacion que el vertice NO existe
        if not containsVertex(graph, vertex):
            edges = lt.newList('SINGLE_LINKED', e.compareedges) # incluye funcion comparacion arcos
            map.put(graph['vertices'], vertex, edges)
            if (graph['directed']):
                map.put(graph['indegree'], vertex, 0)
        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:insertvertex')


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
    # TODO
    pass


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
    try:
        return map.size(graph['vertices'])
    except Exception as exp:
        error.reraise(exp, 'ajlist:numtvertex')


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
    try:
        return (graph['edges'])
    except Exception as exp:
        error.reraise(exp, 'ajlist:numedges')


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
    try:
        lstmap = map.keySet(graph['vertices'])
        return lstmap
    except Exception as exp:
        error.reraise(exp, 'ajlist:vertices')


def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo graph
    Para un grafo No Dirigido, un arco que conecte 2 vertices solo debe aparecer una vez en la lista.

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        Una lista con los arcos del grafo
    Raises:
        Exception
    """
    try:
        lstmap = map.valueSet(graph['vertices'])
        lstresp = lt.newList('SINGLE_LINKED', e.compareedges)
        for lstedge in lt.iterator(lstmap):
            for edge in lt.iterator(lstedge):
                if (graph['directed']):
                    lt.addLast(lstresp, edge)
                else: # caso Grafo No Dirigido
                    vertexA = e.either(edge)
                    vertexB = e.other(edge, vertexA)
                    invertedEdge = e.newEdge(vertexB, vertexA, e.weight(edge))
                    if (not lt.isPresent(lstresp, edge)) and (not lt.isPresent(lstresp, invertedEdge)):
                        # Entre dos vertices que exista un arco, incluir unicamente un arco que los conecte 
                        lt.addLast(lstresp, edge)
        return lstresp
    except Exception as exp:
        error.reraise(exp, 'ajlist:edges')


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
    try:
        element = map.get(graph['vertices'], vertex)
        lst = element['value']
        return (lt.size(lst))
    except Exception as exp:
        error.reraise(exp, 'ajlist:degree')


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
    try:
        if (graph['directed']):
            degree = map.get(graph['indegree'], vertex)
            return degree['value']
        return 0
    except Exception as exp:
        error.reraise(exp, 'ajlist:indegree')


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
    try:
        if (graph['directed']):
            element = map.get(graph['vertices'], vertex)
            lst = element['value']
            return (lt.size(lst))
        return 0
    except Exception as exp:
        error.reraise(exp, 'ajlist:outdegree')


def getEdge(graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb
    El arco debe existir en la misma direccion vertexa -> vertexb
    en caso de grafo dirigido o grafo No dirigido

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice destino

    Returns:
        El arco que une los verices vertexa y vertexb
        None si No existe el arco.
    Raises:
        Exception
    """
    try:
        element = map.get(graph['vertices'], vertexa)
        if element is None:  # NO existe vertexa
            return None
        lst = element['value']
        for edge in lt.iterator(lst):
            if (e.either(edge) == vertexa and
                e.other(edge, e.either(edge)) == vertexb):
                return edge
        return None
    except Exception as exp:
        error.reraise(exp, 'ajlist:getedge')


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
    try:
        return map.get(graph['vertices'], vertex) is not None
    except Exception as exp:
        error.reraise(exp, 'ajlist:containsvertex')


def addEdge(graph, vertexa, vertexb, weight=0):
    """
    Si alguno de los vertices NO existe(n):
    1. NO se agrega el arco
    Si los vertices existen y el arco YA existe:
    1. Se reemplaza el peso del arco (NO se acepta arcos paralelos)
    Si los vertices existen y si el arco NO existe:
    1. Agrega el arco vertexa->vertexb, con peso weight, al vertice vertexa
    2. Adicionalmente, si el grafo es NO Dirigido,
    se agrega el arco vertexb->vertexa, con peso weight, al vertice vertexb.

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice de destino
        weight: peso del arco

    Returns:
       El grafo con el nuevo arco
    Raises:
        Exception
    """
    try:
        # Se consulta la informacion de cada vertice
        entrya = map.get(graph['vertices'], vertexa)           
        entryb = map.get(graph['vertices'], vertexb)
        if entrya == None or entryb == None:
            return graph
        # Se agrega el caso de validacion cuando el arco YA existe
        edge = getEdge(graph, vertexa, vertexb)
        if edge is not None:  # caso arco YA existe
            e.set_weight(edge, weight)
            if ((not graph['directed']) and (vertexa != vertexb)):
                inv_edge = getEdge(graph, vertexb, vertexa)
                e.set_weight(inv_edge, weight)
        else:  # caso arco NO existe
            # Se crea el arco
            edge = e.newEdge(vertexa, vertexb, weight)
            # Se anexa a cada lista el arco correspondiente
            lt.addLast(entrya['value'], edge)
            if not graph['directed']:
                if vertexa != vertexb:
                    inv_edge = e.newEdge(vertexb, vertexa, weight)
                    lt.addLast(entryb['value'], inv_edge)
            else:
                degree = map.get(graph['indegree'], vertexb)
                map.put(graph['indegree'], vertexb, degree['value']+1)
            graph['edges'] += 1

        return graph
    except Exception as exp:
        error.reraise(exp, 'ajlist:addedge')


def adjacents(graph, vertex):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex
    Si el vertice No existe se retorna una lista vacia.

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de adyacencias
    Raises:
        Exception
    """
    try:
        lstresp = lt.newList()
        element = map.get(graph['vertices'], vertex)
        if element is not None:
            lst = element['value']
            for edge in lt.iterator(lst):
                lt.addLast(lstresp, e.other(edge, vertex))
            
        return lstresp
    except Exception as exp:
        error.reraise(exp, 'ajlist:adjacents')


def adjacentEdges(graph, vertex):
    """
    Retorna una lista con todos los arcos asociados a los vértices
    adyacentes de vertex
    Si el vertice No existe se retorna una lista vacia.

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de arcos adyacentes
    Raises:
        Exception
    """
    try:
        element = map.get(graph['vertices'], vertex)
        lst = lt.newList()
        if element is not None:
            lst = element['value']
        return lst
    except Exception as exp:
        error.reraise(exp, 'ajlist:adjacentEdges')
