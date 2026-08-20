"""
Demo de EDA (Estructuras de datos y algoritmos) 2026-20
Python 3.12
Aqui implemento estructuras de datos lineales de tres formas:
    1) usando dict() y codigo funcional
    2) usando @dataclass en codigo funcional
    3) usando @dataclass en codigo orientado a objetos

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# import python libs
# from typing import Any, Callable
from collections.abc import Callable
from typing import Any, TypeVar, Optional
from dataclasses import dataclass, field

# Type for the element stored in the list
# :data: T: TypeVar
T = TypeVar("T")

# ==========================================
# ========= ONE: DICT + FUNCIONAL ==========
# ==========================================
def dflt_cmp_func(a: dict, b: dict, key: str="_id") -> int:
    """dflt_cmp_func is a default comparison function for comparing two dictionaries based on a specified key. 

    Args:
        a (dict): The first dictionary to compare.
        b (dict): The second dictionary to compare.
        key (str, optional): The key to compare based on. Defaults to "_id".

    Returns:
        int: -1 if a[key] < b[key], 0 if a[key] == b[key], 1 if a[key] > b[key].
    """
    if a[key] < b[key]:
        return -1
    elif a[key] > b[key]:
        return 1
    else:
        return 0

def dflt_cmp_func_alt(a: Any, b: Any) -> int:
    """dflt_cmp_func_alt is a default comparison function for comparing two values. 

    Args:
        a (Any): The first value to compare.
        b (Any): The second value to compare.

    Returns:
        int: -1 if a < b, 0 if a == b, 1 if a > b.
    """
    if a < b:
        return -1
    elif a > b:
        return 1
    # else:
    return 0


# def new_lt(cmp_func: Optional[Callable] = None, key: str="_id") -> dict:
def new_lt(cmp_func: Callable | None = None, key: str="_id") -> dict:

    _lt_struct = {
        "elements": [],
        "size": 0,
        "type": "ARRAY_LT",
        "cmp_func": cmp_func,
        "key": key
    }
    # TODO add the default cmp_func
    if _lt_struct["cmp_func"] is None:
        _lt_struct["cmp_func"] = dflt_cmp_func

    return _lt_struct

def is_empty(lt: dict) -> bool:
    """is_empty is a function to know if the list is empty

    Args:
        lt (dict): dictionary representing an array list.

    Returns:
        bool: True if the list is empty, False otherwise.
    """
    return lt.get("size") == 0

def size(lt: dict) -> int:
    """size _summary_

    Args:
        lt (dict): _description_

    Returns:
        int: _description_
    """
    return lt.get("size")

def add_first(lt: dict, elm: Any) -> None:
    """add_first _summary_

    Args:
        lt (dict): _description_
        elm (Any): _description_
    """
    lt.get("elements").insert(0, elm)
    lt["size"] += 1


def get_first(lt: dict) -> Any:

    if lt.get("size") > 0:
        return lt.get("elements")[0]
    raise IndexError("get_first: List is empty")
    # return None


def remove_first(lt: dict) -> Any:

    if lt.get("size") == 0:
        # raise IndexError("remove_first: List is empty")
        return None
    lt.get("elements").pop(0)
    lt["size"] -= 1
    return lt


def demo_dict_struct(lt: list) -> None:
    """demo_dict_struct demonstrates the usage of a linear data structure implemented using a dictionary and functional programming.

    Args:
        lt (list): _description_
    """
    print("Demo de estructura de datos lineal usando dict() y codigo funcional")
    print("===============================================================")
    # nueva lista
    print("Creando una lista vacia")
    my_list = new_lt()

    # detalles
    print(f"\nLista creada: {my_list}")
    print(f"Lista vacia? {is_empty(my_list)}")
    print(f"Tamaño de la lista: {size(my_list)}")

    # tipo de estructura
    print(f"tipo de la estructura: {type(my_list)}")

    # agregando elementos
    print("\nAgregando elementos a la lista")
    for elm in lt:
        add_first(my_list, elm)
        print(f"\tElemento agregado: {elm}")
        print(f"\tLista actual: {my_list}")
        print(f"\tTamaño de la lista: {size(my_list)}")

    # recuperando y removiendo elementos
    print("\nObteniendo el primer elemento de la lista")
    first_elm = get_first(my_list)
    print(f"Primer elemento: {first_elm}")
    print("\nRemoviendo el primer elemento de la lista")
    remove_first(my_list)
    print(f"Lista actual: {my_list}")
    print(f"Tamaño de la lista: {size(my_list)}")

# ==========================================
# ====== ONE: @DATACLASS + FUNCIONAL =======
# ==========================================
@dataclass
class array_lt_func:

    elements: list = field(default_factory=list)
    size: int = 0
    cmp_func: Callable | None = None
    key: str = "_id"

    def __len__(self):
        return self.size

    def __iter__(self):
        """__iter__ is the python native iterator function for the array list, allowing iteration over its elements.

        Returns:
            iter: An iterator for the elements in the array list.
        """
        return iter(self.elements)


def size_alt(lt:array_lt_func) -> int:
    """size _summary_

    Args:
        lt (array_lt_func): _description_

    Returns:
        int: _description_
    """
    return lt.size


def is_empty_alt(lt:array_lt_func) -> bool:
    """is_empty _summary_

    Args:
        lt (array_lt_func): _description_

    Returns:
        bool: _description_
    """
    return lt.size == 0


def add_first_alt(lt:array_lt_func, elm: Any) -> None:
    """add_first _summary_

    Args:
        lt (array_lt_func): _description_
        elm (Any): _description_
    """
    lt.elements.insert(0, elm)
    lt.size += 1


def get_first_alt(lt:array_lt_func) -> Any:
    """get_first _summary_

    Args:
        lt (array_lt_func): _description_

    Returns:
        Any: _description_
    """
    if lt.size > 0:
        return lt.elements[0]
    # raise IndexError("get_first: List is empty")
    return None


def remove_first_alt(lt:array_lt_func) -> Any:
    """remove_first _summary_

    Args:
        lt (array_lt_func): _description_

    Returns:
        Any: _description_
    """
    if lt.size == 0:
        # raise IndexError("remove_first: List is empty")
        return None
    elm = lt.elements.pop(0)
    lt.size -= 1
    return elm


def demo_array_lt_alt(lt:list) -> None:
    """demo_array_lt_alt demonstrates the usage of a linear data structure implemented using a dataclass and functional programming.

    Args:
        lt (list): _description_
    """
    print("Demo de estructura de datos lineal usando @dataclass y codigo funcional")
    print("=====================================================================")
    # nueva lista
    print("Creando una lista vacia")
    my_list = array_lt_func()
    my_list.cmp_func = dflt_cmp_func

    # detalles
    print(f"\nLista creada: {my_list}")
    print(f"Lista vacia? {is_empty_alt(my_list)}")
    print(f"Tamaño de la lista: {size_alt(my_list)}")

    # tipo de estructura
    print(f"tipo de la estructura: {type(my_list)}")

    # agregando elementos
    print("\nAgregando elementos a la lista")
    for elm in lt:
        add_first_alt(my_list, elm)
        print(f"\tElemento agregado: {elm}")
        print(f"\tLista actual: {my_list}")
        print(f"\tTamaño de la lista: {size_alt(my_list)}")

    # recuperando y removiendo elementos
    print("\nObteniendo el primer elemento de la lista")
    first_elm = get_first_alt(my_list)
    print(f"Primer elemento: {first_elm}")
    print("\nRemoviendo el primer elemento de la lista")
    remove_first_alt(my_list)
    print(f"Lista actual: {my_list}")
    print(f"Tamaño de la lista: {size_alt(my_list)}")    

# ==========================================
# ======= ONE: @DATACLASS + OBJETOS ========
# ==========================================
@dataclass
class array_list:
    """array_list is a data class representing a linear data structure (array list) with elements, size, type, comparison function, and key.

    Attributes:
        elements (list): A list to store the elements of the array list.
        size (int): The number of elements in the array list.
        type (str): The type of the data structure, default is "ARRAY_LT".
        cmp_func (Callable): A comparison function for comparing elements.
        key (str): The key to compare based on when using dictionaries.
    """
    elements: list = field(default_factory=list)
    _size: int = 0
    cmp_func: Callable | None = None
    key: str = "_id"

    def __iter__(self):
        """__iter__ is the python native iterator function for the array list, allowing iteration over its elements.

        Returns:
            iter: An iterator for the elements in the array list.
        """
        return iter(self.elements)

    def __len__(self) -> int:
        """__len__ is the python native length function for the array list, returning the number of elements in the list.

        Returns:
            int: The number of elements in the array list.
        """
        return self._size
    
    @property
    def size(self) -> int:
        """size property returns the number of elements in the array list.

        Returns:
            int: The number of elements in the array list.
        """
        return self._size
    
    @size.setter
    def size(self, val:int) -> None:
        """size setter sets the number of elements in the array list.

        Args:
            val (int): The new size for the array list.
        """
        self._size = val

    @property
    def first(self) -> Any:
        """first property returns the first element in the array list.

        Returns:
            Any: The first element in the array list, or None if the list is empty.
        """
        if self._size > 0:
            return self.elements[0]
        # raise IndexError("first: List is empty")
        return None

    @first.setter
    def first(self, val:Any) -> None:
        """first setter sets the first element in the array list.

        Args:
            val (Any): The new first element for the array list.
        """
        if self._size > 0:
            self.elements[0] = val

    def add_first(self, elm: Any) -> None:
        """add_first adds an element to the beginning of the array list.

        Args:
            elm (Any): The element to add to the array list.
        """
        self.elements.insert(0, elm)
        self._size += 1

    def remove_first(self) -> Any:
        """remove_first removes and returns the first element from the array list.

        Returns:
            Any: The removed first element, or None if the list is empty.
        """
        if self._size == 0:
            return None
        elm = self.elements.pop(0)
        self._size -= 1
        return elm


# Main function call to run the program
if __name__ == '__main__':
    demo_lt = [
        {"_id": 1, "name": "Alice", "age": 30},
        {"_id": 2, "name": "Bob", "age": 25},
        {"_id": 3, "name": "Charlie", "age": 35},
    ]
    # demo_dict_struct(demo_lt)
    demo_array_lt_alt(demo_lt)
    