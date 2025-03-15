"""
**test_arraylist** es el módulo que prueba el ADT *Arraylist* con sus respectivas funciones para su uso dinámico y configurable dentro de *DataStructs*.
"""

# impoting testing framework
import unittest
import pytest
import random

# importing the classes to test
from Src.DataStructs.List.arraylist import Arraylist

# importing the data to test the classes
from Test.Data.test_data import get_list_test_data

# asserting module existence
assert Arraylist
assert get_list_test_data

# list of keys to ignore in the global parameters
# :data: IGNORE_KEYS_LT: list
IGNORE_KEYS_LT = (
    "CHECK_ERR_LT",
    "CHECK_TYPE_LT",
    "TEST_AL_LT"
)
"""
Lista de llaves a ignorar en los parámetros globales en las pruebas.
"""


# @pytest.fixture(scope="module")
def cmp_lt_test_function(elm1: dict, elm2: dict) -> int:
    """*cmp_lt_test_function()* función de comparación personalizada para probar la función de las estructuras de tipo listas (*Arraylist*, *Singlelinked*, *DoubleLinked*). Solo funciona con diccionarios con una llave "uuid".

    Args:
        elm1 (dict): primer elemento a comparar.
        elm2 (dict): segundo elemento a comparar.

    Raises:
        Exception: error si la llave no está presente en ambos elementos.
        Exception: error si la comparación es inválida.

    Returns:
        int: devuelve 1 si el primer elemento es mayor que el segundo, -1 si el primer elemento es menor que el segundo, 0 si son iguales.
    """
    key = "uuid"
    key1 = elm1.get(key)
    key2 = elm2.get(key)
    # check if the key is present in both elements
    if None in [key1, key2]:
        raise Exception("Invalid key")
    # comparing elements
    else:
        # if one is greater than the other, return 1
        if key1 > key2:
            return 1
        # if one is less than the other, return -1
        elif key1 < key2:
            return -1
        # if they are equal, return 0
        elif key1 == key2:
            return 0
        # otherwise, raise an exception
        else:
            raise Exception("Invalid comparison")


