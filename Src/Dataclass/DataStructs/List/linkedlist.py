"""
Este ADT representa una estructura de datos lineal, específicamente una lista sensillamente enlazada/encadenada (**SingleLinked**). Esta estructura de datos es una secuencia de nodos enlazados, donde cada nodo contiene un elemento de información y una referencia al siguiente nodo en la secuencia. Esto le permite a la lista un crecimiento y reducción dinámico en la memoria disponible.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# native python modules
# import dataclass to define the array list
from dataclasses import dataclass
# import modules for defining the element's type in the array
from typing import List, Optional, Callable, Generic
# import inspect for getting the name of the current function
import inspect

# custom modules
# node class for the linked list
from Src.Dataclass.DataStructs.List.ltnode import SingleNode
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
class SingleLinked(Generic[T]):
    """**SingleLinked** representa una estructura de datos dinámica de tipo lista sensillamente encadenada (*SingleLinked*), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        SingleLinked: ADT de tipo *SingleLinked* o Lista Sensillamente Encadenada.
    """
    # input elements from python list
    # :attr: iodata
    iodata: Optional[List[T]] = None
    """
    Lista nativa de Python personalizable por el usuario para inicializar la estructura. Por defecto es *None* y el usuario puede incluirla como argumento al crear la estructura.
    """

    # the cmp_function is used to compare elements, not defined by default
    # :attr: cmp_function
    cmp_function: Optional[Callable[[T, T], int]] = None
    """
    Función de comparación personalizable por el usuario para reconocer los elementos dentro del *SingleLinked*. Por defecto es la función *lt_dflt_cmp_function()* propia de *DataStructs*, puede ser un parametro al crear la estructura.
    """

    # reference to the first node of the list
    # :attr: first
    first: Optional[SingleNode[T]] = None
    """
    Representa la referencia en memoria al primer nodo del *SingleLinked*.
    """

    # reference to the last node of the list
    # :attr: last
    last: Optional[SingleNode[T]] = None
    """
    Representa la referencia en memoria al último nodo del *SingleLinked*.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave personalizable por el usuario utilizada para reconocer los elementos dentro del *SingleLinked*. Por defecto es la llave de diccionario (*dict*)*DFLT_DICT_KEY = 'id'* propia de *DataStructs*, puede ser un parametro al crear la estructura.
    """

    # by default, the list is empty
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los parametros personalizados por el usuario al crear el *SingleLinked*. En caso de no estar definidos, se asignan los valores por defecto, puede cargar listas nativas con el parametro *iodata* de python dentro de la estructura.
        """
        try:
            # counter for elements in the input list
            # i = 0
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DFLT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.dflt_cmp_function
            # if the list is empty, the first and last are the same and None
            if self.first is None:
                self.last = self.first
            # if input data is iterable add them to the SingleLinkedList
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def dflt_cmp_function(self, elm1, elm2) -> int:
        """*dflt_cmp_function()* es la función de comparación por defecto para comparar elementos dentro del *SingleLinked*, es una función crucial para que la estructura funcione correctamente.

        Args:
            elm1 (Any): primer elemento a comparar.
            elm2 (Any): segundo elemento a comparar.

        Returns:
            int: respuesta de la comparación entre los elementos, 0 si son iguales, 1 si elm1 es mayor que elm2, -1 si elm1 es menor.
        """
        # TODO check the usability of the try, except block
        try:
            # passing self,key as the first argument to the default cmp function
            return lt_dflt_cmp_function(self.key, elm1, elm2)
        except Exception as err:
            self._handle_error(err)

    def _handle_error(self, err: Exception) -> None:
        """*_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *SingleLinked*.

        Si se presenta un error en *SingleLinked*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DataStructs* para manejarlo segun se considere conveniente el usuario.

        Args:
            err (Exception): Excepción que se generó en el *SingleLinked*.
        """
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función propia de la estructura que revisa si el tipo de dato del elemento que se desea agregar al *SingleLinked* es del mismo tipo contenido dentro de los elementos del *SingleLinked*.

        Args:
            element (T): elemento que se desea procesar en *SingleLinked*.

        Raises:
            TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *SingleLinked*.

        Returns:
            bool: operador que indica si el ADT *SingleLinked* es del mismo tipo que el elemento que se desea procesar.
        """
        # if the structure is not empty, check the first element type
        if not self.is_empty():
            # get the type of the first element
            lt_type = type(self.first.get())
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for struct configured with {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    def is_empty(self) -> bool:
        """*is_empty()* revisa si el *SingleLinked* está vacío.

        Returns:
            bool: operador que indica si la estructura *SingleLinked* está vacía.
        """
        # ALTERNATIVE:
        # return self.first is None
        return self.size() == 0

    def size(self) -> int:
        """*size()* devuelve el número de elementos que actualmente contiene el *SingleLinked*.

        Returns:
            int: tamaño de la estructura *SingleLinked*.
        """
        return self._size

    def add_first(self, element: T) -> None:
        """*add_first()* adiciona un elemento al inicio del *SingleLinked*.

        Args:
            element (T): elemento que se desea agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node with the element
                new_node = SingleNode(element)
                # ALTERANTIVE:
                # new_node = SingleNode()
                # new_node.set(element)

                # the new node points to the first node
                new_node._next = self.first
                # set the new node as the first node
                self.first = new_node
                if self.size() == 0:
                    # if the list is empty, the last node is the first node
                    self.last = self.first

                # ALTERNATIVE:
                # if self.is_empty():
                #     self.last = self.first
                # increase the size of the list
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """*add_last()* adiciona un elemento al final del *SingleLinked*.

        Args:
            element (T): elemento que se desea agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                # create a new node
                new_node = SingleNode(element)
                if self.size() == 0:
                    self.first = new_node
                else:
                    self.last._next = new_node
                self.last = new_node
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """*add_element()* adiciona un elemento en una posición especifica del *SingleLinked*.

        Args:
            element (T): elemento que se desea agregar a la estructura.
            pos (int): posición en la que se desea agregar el elemento.

        Raises:
            IndexError: error si la posición es inválida.
            IndexError: error si la estructura está vacía.
        """
        try:
            if not self.is_empty():
                if self._check_type(element):
                    if pos < 0 or pos > self.size():
                        raise IndexError("Position is out of range")
                    # create a new node
                    new_node = SingleNode(element)
                    # if the list is empty, add the element to the first
                    if self.size() == 0:
                        self.first = new_node
                        self.last = new_node
                    # if the position is the first, add it to the first
                    elif self.size() > 0 and pos == 0:
                        new_node._next = self.first
                        self.first = new_node
                    # if the position is the last, add it to the last
                    elif self.size() > 0 and pos == self.size() - 1:
                        self.last._next = new_node
                        self.last = new_node
                    else:
                        i = 0
                        current = self.first
                        previous = self.first
                        while i < pos + 1:
                            previous = current
                            current = current.next()
                            i += 1
                        new_node._next = current
                        previous._next = new_node
                    self._size += 1
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

    def get_first(self) -> Optional[T]:
        """*get_first()* lee el primer elemento del *SingleLinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el primer elemento del *SingleLinked*.
        """
        try:
            data = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.first is not None:
                data = self.first.get()
            return data
        except Exception as err:
            self._handle_error(err)

    def get_last(self) -> Optional[T]:
        """*get_last()* lee el último elemento del *SingleLinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el ultimo elemento del *SingleLinked*.
        """
        try:
            data = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.last is not None:
                data = self.last.get()
            return data
        except Exception as err:
            self._handle_error(err)

    def get_element(self, pos: int) -> Optional[T]:
        """*get_element()* lee un elemento en una posición especifica del *SingleLinked*.

        Args:
            pos (int): posición del elemento que se desea leer.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición es inválida.

        Returns:
             Optional[T]: el elemento en la posición especifica del *SingleLinked*.
        """
        try:
            data = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError("Index", pos, "is out of range")
            else:
                current = self.first
                i = 0
                # TODO check algorithm with "while i != pos:"
                while i != pos:
                    current = current.next()
                    i += 1
                data = current.get()
            return data
        except Exception as err:
            self._handle_error(err)

    def remove_first(self) -> Optional[T]:
        """*remove_first()* elimina el primer elemento del *SingleLinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
             Optional[T]: el primer elemento eliminado del *SingleLinked*.
        """
        try:
            data = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.size() > 0 and self.first is not None:
                temp = self.first.next()
                node = self.first
                self.first = temp
                self._size -= 1
                if self.size() == 0:
                    self.last = None
                    self.first = None
                data = node.get()
            return data
        except Exception as err:
            self._handle_error(err)

    def remove_last(self) -> Optional[T]:
        """*remove_last()* elimina el último elemento del *SingleLinked*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            Optional[T]: el ultimo elemento eliminado del *SingleLinked*.
        """
        try:
            data = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if self.size() > 0 and self.last is not None:
                if self.first == self.last:
                    node = self.first
                    self.last = None
                    self.first = None
                else:
                    temp = self.first
                    while temp.next() != self.last:
                        temp = temp.next()
                    node = self.last
                    self.last = temp
                    self.last._next = None
                self._size -= 1
                data = node.get()
            return data
        except Exception as err:
            self._handle_error(err)

    def remove_element(self, pos: int) -> Optional[T]:
        """*remove_element()* elimina un elemento en una posición especifica del *SingleLinked*.

        Args:
            pos (int): posición del elemento que se desea eliminar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.

        Returns:
            Optional[T]: el elemento eliminado del *SingleLinked*.
        """
        try:
            data = None
            if self.is_empty():
                raise IndexError("Empty data structure")
            if pos < 0 or pos > self.size() - 1:
                raise IndexError(f"Index {pos} is out of range")
            current = self.first
            prev = self.first
            i = 0
            if pos == 0:
                data = self.first.get()
                self.first = self.first.next()
            elif pos >= 1:
                # TODO check algorithm with "while i != pos:"
                while i != pos:
                    prev = current
                    current = current.next()
                    i += 1
                prev._next = current.next()
                data = current.get()
            self._size -= 1
            return data
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """*compare_elements()* compara dos elementos dentro del *SingleLinked* según la función de comparación de la estructura.

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
        """*find()* busca el elemento dentro del *SingleLinked* y devuelve su posición o -1 si no lo encuentra.

        Args:
            element (T): elemento que se desea revisar en el *SingleLinked*.

        Returns:
            int: la posición del elemento en el *SingleLinked*, -1 si no está.
        """
        try:
            pos = -1
            if self.size() > 0:
                node = self.first
                found = False
                i = 0
                while not found and i < self.size():
                    data = node.get()
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
                    if node.next() is not None:
                        node = node.next()
            return pos
        except Exception as err:
            self._handle_error(err)

    def update(self, new_info: T, pos: int) -> None:
        """*update()* cambia la información de un elemento en la posición especificada del *SingleLinked*.

        Args:
            new_info (T): nueva información que se desea para el elemento.
            pos (int): posición del elemento que se desea cambiar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError("Index", pos, "is out of range")
            # if not self._check_type(new_info):
            elif self._check_type(new_info):
                # raise TypeError("Invalid element type")
                current = self.first
                i = 0
                while i != pos:
                    current = current.next()
                    i += 1
                current.set(new_info)
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def exchange(self, pos1: int, pos2: int) -> None:
        """*exchange()* intercambia la información de dos elementos en dos posiciones especificadas del *SingleLinked*.

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
            info_pos1 = self.get_element(pos1)
            info_pos2 = self.get_element(pos2)
            self.change_info(info_pos2, pos1)
            self.change_info(info_pos1, pos2)
        except Exception as err:
            self._handle_error(err)

    def sublist(self, start: int, end: int) -> "SingleLinked[T]":
        """*sublist()* crea una sublista de la estructura según dos posiciones dentro del *SingleLinked* original.

        Args:
            start (int): posición inicial de la sublista.
            end (int): posición final de la sublista.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición inicial o final son inválidas.

        Returns:
            SingleLinked[T]: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self.size() - 1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = SingleLinked(cmp_function=self.cmp_function,
                                  key=self.key)
            i = 0
            current = self.first
            while i != end + 1:
                if i >= start:
                    sub_lt.add_last(current.get())
                current = current.next()
                i += 1
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "SingleLinked[T]") -> "SingleLinked[T]":
        """*concat()* concatena dos estructuras de datos *SingleLinked* para crear una estructura con los elementos de las dos estructuras.

        Args:
            other (SingleLinked[T]): estructura de datos *SingleLinked* que se desea concatenar con la estructura original.

        Raises:
            TypeError: error si la estructura que se desea concatenar no es un *SingleLinked*.
            TypeError: error si la llave de la estructura que se desea unir no es la misma que la llave de la estructura original.
            TypeError: error si la función de comparación de la estructura que se desea unir no es la misma que la función de comparación de la estructura original.

        Returns:
            SingleLinked[T]: Estructura de datos original *SingleLinked* que contiene los elementos de las dos estructuras originales.
        """
        try:
            if not isinstance(other, SingleLinked):
                err_msg = f"Structure is not an SingleLinked: {type(other)}"
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
            # concatenate the two lists
            self.last._next = other.first
            self.last = other.last
            # update the size
            self._size = self.size() + other.size()
            return self
        except TypeError as err:
            self._handle_error(err)

    def clone(self) -> "SingleLinked[T]":
        """*clone()* crea una copia de la estructura de datos *SingleLinked* en una nueva estructura. NO se usa *copy()* porque puede entrar en conflicto con la implementación nativa de Python.

        Returns:
            SingleLinked[T]: copia de la estructura de datos *SingleLinked* con la misma función de comparación y llave de la estructura original.
        """
        try:
            copy_lt = SingleLinked(cmp_function=self.cmp_function,
                                   key=self.key)
            current = self.first
            while current is not None:
                copy_lt.add_last(current.get())
                current = current.next()
            return copy_lt
        except Exception as err:
            self._handle_error(err)

    def __iter__(self):
        """*__iter__()* iterador nativo de Python personalizado para el *SingleLinked*. Permite utilizar los ciclos *for* de Python para recorrer los elementos de la estructura.

        Returns:
            __iter__: iterador Python sobre los elementos del *SingleLinked*.
        """
        try:
            # TODO do I need the try/except block?
            current = self.first
            while current is not None:
                yield current.get()
                current = current.next()
        except Exception as err:
            self._handle_error(err)

    def __len__(self) -> int:
        """*__len__()* función nativa de Python personalizada para el *SingleLinked*. Permite utilizar la función *len()* de Python para recuperar el tamaño del *SingleLinked*.

        Returns:
            int: tamaño del *SingleLinked*.
        """
        return self.size()
