"""
Este ADT representa una estructura de datos lineal, específicamente una lista doblemente enlazada/encadenada (**Doublelinked**). Esta estructura de datos es una secuencia de nodos enlazados, donde cada nodo contiene un elemento de información, una referencia al siguiente, y al anterior nodo en la secuencia. Esto le permite a la lista un crecimiento y reducción dinámico en la memoria disponible.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass, field
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect

# custom modules
# node class for the linked list
from Src.Dataclass.DataStructs.Lists.ltnode import DLLTNode
# generic error handling and type checking
from Src.Dataclass.Utils.error import error_handler
from Src.Dataclass.Utils.default import lt_dflt_cmp_function
from Src.Dataclass.Utils.default import T
from Src.Dataclass.Utils.default import DFLT_DICT_KEY
from Src.Dataclass.Utils.default import VALID_IO_TYPE

# checking custom modules
assert error_handler
assert lt_dflt_cmp_function
assert T
assert DFLT_DICT_KEY
assert VALID_IO_TYPE


@dataclass
class Doublelinked(Generic[T]):
    """**Doublelinked** representa una estructura de datos para una lista doblemente enlazada/encadenada (*Doublelinked*). Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        Doublelinked: ADT de tipo *Doublelinked* o Lista Doblemente Encadenada.
    """
    # input elements from python list
    # :param iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación personalizable por el usuario para reconocer los elementos dentro del *Doublelinked*. Por defecto es la función *lt_dflt_cmp_function()* propia de *DataStructs*, puede ser un parametro al crear la estructura.
    """

    # reference to the header node of the list, DLLTNode by default
    # :attr: _header
    _header: Optional[DLLTNode[T]] = field(
        default_factory=lambda: DLLTNode())
    """
    Representa el nodo sentinela de la cabecera de la estructura (header), por defecto es un *DLLTNode* vacío.
    """
    # reference to the trailer node of the list, DLLTNode by default
    # :attr: _trailer
    _trailer: Optional[DLLTNode[T]] = field(
        default_factory=lambda: DLLTNode())
    """
    Representa el nodo sentinela del colero de la estructura (trailer), por defecto es un *DLLTNode* vacío.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave personalizable por el usuario utilizada para reconocer los elementos dentro del *Doublelinked*. Por defecto es la llave de diccionario (*dict*) *DFLT_DICT_KEY = 'id'* propia de *DataStructs*, puede ser un parametro al crear la estructura.
    """

    # by default, the list is empty, -1 for the header and trailer nodes
    # :attr: _size
    _size: int = -1
    """
    Es el número de elementos que contiene la estructura, por defecto es 0, en algunos casos es -1 para ajustar por los nodos sentinelas de la estructura.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los parametros personalizados por el usuario al crear el *Doublelinked*. En caso de no estar definidos, se asignan los valores por defecto, puede cargar listas nativas con el parametro *iodata* de python dentro de la estructura.
        """
        try:
            # Link sentinel nodes
            self._header._next = self._trailer
            self._trailer._prev = self._header
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DFLT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.dflt_cmp_function
            # if input data is iterable add them to the Doublelinked
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def dflt_cmp_function(self, elm1, elm2) -> int:
        """*dflt_cmp_function()* es la función de comparación por defecto para comparar elementos dentro del *Doublelinked*, es una función crucial para que la estructura funcione correctamente.

        Args:
            elm1 (Any): primer elemento a comparar.
            elm2 (Any): segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
        """
        try:
            # passing self as the first argument to simulate a method
            return lt_dflt_cmp_function(self.key, elm1, elm2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *Doublelinked*.

        Si se presenta un error en *Doublelinked*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DataStructs* para manejarlo segun se considere conveniente el usuario.

        Args:
            err (Exception): Excepción que se generó en el *Doublelinked*.
        """
        # TODO check usability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función propia de la estructura que revisa si el tipo de dato del elemento que se desea agregar al *Doublelinked* es del mismo tipo contenido dentro de los elementos del *Doublelinked*.

        Args:
            element (T): elemento que se desea procesar en *Doublelinked*.

        Raises:
            TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *Doublelinked*.

        Returns:
            bool: operador que indica si el ADT *Doublelinked* es del mismo tipo que el elemento que se desea procesar.
        """
        # TODO check usability of this function
        # if the structure is not empty, check the header element type
        if not self.is_empty() and self._header.next().info is not None:
            # get the type of the next element to the header
            lt_type = type(self._header.next().get_info())
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for struct configured with {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    # @property
    def is_empty(self) -> bool:
        """*is_empty()* revisa si el *Doublelinked* está vacío.

        Returns:
            bool: operador que indica si la estructura *Doublelinked* está vacía.
        """
        try:
            # TODO complete the code
            pass
        except Exception as err:
            self._handle_error(err)

    # @property
    def size(self) -> int:
        """*size()* devuelve el número de elementos que actualmente contiene el *Doublelinked*.

        Returns:
            int: tamaño de la estructura *Doublelinked*.
        """
        try:
            # TODO complete the code
            pass
        except Exception as err:
            self._handle_error(err)

    def add_first(self, element: T) -> None:
        """*add_first()* adiciona un elemento al inicio del *Doublelinked*.

        Args:
            element (T): elemento que se desea agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # TODO complete the code
                pass
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """*add_last()* adiciona un elemento al final del *Doublelinked*.

        Args:
            element (T): elemento que se desea agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # TODO complete the code
                pass
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """*add_element()* adiciona un elemento en una posición especifica del *Doublelinked*.

        Args:
            element (T): elemento que se desea agregar a la estructura.
            pos (int): posición en la que se desea agregar el elemento.

        Raises:
            IndexError: error si la posición es inválida.
            IndexError: error si la estructura está vacía.
        """
        try:
            if not self.is_empty():
                # TODO complete the code
                pass
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

    def get_first(self) -> Optional[T]:
        """*get_first()* lee el primer elemento del *Doublelinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el primer elemento del *Doublelinked*.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._header.next() is not None:
                # TODO complete the code
                pass
            return info
        except Exception as err:
            self._handle_error(err)

    def get_last(self) -> Optional[T]:
        """*get_last()* lee el último elemento del *Doublelinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el ultimo elemento del *Doublelinked*.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self._trailer.prev() is not None:
                # TODO complete the code
                pass
            return info
        except Exception as err:
            self._handle_error(err)

    def get_element(self, pos: int) -> Optional[T]:
        """*get_element()* lee un elemento en una posición especifica del *Doublelinked*.

        Args:
            pos (int): posición del elemento que se desea leer.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición es inválida.

        Returns:
             Optional[T]: el elemento en la posición especifica del *Doublelinked*.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError("Index", pos, "is out of range")
            else:
                # TODO complete the code
                pass
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_first(self) -> Optional[T]:
        """*remove_first()* elimina el primer elemento del *Doublelinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el primer elemento eliminado del *Doublelinked*.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.size() > 0 and self._header.next() is not None:
                # TODO complete the code
                pass
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_last(self) -> Optional[T]:
        """*remove_last()* elimina el último elemento del *Doublelinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el ultimo elemento eliminado del *Doublelinked*.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.size() > 0 and self._trailer.prev() is not None:
                # TODO complete the code
                pass
            return info
        except Exception as err:
            self._handle_error(err)

    def remove_element(self, pos: int) -> Optional[T]:
        """*remove_element()* elimina un elemento en una posición especifica del *Doublelinked*.

        Args:
            pos (int): posición del elemento que se desea eliminar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.

        Returns:
            Optional[T]: el elemento eliminado del *Doublelinked*.
        """
        try:
            info = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if pos < 0 or pos > self.size() - 1:
                raise IndexError(f"Index {pos} is out of range")
            # Determine where to start based on the position
            # if there is only one element, link the sentinel nodes
            # TODO complete the code
            pass
            return info
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """*compare_elements()* compara dos elementos dentro del *Doublelinked* según la función de comparación de la estructura.

        Args:
            elem1 (T): Primer elemento a comparar.
            elem2 (T): Segundo elemento a comparar.

        Raises:
            TypeError: error si la función de comparación no está definida.

        Returns:
            int: -1 si elem1 es menor que elem2, 0 si son iguales, 1 si elem1 es mayor que elem2.
        """
        try:
            # use the structure cmp function
            if self.cmp_function is not None:
                return self.cmp_function(elem1, elem2)
            # raise an exception if the cmp function is not defined
            raise TypeError("Undefined compare function!!!")
        except Exception as err:
            self._handle_error(err)

    def find(self, element: T) -> int:
        """*find()* busca el elemento dentro del *Doublelinked* y devuelve su posición o -1 si no lo encuentra.

        Args:
            element (T): elemento que se desea revisar en el *Doublelinked*.

        Returns:
            int: la posición del elemento en el *Doublelinked*, -1 si no está.
        """
        try:
            pos = -1
            if self.size() > 0:
                # setting the current node by the header
                # TODO complete the code
                pass
            return pos
        except Exception as err:
            self._handle_error(err)

    def update(self, new_info: T, pos: int) -> None:
        """*update()* cambia la información de un elemento en la posición especificada del *Doublelinked*.

        Args:
            new_info (T): nueva información que se desea para el elemento.
            pos (int): posición del elemento que se desea cambiar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.
        """
        # TODO change the method name to "change_data()" or "update()"?
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError("Index", pos, "is out of range")
            # if not self._check_type(new_info):
            elif self._check_type(new_info):
                # TODO complete the code
                pass
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def exchange(self, pos1: int, pos2: int) -> None:
        """*exchange()* intercambia la información de dos elementos en dos posiciones especificadas del *Doublelinked*.

        Args:
            pos1 (int): posición del primer elemento.
            pos2 (int): posición del segundo elemento.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición del primer elemento es inválida.
            Exception: error si la posición del segundo elemento es inválida.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos1 < 0 or pos1 > self.size() - 1:
                raise IndexError("Index", pos1, "is out of range")
            elif pos2 < 0 or pos2 > self.size() - 1:
                raise IndexError("Index", pos2, "is out of range")
            # TODO complete the code
            pass
        except Exception as err:
            self._handle_error(err)

    def sublist(self, start: int, end: int) -> "Doublelinked[T]":
        """*sublist()* crea una sublista de la estructura según dos posiciones dentro del *Doublelinked* original.

        Args:
            start (int): posición inicial de la sublista.
            end (int): posición final de la sublista.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición inicial o final son inválidas.

        Returns:
            Doublelinked[T]: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self.size() - 1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = Doublelinked(cmp_function=self.cmp_function,
                                  key=self.key)
            # TODO complete the code
            pass
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "Doublelinked[T]") -> "Doublelinked[T]":
        """*concat()* concatena dos estructuras de datos *Doublelinked* para crear una estructura con los elementos de las dos estructuras.

        Args:
            other (Doublelinked[T]): estructura de datos *Doublelinked* que se desea concatenar con la estructura original.

        Raises:
            TypeError: error si la estructura que se desea concatenar no es un *Doublelinked*.
            TypeError: error si la llave de la estructura que se desea unir no es la misma que la llave de la estructura original.
            TypeError: error si la función de comparación de la estructura que se desea unir no es la misma que la función de comparación de la estructura original.

        Returns:
            Doublelinked[T]: Estructura de datos original *Doublelinked* que contiene los elementos de las dos estructuras originales.
        """
        try:
            if not isinstance(other, Doublelinked):
                err_msg = f"Structure is not an Doublelinked: {type(other)}"
                raise TypeError(err_msg)
            if self.key != other.key:
                raise TypeError(f"Invalid key: {self.key} != {other.key}")
            # checking functional code of the cmp function
            code1 = self.cmp_function.__code__.co_code
            code2 = other.cmp_function.__code__.co_code
            if code1 != code2:
                err_msg = f"Invalid compare function: {self.cmp_function}"
                err_msg += f" != {other.cmp_function}"
                raise TypeError(err_msg)

            # Link the last node with the first node of the other list
            # TODO complete the code
            return self
        except TypeError as err:
            self._handle_error(err)

    def clone(self) -> "Doublelinked[T]":
        """*clone()* crea una copia de la estructura de datos *Doublelinked*.

        Returns:
            Doublelinked[T]: copia de la estructura de datos *Doublelinked*.
        """
        try:
            copy_lt = Doublelinked(cmp_function=self.cmp_function,
                                   key=self.key)
            # TODO complete the code
            return copy_lt
        except Exception as err:
            self._handle_error(err)

    def __iter__(self):
        """*__iter__()* iterador nativo de Python personalizado para el *Doublelinked*. Permite utilizar los ciclos *for* de Python para recorrer los elementos de la estructura en orden ascendente.

        Returns:
            __iter__: iterador Python sobre los elementos del *Doublelinked*.
        """
        try:
            # FIXME do I need the try/except block?
            # TODO complete the code
            pass
        except Exception as err:
            self._handle_error(err)

    def __reversed__(self):
        """*__reversed__* iterador nativo de Python personalizado para el *Doublelinked*. Permite utilizar los ciclos *for* de Python para recorrer los elementos de la estructura en orden descendente.

        Yields:
            iterator: iterador Python sobre los elementos del *Doublelinked*.
        """
        try:
            # FIXME do I need the try/except block?
            # TODO complete the code
            pass
        except Exception as err:
            self._handle_error(err)

    def __len__(self) -> int:
        """*__len__()* función nativa de Python personalizada para el *Doublelinked*. Permite utilizar la función *len()* de Python para recuperar el tamaño del *Doublelinked*.

        Returns:
            int: tamaño del *Doublelinked*.
        """
        return self.size()
