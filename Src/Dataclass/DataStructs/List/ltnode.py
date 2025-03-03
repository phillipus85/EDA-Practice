"""
Este ADT representa un nodo **Node** de información de una estructura de datos dinámica, las cuales pueden ser: listas sencillas, listas doblemente encadenadas, pilas, colas, BST, RBT, entre otras.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


# native python modules
# import dataclass for defining the node class
from dataclasses import dataclass
# import modules for defining the Node type
from typing import Generic, Optional

# custom modules
# generic error handling and type checking
from Src.Dataclass.Utils.default import T

# checking custom modules
assert T


@dataclass
class Node(Generic[T]):
    """**Node** Es el ADT que representar la información de un nodo de una estructura de datos dinámica y las funciones basicas para acceder a ella. Puede utilizarse para representar un nodo de una lista sencilla o doblemente encadenada.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        Node: ADT de tipo *Node* o nodo de información.
    """
    # optional information of any type
    # :attr: _data
    _data: Optional[T] = None
    """
    Es la información contenida en el nodo.
    """

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función propia de la estructura que verifica que la información de *Node* sea del tipo adecuado.

        Args:
            element (T): elemento que se desea procesar en *Node*.

        Raises:
            TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *Node*.

        Returns:
            bool: operador que indica si el ADT *Node* es del mismo tipo que el elemento que se desea procesar.
        """
        if not isinstance(element, type(self._data)):
            err_msg = f"Invalid data type: {type(self._data)} "
            err_msg += f"for struct configured with {type(element)}"
            raise TypeError(err_msg)
        return True

    def set(self, data: T) -> None:
        """*set()* establece la información de *Node*.

        Args:
            data (T): información que se desea actualizar en *Node*.
        """
        if self._data is not None:
            self._check_type(data)
        self._data = data

    def get(self) -> T:
        """*get()* recupera la información de *Node*.

        Returns:
            T: información de *Node*.
        """
        return self._data


@dataclass
class SingleNode(Node, Generic[T]):
    """**SingleNode** representa un nodo de una lista sencillamente encadenada. Basada en el ADT *Node* que contiene la información del nodo.

    Args:
        Node (dataclass): ADT base para implementar un nodo con información genérica.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        SingleNode: ADT para un *SingleNode* o nodo para una lista sencillamente encadenada.
    """
    # optional reference to the next node of the same type
    # :attr: _next
    _next: Optional["SingleNode[T]"] = None
    """
    Referencia al siguiente nodo de la lista.
    """

    def next(self) -> Optional["SingleNode[T]"]:
        """*next()* recupera la referencia el siguiente nodo de la lista. Si no existe retorna *None*.

        Returns:
            Optional[SingleNode[T]]: referencia al siguiente *Node* de la lista si existe.
        """
        return self._next


@dataclass
class DoubleNode(SingleNode, Generic[T]):
    """**DoubleNode** representa un nodo de una lista doblemente encadenada. Basada en el ADT *SingleNode* que contiene la información del nodo.

    Args:
        SingleNode (Dataclass): ADT base para implementar un nodo con información genérica.
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        DoubleNode: ADT para un *DoubleNode* o nodo para una lista doblemente encadenada.
    """
    # optional reference to the previous node of the same type
    # :attr: _prev
    _prev: Optional["DoubleNode[T]"] = None
    """
    Referencia al anterior nodo anterior de la lista.
    """

    def prev(self) -> Optional["DoubleNode[T]"]:
        """*prev()* recupera la referencia al anterior *DoubleNode* de la lista. Si no existe retorna *None*.

        Returns:
            Optional[DoubleNode[T]]: referencia al anterior *DoubleNode* si existe.
        """
        return self._prev