class TestArraylist(unittest.TestCase):
    """**TestArraylist** clase *unittest* para probar la estructura *Arraylist* de *DataStructs*.

    Args:
        unittest (TestCase): clase *unittest.TestCase* para las pruebas unitarias en Python.
    """

    @pytest.fixture(autouse=True)
    def inject_fixtures(self):
        """*inject_fixtures()* inyecta los parámetros globales de prueba para *Arraylist* como un *fixture* para todas las pruebas con *pytest*.
        """
        self.global_params = get_list_test_data()
        # FIXME do we need this? is this okey?
        TEST_ARRAY_LIST_LT = list()
        for i in self.global_params.get("TEST_INT_LT"):
            temp_lt = self.global_params.get("TEST_DICT_LT")
            tal = Arraylist(temp_lt)
            TEST_ARRAY_LIST_LT.append(tal)
        self.global_params["TEST_AL_LT"] = TEST_ARRAY_LIST_LT

    def test_default_arraylist(self):
        """*test_default_arraylist()* prueba en inicializar un arreglo dinámico *Arraylist* vacío con sus valores por predeterminados.
        """
        # Test an empty Arraylist
        ar_lt = Arraylist()
        # Test if Arraylist is not None
        assert ar_lt is not None
        # Test if Arraylist is empty
        assert ar_lt._size == 0
        # Test if Arraylist elements is empty
        assert ar_lt.elements == []
        # Test if Arraylist key is "id"
        assert ar_lt.key == "id"
        # Test if Arraylist cmp_function is the default
        assert ar_lt.cmp_function == ar_lt.dflt_cmp_function
        # Test if Arraylist is an instance of Arraylist
        assert isinstance(ar_lt, Arraylist)

    def test_default_cmp_function(self):
        """*test_default_cmp_function()* prueba para la función de comparación predeterminada de *Arraylist* con diferentes tipos de elementos.
        """
        # create a new empty Arraylist with the default cmp function
        ar_lt = Arraylist()
        # iterate over tglobal params and use the default cmp function
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result of the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = ar_lt.dflt_cmp_function(ce, pe) in exp_res
                        res2 = ar_lt.dflt_cmp_function(ce, ce) in exp_res
                        res3 = ar_lt.dflt_cmp_function(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_custom_arraylist(self):
        """*test_custom_arraylist()* prueba para inicializar un arreglo dinámico *Arraylist* con elementos de diferentes tipos.
        """
        # getting the global variables
        data_type_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, data_type in zip(self.global_params.keys(), data_type_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(test_data)
                # test for the Arraylist is not None
                assert ar_lt is not None
                # test for the Arraylist elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the Arraylist key is "id"
                assert ar_lt.key == "id"
                # test for the Arraylist cmp_function is the default
                assert ar_lt.cmp_function == ar_lt.dflt_cmp_function
                # test for the Arraylist is an instance of Arraylist
                assert isinstance(ar_lt, Arraylist)
                # test for the Arraylist elements are of the same type
                assert isinstance(ar_lt.elements[0], data_type)
                # test for the Arraylist size is equal to test_data
                assert ar_lt._size == len(test_data)

    def test_custom_key(self):
        """*test_custom_key()* prueba para inicializar un arreglo dinámico o *Arraylist* con elementos de diferentes tipos y una llave personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                ar_lt = Arraylist(iodata=test_data,
                                  key="uuid")
                # test for the Arraylist is not None
                assert ar_lt is not None
                # test for the Arraylist size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the Arraylist elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the Arraylist key is "uuid"
                assert ar_lt.key == "uuid"
                # test for the Arraylist cmp_function is the default
                assert ar_lt.cmp_function == ar_lt.dflt_cmp_function
                # test for the Arraylist is an instance of Arraylist
                assert isinstance(ar_lt, Arraylist)
                # test for the Arraylist elements are of the same type
                assert isinstance(ar_lt.elements[0], dtype)

    def test_custom_cmp_function(self):
        """*test_custom_cmp_function()* prueba inicializar un arreglo dinámico o *Arraylist* con elementos de diferentes tipos y una función de comparación personalizada.
        """
        # getting the global variables
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # iterate over tglobal params and create single linked list node
        for key, dtype in zip(self.global_params.keys(), dtype_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                ar_lt = Arraylist(iodata=test_data,
                                  cmp_function=cmp_lt_test_function)
                # test for the Arraylist is not None
                assert ar_lt is not None
                # test for the Arraylist size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the Arraylist elements is equal to test_data
                assert ar_lt.elements == test_data
                # test for the Arraylist key is the default "id"
                assert ar_lt.key == "id"
                # test for the Arraylist cmp_function is the custom function
                assert ar_lt.cmp_function == cmp_lt_test_function
                # test for the Arraylist is an instance of Arraylist
                assert isinstance(ar_lt, Arraylist)
                # test for the Arraylist elements are of the same type
                assert isinstance(ar_lt.elements[0], dtype)

    def test_size(self):
        """*test_size()* prueba la función *size()* de *Arraylist* con estructuras de datos vacías y no vacías.
        """

        # create a new empty Arraylist
        ar_lt = Arraylist()
        # test for the Arraylist size is 0 with size method
        assert ar_lt.size() == 0
        # test for the Arraylist size is 0 with _size attribute
        assert ar_lt._size == 0
        # check if the Arraylist elements is empty
        assert ar_lt.elements == []

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # getting the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # test for the Arraylist size() is equal to test_data
                assert ar_lt.size() == len(test_data)
                # test for the Arraylist _size is equal to test_data
                assert ar_lt._size == len(test_data)
                # test for the Arraylist elements is equal to test_data
                assert ar_lt.elements == test_data

    def test_is_empty(self):
        """*test_is_empty()* prueba la función *is_empty()* de *Arraylist* con estructuras de datos vacías y no vacías."""
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # test for the Arraylist is empty
        assert ar_lt.is_empty() is True
        # test for the Arraylist elements is empty
        assert ar_lt.elements == []

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # test for the Arraylist is not empty
                assert ar_lt.is_empty() is False
                # test for the Arraylist elements is equal to test_data
                assert ar_lt.elements == test_data

    def test_add_first(self):
        """*test_add_first()* prueba la función *add_first()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si el elemento añadido esta en el índice 0 de *Arraylist*.
        """
        # testing type handling
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                with pytest.raises(TypeError) as excinfo:
                    ar_lt = Arraylist(test_data)
                    # induce the error by adding an element of a different type
                    ar_lt.add_first(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_first method normal behavior
                ar_lt = Arraylist()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the Arraylist
                    ar_lt.add_first(t_data)
                    # get the first element of the Arraylist
                    t_elem = ar_lt.get_first()
                    # test for the Arraylist get_first() is equal to test_data
                    assert t_elem == t_data
                    # test if the Arraylist size is equal to test_len
                    assert (ar_lt.size() == i + 1)

    def test_add_last(self):
        """*test_add_last()* prueba la función *add_last()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *TypeError* para tipos de datos no compatibles. También comprueba si el elemento añadido esta en el índice final de *Arraylist*.
        """
        # testing type handling
        # getting the global variables
        # type error test data list
        type_err_lt = self.global_params.get("CHECK_ERR_LT")
        # data type list
        dtype_lt = self.global_params.get("CHECK_TYPE_LT")
        # global params keys
        param_keys = self.global_params.keys()

        # iterate over the type error list and create a node for each type
        for key, dtype, err in zip(param_keys, dtype_lt, type_err_lt):
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                with pytest.raises(TypeError) as excinfo:
                    ar_lt = Arraylist(test_data)
                    # induce the error by adding an element of a different type
                    ar_lt.add_last(err)
                # assert the type error is raised
                assert "Invalid data type" in str(excinfo.value)
                # assert the node info is the same type as test_data
                assert isinstance(test_data[0], dtype)
                # assert the node info is not the same type as err
                assert dtype != err

                # testing add_lat method normal behavior
                ar_lt = Arraylist()
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the first element of the test data
                    t_data = test_data[i]
                    # add the element to the Arraylist
                    ar_lt.add_last(t_data)
                    # get the first element of the Arraylist
                    t_elem = ar_lt.get_last()
                    # test for the Arraylist get_last() is equal to test_data
                    assert t_elem == t_data
                    # test if the Arraylist size is equal to test_len
                    assert (ar_lt.size() == i + 1)

    def test_add_element(self):
        """*test_add_element()* prueba la función *add_element()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* y *TypeError* para estructuras de datos vacías y tipos de datos no compatibles. También comprueba si el elemento añadido esta en el índice adecuado del *Arraylist*.
                """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.add_element(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the add_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    ar_lt.add_element(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the Arraylist
                ar_lt.add_element(t_data, i)
                # get the added element in the index of the Arraylist
                t_elem = ar_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the Arraylist size is equal to test_len
                assert (ar_lt.size() == (test_len + 1))

    def test_get_first(self):
        """*test_get_first()* prueba la función *get_first()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento recuperado es el primero del *Arraylist*.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # test for the Arraylist get_first() is equal to test_data
                assert ar_lt.get_first() == test_data[0]
                # test if Arraylist size() is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_get_last(self):
        """*test_get_last()* prueba la función *get_last()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento recuperado es el último del *Arraylist*.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_last method
        with pytest.raises(Exception) as excinfo:
            ar_lt.get_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # test for the Arraylist get_last() is equal to test_data
                assert ar_lt.get_last() == test_data[-1]
                # test if Arraylist size() is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_get_element(self):
        """*test_get_element()* prueba la función *get_element()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento recuperado es el mismo que originalmente se encontraba en el índice.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.get_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)

                # test get_element with an out-of-range index
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len, test_len * 2)
                    ar_lt.get_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # test for get_element(i) is equal to test_data[i]
                    assert ar_lt.get_element(i) == test_data[i]
                    # test if Arraylist size() is equal to test_len
                    assert (ar_lt.size() == test_len)

    def test_remove_first(self):
        """*test_remove_first()* prueba la función *remove_first()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento eliminado es el mismo que originalmente al inicio del *Arraylist*.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.remove_first()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                for i in range(0, len(test_data) - 1):
                    t_data = test_data[i]
                    t_elem = ar_lt.remove_first()
                    # test if the removed element is equal to the first
                    assert t_elem == t_data
                    # test if the Arraylist size is equal to test_len
                    assert (ar_lt.size() == (test_len - i - 1))

    def test_remove_last(self):
        """*test_remove_last()* prueba la función *remove_last()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías. También comprueba si el elemento eliminado es el mismo que originalmente al final del *Arraylist*.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_first method
        with pytest.raises(Exception) as excinfo:
            ar_lt.remove_last()
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # get the last element of the test data

                    t_data = test_data[test_len - 1 - i]
                    # remove the last element of the Arraylist
                    t_elem = ar_lt.remove_last()
                    # test if the removed element is equal to the last
                    assert t_elem == t_data
                    # test if the Arraylist size is equal to test_len
                    assert (ar_lt.size() == (test_len - i - 1))

    def test_remove_element(self):
        """*test_remove_element()* prueba la función *remove_element()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento eliminado es el mismo que originalmente se encontraba en el índice y la estructura de datos no se ha modificado mas allá de la longitud original.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.remove_element(i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)

                # force an exception in the get_element method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * -1, -1)
                    ar_lt.remove_element(i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # remove the element in the index of the Arraylist
                t_elem = ar_lt.remove_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the Arraylist size is equal to test_len
                assert (ar_lt.size() == (test_len - 1))

    def test_compare_elements(self):
        """*test_compare_elements()* prueba la función *compare_elements()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *TypeError* para funciones de comparación no definidas. También comprueba si la comparación es válida para los elementos de la estructura de datos.
        """
        ar_lt = Arraylist()
        # delete the default cmp function
        ar_lt.cmp_function = None
        # delete the default key
        ar_lt.key = None
        # force an exception in the compare_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            j = random.randint(0, 100)
            ar_lt.compare_elements(i, j)
        # test for the exception type
        assert excinfo.type == TypeError
        # test for the exception message
        assert "Undefined compare function" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = Arraylist(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # iterate over the test data
                for i in range(0, len(test_data) - 1):
                    # to avoid index out of range
                    if i > 1 and i < len(test_data) - 1:
                        # get current element, previous and next
                        ce = test_data[i]
                        pe = test_data[i - 1]
                        ne = test_data[i + 1]
                        # test the result with the default cmp function
                        exp_res = (-1, 0, 1)
                        res1 = ar_lt.compare_elements(ce, pe) in exp_res
                        res2 = ar_lt.compare_elements(ce, ce) in exp_res
                        res3 = ar_lt.compare_elements(ce, ne) in exp_res
                        # test all 3 conditions are true
                        assert all([res1, res2, res3])

    def test_find(self):
        """*test_find()* prueba la función *find()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba que el número entero del indice devuelto sea válido, es decir que esté entre -1 y el tamaño de la estructura de datos menos 1. -1 significa que el elemento no está presente en la estructura de datos y los indices van desde 0 a n-1.
        """
        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                test_len = len(test_data)
                ar_lt = Arraylist(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = Arraylist(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                t_data = test_data[i]
                # test if the element is present in the Arraylist
                idx = ar_lt.find(t_data)
                # test if the index is valid
                # FIXME check this tokenization assert
                assert -1 <= idx <= test_len - 1

    def test_update(self):
        """*test_update()* prueba la función *update()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si el elemento cambiado es igual al índice de *Arraylist* y la estructura de datos no se ha modificado mas allá de la longitud original.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the get_element method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            ar_lt.update(i, i)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = Arraylist(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                test_elm = test_data[i]
                # force an exception in the update method
                with pytest.raises(Exception) as excinfo:
                    i = random.randint(test_len * 2, test_len * 3)
                    ar_lt.update(test_elm, i)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i = random.randint(0, test_len - 1)
                # get the element in the test data
                t_data = test_data[i]
                # add the element in the index of the Arraylist
                ar_lt.update(t_data, i)
                # get the added element in the index of the Arraylist
                t_elem = ar_lt.get_element(i)
                # test if the removed element is equal to the index
                assert t_elem == t_data
                # test if the Arraylist size is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_exchange(self):
        """*test_exchange()* prueba la función *exchange()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías y fuera del rango de índice. También comprueba si los elementos intercambiados son iguales al índice original del *Arraylist* y que la estructura de datos no se ha modificado su longitud.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the exchange method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            ar_lt.exchange(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)

        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # get the length of the test data
                test_len = len(test_data)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = Arraylist(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)

                # force an exception in the exchange method
                with pytest.raises(Exception) as excinfo:
                    i, j = random.sample(range(test_len * 2, test_len * 3), 2)
                    ar_lt.exchange(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # test for the exception message
                assert "is out of range" in str(excinfo.value)

                # select a random valid index in the test data
                i, j = random.sample(range(0, test_len - 1), 2)
                # get the elements in the test data
                test_elm1 = test_data[i]
                test_elm2 = test_data[j]

                # exchange the elements in the index of the Arraylist
                ar_lt.exchange(i, j)
                # get the exchanged elements in the index of the Arraylist
                exch_elm1 = ar_lt.get_element(i)
                exch_elm2 = ar_lt.get_element(j)

                # test if the removed element is equal to the index
                assert exch_elm1 == test_elm2
                assert exch_elm2 == test_elm1
                # test if the Arraylist size is equal to test_len
                assert (ar_lt.size() == test_len)

    def test_sublist(self):
        """*test_sublist()* prueba la función *sublist()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *IndexError* para estructuras de datos vacías yfuera del rango de índice. También comprueba si los elementos de la sublista son iguales a los de la lista original.
        """
        # create a new empty Arraylist
        ar_lt = Arraylist()
        # force an exception in the sublist method
        with pytest.raises(Exception) as excinfo:
            i = random.randint(0, 100)
            i, j = random.sample(range(0, 100), 2)
            ar_lt.sublist(i, j)
        # test for the exception type
        assert excinfo.type == IndexError
        # test for the exception message
        assert "Empty data structure" in str(excinfo.value)
        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                ar_lt = Arraylist(iodata=test_data)
                # get the length of the test data
                test_len = len(test_data)
                assert ar_lt.size() == test_len
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = Arraylist(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                i = random.randint(test_len * -1, -1)
                j = random.randint(test_len + 1, test_len * 2)
                # # sample(range(test_len * 2, test_len * 3), 2)
                # # force an exception in the sublist method
                with pytest.raises(Exception) as excinfo:
                    ar_lt.sublist(i, j)
                # test for the exception type
                assert excinfo.type == IndexError
                # # test for the exception message
                assert "Invalid range: between" in str(excinfo.value)

                # select a random valid a low index in the test data
                # low = random.randint(0, test_len - 1)
                low = random.randint(0, (test_len - 1) // 2)
                # select a random valid a high index in the test data
                high = random.randint(low, test_len - 1)
                # get the elements in the test data
                sub_lt = list()
                i = low
                while i < high + 1:
                    sub_lt.append(test_data[i])
                    i += 1
                # get the elements size in the test data
                sub_lt_size = len(sub_lt)
                # create a sublist with the low and high index
                sub_ar_lt = ar_lt.sublist(low, high)
                # test for the sublist size is an Arraylist
                assert isinstance(sub_ar_lt, Arraylist)
                # test for the sublist size is equal to test_len
                assert sub_lt_size == sub_ar_lt.size()
                # test for the sublist elements are equal to sub_lt
                assert sub_lt == sub_ar_lt.elements

    def test_concat(self):
        """*test_concat()* prueba la función *concat()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *TypeError* para estructuras de datos no compatibles. También comprueba si los elementos de la lista resultante son iguales a la suma de los elementos de las listas originales.
        """
        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                ar_lt1 = Arraylist(iodata=test_data)
                # create a python list with the test data
                ar_lt2 = test_data.copy()

                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                err_msg = "Structure is not an Arraylist:"
                assert err_msg in str(excinfo.value)

                # create a new Arraylist with the wrong key
                ar_lt2 = Arraylist(iodata=test_data,
                                   key="testid")
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid key:" in str(excinfo.value)

                # create a new Arraylist with the wrong cmp function
                ar_lt2 = Arraylist(iodata=test_data,
                                   cmp_function=cmp_lt_test_function)
                # force an exception in the concat method
                with pytest.raises(Exception) as excinfo:
                    ar_lt1.concat(ar_lt2)
                # test for the exception type
                assert excinfo.type == TypeError
                # test for the exception message
                assert "Invalid compare function:" in str(excinfo.value)

                # create a new correct Arraylist with the test data
                ar_lt1 = Arraylist(iodata=test_data)
                ar_lt2 = Arraylist(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt1 = Arraylist(iodata=test_data,
                                       cmp_function=cmp_lt_test_function)
                    ar_lt2 = Arraylist(iodata=test_data,
                                       cmp_function=cmp_lt_test_function)
                # get the elements in the test data
                ar_lt1_data = ar_lt1.elements.copy()
                ar_lt2_data = ar_lt2.elements.copy()

                # create the new concatenated Arraylist
                ans = ar_lt1.concat(ar_lt2)
                ans_data = ans.elements.copy()

                assert isinstance(ans, Arraylist)
                assert ans.size() == len(ar_lt1_data) + len(ar_lt2_data)
                assert ans_data == ar_lt1_data + ar_lt2_data
                assert all((ans.key, ar_lt1.key, ar_lt2.key))
                assert all((ans.cmp_function,
                            ar_lt1.cmp_function,
                            ar_lt2.cmp_function))

    def test_clone(self):
        """
        *test_clone()* prueba la función *clone()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba si los elementos de la lista copiada son iguales a los de la lista original.
        """
        # TODO implement the test_copy() test!!!
        pass

    # def test_clone_lt(self):
    #     """*test_clone()* prueba como clonar un ADT *List* dinámico con diferentes estructuras de datos.
    #     """
    #     # FIXME, deprecated, use copy() method from the ADT
    #     # get the global parameters
    #     params = self.global_params
    #     data = self.global_data
    #     struct_dict = params.get("TEST_STRUCT_DICT")
    #     struct_key_lt = struct_dict.keys()
    #     data_type_lt = data.get("CHECK_TYPE_LT")
    #     test_data_lt = data.keys()

    #     # iterare over the test structures
    #     for tdsimp, tdstype in zip(struct_key_lt, LIST_DSTYPE_LT):
    #         # test_lt = List(dstruct=tdsimp)
    #         # iterate over the test data inside de structures
    #         for key, dtype in zip(test_data_lt, data_type_lt):
    #             if key not in IGNORE_KEYS_LT:
    #                 # get the test data
    #                 test_data = data.get(key)
    #                 # create the list
    #                 og_lt = List(dstruct=tdsimp,
    #                              iodata=test_data)
    #                 # test the list is not none
    #                 assert og_lt is not None
    #                 # test the list is the correct data structure
    #                 assert isinstance(og_lt, tdstype)
    #                 # test the list match the size of the test data
    #                 assert og_lt.size() == len(test_data)
    #                 # test the first element of the list
    #                 assert og_lt.get_first() == test_data[0]
    #                 # test the first element is the correct type
    #                 assert isinstance(og_lt.get_first(), dtype)

    #                 # clone the list
    #                 cl_lt = clone_lt(og_lt)
    #                 # test the clone list is not none
    #                 assert cl_lt is not None
    #                 # test the clone list is the correct data structure
    #                 assert isinstance(cl_lt, tdstype)
    #                 # test the clone list match the size of the test data
    #                 assert cl_lt.size() == len(test_data)
    #                 # test the clone list first element
    #                 assert cl_lt.get_first() == test_data[0]
    #                 # test the clone list first element is the correct type
    #                 assert isinstance(cl_lt.get_first(), dtype)

    #                 # test cmp_function
    #                 assert og_lt.cmp_function == cl_lt.cmp_function
    #                 # test key
    #                 assert og_lt.key == cl_lt.key

    #                 # iterate both lists
    #                 for og, cl in zip(og_lt, cl_lt):
    #                     # test the elements are the same
    #                     assert og == cl
    #                     # test the elements are the correct type
    #                     assert isinstance(og, dtype)
    #                     assert isinstance(cl, dtype)

    #     # iterate over the test data inside de structures
    #     for key in test_data_lt:
    #         if key not in IGNORE_KEYS_LT:
    #             # get the test data
    #             test_data = data.get(key)
    #             # create the list
    #             og_lt = list(test_data)
    #             # force an exception in the get_element method
    #             with pytest.raises(Exception) as excinfo:
    #                 clone_lt(og_lt)
    #             # test for the exception type
    #             assert excinfo.type == ValueError
    #             # test for the exception message
    #             src_type = type(og_lt).__name__
    #             err_msg = f"Unable to clone List, '{src_type}' type not found"
    #             assert err_msg in str(excinfo.value)

    def test_iterator(self):
        """*test_iterator()* prueba el iterador *__iter__()* de *Arraylist* en diferentes casos y tipos de datos. Comprueba las excepciones de *StopIteration* para estructuras de datos vacías. También comprueba si los elementos se pueden iterar en conjunto con los elementos de otras estructuras de datos nativas de Python y que los elementos iterados sean iguales a los de la lista original.
        """
        # iterates over global params and create filled Arraylist
        for key in self.global_params.keys():
            # ignore 3 keys from the global params
            if key not in IGNORE_KEYS_LT:
                # get the test data
                test_data = self.global_params.get(key)
                # create a new Arraylist with the test data
                test_len = len(test_data)
                ar_lt = Arraylist(iodata=test_data)
                # if it is the custom dict, use the custom cmp function
                if key == "TEST_CUSTOM_DICT_LT":
                    ar_lt = Arraylist(iodata=test_data,
                                      cmp_function=cmp_lt_test_function)
                # iterates over the Arraylist and the test data and compare
                for element, data in zip(ar_lt, test_data):
                    # test for the element is equal to test_data
                    assert element == data
                    # test for the element type is equal to test_data
                    assert type(element) is type(data)
                # test for the iterator is exhausted and the StopIteration
                assert ar_lt.size() == test_len
