"""
Este ADT representa una estructura de datos lineal, específicamente un arreglo dinámico (**Arraylist**). El arreglo dinámico es una estructura de datos que permite almacenar un conjunto de elementos del mismo tipo, en la cual se puede acceder y procesar sus elementos utilizando las funciones propias de la estructura.

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
class Arraylist(Generic[T]):
    """**Arraylist** representa la estructura de datos para arreglos dinamicos (*Arraylist*), Implementada con Generic[T] y @dataclass para que sea una estructura de datos genérica.

    Args:
        Generic (T): TAD (Tipo Abstracto de Datos) o ADT (Abstract Data Type) para una estructura de datos genéricas en python.

    Returns:
        Arraylist: ADT de tipo *Arraylist* o Arreglo Dinámico.

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
    Función de comparación personalizable por el usuario para reconocer los elementos dentro del *Arraylist*. Por defecto es la función *lt_dflt_cmp_function()* propia de *DataStructs*, puede ser un parametro al crear la estructura.
    """

    # using default_factory to generate an empty list
    # :attr: elements
    elements: List[T] = field(default_factory=list)
    """
    Lista nativa de Python que contiene los elementos de la estructura.
    """

    # the key is used to compare elements, not defined by default
    # :attr: key
    key: Optional[str] = None
    """
    Nombre de la llave personalizable por el usuario utilizada para reconocer los elementos dentro del *Arraylist*. Por defecto es la llave de diccionario (*dict*) *DFLT_DICT_KEY = 'id'* propia de *DataStructs*, puede ser un parametro al crear la estructura.
    """

    # by default, the list is empty
    # :attr: _size
    _size: int = 0
    """
    Es el número de elementos que contiene la estructura, por defecto es 0 y se actualiza con cada operación que modifica la estructura.
    """

    def __post_init__(self) -> None:
        """*__post_init__()* configura los parametros personalizados por el usuario al crear el *Arraylist*. En caso de no estar definidos, se asignan los valores por defecto, puede cargar listas nativas con el parametro *iodata* de python dentro de la estructura.
        """
        try:
            # if the key is not defined, use the default
            if self.key is None:
                self.key = DFLT_DICT_KEY     # its "id" by default
            # if the compare function is not defined, use the default
            if self.cmp_function is None:
                self.cmp_function = self.dflt_cmp_function
            # if elements are in a list, add them to the Arraylist
            if isinstance(self.iodata, VALID_IO_TYPE):
                for elm in self.iodata:
                    self.add_last(elm)
            self.iodata = None
        except Exception as err:
            self._handle_error(err)

    def dflt_cmp_function(self, elm1, elm2) -> int:
        """*dflt_cmp_function()* es la función de comparación por defecto para comparar elementos dentro del *Arraylist*, es una función crucial para que la estructura funcione correctamente.

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
        """*_handle_error()* función propia de la estructura que maneja los errores que se pueden presentar en el *Arraylist*.

        Si se presenta un error en *Arraylist*, se formatea el error según el contexto (paquete/módulo/clase), la función (método) que lo generó y lo reenvia al componente superior en la jerarquía *DataStructs* para manejarlo segun se considere conveniente el usuario.

        Args:
            err (Exception): Excepción que se generó en el *Arraylist*.
        """
        # TODO check readability of this function
        cur_context = self.__class__.__name__
        cur_function = inspect.currentframe().f_code.co_name
        error_handler(cur_context, cur_function, err)

    def _check_type(self, element: T) -> bool:
        """*_check_type()* función propia de la estructura que revisa si el tipo de dato del elemento que se desea agregar al *Arraylist* es del mismo tipo contenido dentro de los elementos del *Arraylist*.

        Args:
            element (T): elemento que se desea procesar en *Arraylist*.

        Returns:
            bool: operador que indica si el ADT *Arraylist* es del mismo tipo que el elemento que se desea procesar.

        Raises:
            TypeError: error si el tipo de dato del elemento que se desea agregar no es el mismo que el tipo de dato de los elementos que ya contiene el *Arraylist*.
        """
        # TODO check readability of this function
        # if the structure is not empty, check the first element type
        if not self.is_empty():
            # get the type of the first element
            lt_type = type(self.elements[0])
            # raise an exception if the type is not valid
            if not isinstance(element, lt_type):
                err_msg = f"Invalid data type: {type(lt_type)} "
                err_msg += f"for struct configured with {type(element)}"
                raise TypeError(err_msg)
        # otherwise, any type is valid
        return True

    def is_empty(self) -> bool:
        """*is_empty()* revisa si el *Arraylist* está vacío.

        Returns:
            bool: operador que indica si la estructura *Arraylist* está vacía.
        """
        try:
            return self.size() == 0
        except Exception as err:
            self._handle_error(err)

    def size(self) -> int:
        """*size()* devuelve el número de elementos que actualmente contiene el *Arraylist*.

        Returns:
            int: tamaño de la estructura *Arraylist*.
        """
        try:
            return self._size
        except Exception as err:
            self._handle_error(err)

    def add_first(self, element: T) -> None:
        """*add_first()* adiciona un elemento al inicio del *Arraylist*.

        Args:
            element (T): elemento que se desea agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                self.elements.insert(0, element)
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_last(self, element: T) -> None:
        """*add_last()* adiciona un elemento al final del *Arraylist*.

        Args:
            element (T): elemento que se desea agregar a la estructura.

        Raises:
            Exception: si la operación no se puede realizar, se invoca la función *_handle_error()* para manejar el error.
        """
        try:
            # if the element type is valid, add it to the list
            if self._check_type(element):
                self.elements.append(element)
                self._size += 1
        except Exception as err:
            self._handle_error(err)

    def add_element(self, element: T, pos: int) -> None:
        """*add_element()* adiciona un elemento en una posición especifica del *Arraylist*.

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
                        raise IndexError(f"Index {pos} is out of range")
                    self.elements.insert(pos, element)
                    self._size += 1
            else:
                raise IndexError("Empty data structure")
        except (TypeError, IndexError) as err:
            self._handle_error(err)

    def get_first(self) -> T:
        """*get_first()* lee el primer elemento del *Arraylist*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el primer elemento del *Arraylist*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            return self.elements[0]
        except Exception as err:
            self._handle_error(err)

    def get_last(self) -> T:
        """*get_last()* lee el último elemento del *Arraylist*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el ultimo elemento del *Arraylist*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            return self.elements[self.size() - 1]
        except Exception as err:
            self._handle_error(err)

    def get_element(self, pos: int) -> T:
        """*get_element()* lee un elemento en una posición especifica del *Arraylist*.

        Args:
            pos (int): posición del elemento que se desea leer.

        Raises:
            Exception: error si la estructura está vacía.
            Exception: error si la posición es inválida.

        Returns:
            T: el elemento en la posición especifica del *Arraylist*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError(f"Index {pos} is out of range")
            return self.elements[pos]
        except Exception as err:
            self._handle_error(err)

    def remove_first(self) -> T:
        """*remove_first()* elimina el primer elemento del *Arraylist*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el primer elemento eliminado del *Arraylist*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            element = self.elements.pop(0)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def remove_last(self) -> T:
        """*remove_last()* elimina el último elemento del *Arraylist*.

        Raises:
            Exception: error si la estructura está vacía.

        Returns:
            T: el ultimo elemento eliminado del *Arraylist*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            element = self.elements.pop(self.size() - 1)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def remove_element(self, pos: int) -> T:
        """*remove_element()* elimina un elemento en una posición especifica del *Arraylist*.

        Args:
            pos (int): posición del elemento que se desea eliminar.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición es inválida.

        Returns:
            T: el elemento eliminado del *Arraylist*.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif pos < 0 or pos > self.size() - 1:
                raise IndexError(f"Index {pos} is out of range")
            element = self.elements.pop(pos)
            self._size -= 1
            return element
        except Exception as err:
            self._handle_error(err)

    def compare_elements(self, elem1: T, elem2: T) -> int:
        """*compare_elements()* compara dos elementos dentro del *Arraylist* según la función de comparación de la estructura.

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
        """*find()* busca el elemento dentro del *Arraylist* y devuelve su posición o -1 si no lo encuentra.

        Args:
            element (T): elemento que se desea revisar en el *Arraylist*.

        Returns:
            int: la posición del elemento en el *Arraylist*, -1 si no está.
        """
        try:
            pos = -1
            if self.size() > 0:
                found = False
                i = 0
                while not found and i < self.size() - 1:
                    data = self.get_element(i)
                    if self.compare_elements(element, data) == 0:
                        found = True
                        pos = i
                    i += 1
            return pos
        except Exception as err:
            self._handle_error(err)

    def update(self, new_info: T, pos: int) -> None:
        """*update()* cambia la información de un elemento en la posición especificada del *Arraylist*.

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
                raise IndexError(f"Index {pos} is out of range")
            # if not self._check_type(new_info):
            elif self._check_type(new_info):
                # raise TypeError("Invalid element type")
                self.elements[pos] = new_info
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def exchange(self, pos1: int, pos2: int) -> None:
        """*exchange()* intercambia la información de dos elementos en dos posiciones especificadas del *Arraylist*.

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
                raise IndexError(f"Index {pos1} is out of range")
            elif pos2 < 0 or pos2 > self.size() - 1:
                raise IndexError(f"Index {pos2} is out of range")
            info_pos1 = self.get_element(pos1)
            info_pos2 = self.get_element(pos2)
            self.update(info_pos2, pos1)
            self.update(info_pos1, pos2)
        except Exception as err:
            self._handle_error(err)

    def sublist(self, start: int, end: int) -> "Arraylist[T]":
        """*sublist()* crea una sublista de la estructura según dos posiciones dentro del *Arraylist* original.

        Args:
            start (int): posición inicial de la sublista.
            end (int): posición final de la sublista.

        Raises:
            IndexError: error si la estructura está vacía.
            IndexError: error si la posición inicial o final son inválidas.

        Returns:
            Arraylist[T]: una sublista de la estructura original con la función de comparación y la llave de la estructura original.
        """
        try:
            if self.is_empty():
                raise IndexError("Empty data structure")
            elif start < 0 or end > self.size() - 1 or start > end:
                raise IndexError(f"Invalid range: between [{start}, {end}]")
            sub_lt = Arraylist(cmp_function=self.cmp_function,
                               key=self.key)
            i = start
            while i < end + 1:
                element = self.get_element(i)
                if self._check_type(element):
                    sub_lt.add_last(element)
                i += 1
            return sub_lt
        except (IndexError, TypeError) as err:
            self._handle_error(err)

    def concat(self, other: "Arraylist[T]") -> "Arraylist[T]":
        """*concat()* concatena dos estructuras de datos *Arraylist* para crear una estructura con los elementos de las dos estructuras.

        Args:
            other (Arraylist[T]): estructura de datos *Arraylist* que se desea concatenar con la estructura original.

        Raises:
            TypeError: error si la estructura que se desea concatenar no es un *Arraylist*.
            TypeError: error si la llave de la estructura que se desea unir no es la misma que la llave de la estructura original.
            TypeError: error si la función de comparación de la estructura que se desea unir no es la misma que la función de comparación de la estructura original.

        Returns:
            Arraylist[T]: Estructura de datos original *Arraylist* que contiene los elementos de las dos estructuras originales.
        """
        try:
            if not isinstance(other, Arraylist):
                err_msg = f"Structure is not an Arraylist: {type(other)}"
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
            # concatenate the elements of the two lists
            self.elements = self.elements + other.elements
            # update the size of the new list
            self._size = self.size() + other.size()
            return self
        except TypeError as err:
            self._handle_error(err)

    def clone(self) -> "Arraylist[T]":
        """*clone()* copia los elementos contenidos en estructura *Arraylist* en una nueva estructura. NO se usa *copy()* porque puede entrar en conflicto con la implementación nativa de Python.

        Returns:
            Arraylist[T]: copia independiente de la estructura *Arraylist* con la misma función de comparación y llave de la estructura original.
        """
        try:
            # create a new list
            copy_lt = Arraylist(cmp_function=self.cmp_function,
                                key=self.key)
            # add all the elements of the current list
            for element in self.elements:
                copy_lt.add_last(element)
            return copy_lt
        except Exception as err:
            self._handle_error(err)

    def __iter__(self):
        """*__iter__()* iterador nativo de Python personalizado para el *Arraylist*. Permite utilizar los ciclos *for* de Python para recorrer los elementos de la estructura.

        Returns:
            __iter__: iterador Python sobre los elementos del *Arraylist*.
        """
        try:
            return iter(self.elements)
        except Exception as err:
            self._handle_error(err)

    def __len__(self) -> int:
        """*__len__()* función nativa de Python personalizada para el *Arraylist*. Permite utilizar la función *len()* de Python para recuperar el tamaño del *Arraylist*.

        Returns:
            int: tamaño del *Arraylist*.
        """
        return self._size

    def __add__(self, other: "Arraylist[T]") -> "Arraylist[T]":
        """*__add__()* función nativa de Python personalizada para el *Arraylist*. Permite utilizar el operador + par
        a concatenar dos estructuras de datos *Arraylist*.

        Args:
            other (Arraylist[T]): estructura de datos *Arraylist* que se desea concatenar con la estructura original.

        Returns:
            Arraylist[T]: Estructura de datos original *Arraylist* que contiene los elementos de las dos estructuras originales.
        """
        return self.concat(other)
