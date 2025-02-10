# import testing package
# import unittest
# import pytest

"""
Este módulo contiene datos de prueba para las pruebas unitarias para diferentes estructuras de datos en DISCLib.
"""


def get_nodelist_test_data():
    """*get_nodelist_test_data()* recupera un diccionario con los datos de prueba para la estructura *Node*.

    Returns:
        dict: diccionario con los datos de prueba para la estructura *Node*.
    """
    parameters = dict(
        # global variables for testing
        TEST_STR="Hello Node!",
        TEST_INT=42,
        TEST_FLOAT=42.0,
        TEST_BOOL=True,
        TEST_DICT={
            "key1": "Hello Node!",
            "key2": 42,
            "key3": 42.0,
            "key4": [
                "value1",
                "value2",
                "value3",
            ],
            "key5": {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
            },
            "key6": None,
            "key7": True,
        },
        TEST_LT=[
            "value1",
            "value2",
            "value3",
            42,
            42.7,
            "Hello Node!",
            None,
            True,
        ],
        CHECK_ERR_LT=[
            int(1234),
            list(),
            dict(id=1, name="John Doe"),
            float(42.87),
            bool(False),
            str("Hello Node!"),
        ],
        CHECK_TYPE_LT=[
            str,
            int,
            float,
            bool,
            dict,
            list
        ]
    )
    return parameters


def get_list_test_data():
    """*get_list_test_data()* recupera un diccionario con los datos de prueba para la clase *List*, esto incluye los datos de prueba para la estructura *ArrayList*, *SinglyLinked* y *DoubleLinked* y los ADTs *Stack* y *Queue*.

    Returns:
        dict: diccionario con los datos de prueba para la clase *List*.
    """
    parameters = dict(
        TEST_STR_LT=[
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
        ],
        TEST_INT_LT=[
            1,
            2,
            3,
            4,
            5,
            6,
            7,
        ],
        TEST_FLOAT_LT=[
            1.1,
            2.2,
            3.3,
            4.4,
            5.5,
            6.6,
            7.7,
        ],
        TEST_BOOL_LT=[
            True,
            False,
            True,
            False,
            True,
            False,
            True,
        ],
        TEST_DICT_LT=[
            {"a": 1, "id": 1},
            {"a": 2, "id": 2},
            {"a": 3, "id": 3},
            {"a": 4, "id": 4},
            {"a": 5, "id": 5},
            {"a": 6, "id": 6},
            {"a": 7, "id": 7},
        ],
        TEST_CUSTOM_DICT_LT=[
            {"a": 1, "uuid": "a1", "b": 1.1, "id": 1},
            {"a": 2, "uuid": "a2", "b": 2.2, "id": 2},
            {"a": 3, "uuid": "a3", "b": 3.3, "id": 3},
            {"a": 4, "uuid": "a4", "b": 4.4, "id": 4},
            {"a": 5, "uuid": "a5", "b": 5.5, "id": 5},
            {"a": 6, "uuid": "a6", "b": 6.6, "id": 6},
            {"a": 7, "uuid": "a7", "b": 7.7, "id": 7},
        ],
        TEST_LIST_LT=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
            [16, 17, 18],
            [19, 20, 21],
        ],
        TEST_TUPLE_LT=[
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15),
            (16, 17, 18),
            (19, 20, 21),
        ],
        TEST_SET_LT=[
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12},
            {13, 14, 15},
            {16, 17, 18},
            {19, 20, 21},
        ],
        CHECK_TYPE_LT=[
            str,
            int,
            float,
            bool,
            dict,
            dict,
            list,
            tuple,
            set,
        ],
        CHECK_ERR_LT=[
            set,
            tuple,
            list,
            dict,
            bool,
            float,
            int,
            str,
            dict,
        ],
    )
    return parameters


def get_mapentry_test_data():
    """*get_mapentry_test_data()* recupera un diccionario con los datos de prueba para la estructura de datos *MapEntry*.

    Returns:
        dict: diccionario con los datos de prueba para la estructura *MapEntry*.
    """
    parameters = dict(
        TEST_STR=dict(key="Entry",
                      value="Hello Entry!"),
        TEST_INT=dict(key=42,
                      value=42),
        TEST_FLOAT=dict(key=42.0,
                        value=42.0),
        TEST_BOOL=dict(key=True,
                       value=True),
        TEST_DICT=dict(key={"key1": "Hello Node!", },
                       value={
                           "key1": "Hello Node!",
                           "key2": 42,
                           "key3": 42.0,
                           "key4": [
                               "value1",
                               "value2",
                               "value3", ],
                           "key5": {
                               "key1": "value1",
                               "key2": "value2",
                               "key3": "value3", },
                           "key6": None,
                           "key7": True, }),
        TEST_LT=dict(key=list("value1",),
                     value=[
                         "value1",
                         "value2",
                         "value3",
                         42,
                         42.7,
                         "Hello Node!",
                         None,
                         True, ]),
        CHECK_ERR_LT=[
            int(1234),
            list(),
            dict(id=1, name="John Doe"),
            float(42.87),
            bool(False),
            str("Hello Node!"),
        ],
        CHECK_TYPE_LT=[
            str,
            int,
            float,
            bool,
            dict,
            list
        ]
    )
    return parameters


def get_hashtable_test_data():
    """*get_hashtable_test_data()* recupera un diccionario con los datos de prueba para las las estructuras *SeparateChaining* y *LinearProbing*.

    Returns:
        dict: diccionario con los datos de prueba para el ADT *Map*.
    """
    parameters = dict(
        TEST_STR_LT=[
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
        ],
        TEST_INT_LT=[
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
        ],
        TEST_FLOAT_LT=[
            1.1,
            2.2,
            3.3,
            4.4,
            5.5,
            6.6,
            7.7,
            8.8,
            9.9,
            10.10,
            11.11,
            12.12,
        ],
        TEST_BOOL_LT=[
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
        ],
        TEST_DICT_LT=[
            {"a": 1, "id": 1},
            {"a": 2, "id": 2},
            {"a": 3, "id": 3},
            {"a": 4, "id": 4},
            {"a": 5, "id": 5},
            {"a": 6, "id": 6},
            {"a": 7, "id": 7},
            {"a": 8, "id": 8},
            {"a": 9, "id": 9},
            {"a": 10, "id": 10},
            {"a": 11, "id": 11},
            {"a": 12, "id": 12},
        ],
        TEST_CUSTOM_DICT_LT=[
            {"a": 1, "uuid": "a1", "b": 1.1, "id": 1},
            {"a": 2, "uuid": "a2", "b": 2.2, "id": 2},
            {"a": 3, "uuid": "a3", "b": 3.3, "id": 3},
            {"a": 4, "uuid": "a4", "b": 4.4, "id": 4},
            {"a": 5, "uuid": "a5", "b": 5.5, "id": 5},
            {"a": 6, "uuid": "a6", "b": 6.6, "id": 6},
            {"a": 7, "uuid": "a7", "b": 7.7, "id": 7},
            {"a": 8, "uuid": "a8", "b": 8.8, "id": 8},
            {"a": 9, "uuid": "a9", "b": 9.9, "id": 9},
            {"a": 10, "uuid": "a10", "b": 10.10, "id": 10},
            {"a": 11, "uuid": "a11", "b": 11.11, "id": 11},
            {"a": 12, "uuid": "a12", "b": 12.12, "id": 12},
        ],
        TEST_LIST_LT=[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
            [16, 17, 18],
            [19, 20, 21],
            [22, 23, 24],
            [25, 26, 27],
            [28, 29, 30],
            [31, 32, 33],
            [34, 35, 36],
        ],
        TEST_TUPLE_LT=[
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
            (13, 14, 15),
            (16, 17, 18),
            (19, 20, 21),
            (22, 23, 24),
            (25, 26, 27),
            (28, 29, 30),
            (31, 32, 33),
            (34, 35, 36),
        ],
        TEST_SET_LT=[
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12},
            {13, 14, 15},
            {16, 17, 18},
            {19, 20, 21},
            {22, 23, 24},
            {25, 26, 27},
            {28, 29, 30},
            {31, 32, 33},
            {34, 35, 36},
        ],
        CHECK_KEY_TYPE_LT=[
            str,
            int,
            float,
            bool,
            int,
            str,
            list,
            tuple,
            set,
        ],
        CHECK_VALUE_TYPE_LT=[
            str,
            int,
            float,
            bool,
            dict,
            dict,
            list,
            tuple,
            set,
        ],
        CHECK_KEY_ERR_LT=[
            set,
            tuple,
            list,
            dict,
            bool,
            float,
            int,
            str,
            dict,
        ],
        CHECK_VALUE_ERR_LT=[
            set,
            tuple,
            list,
            dict,
            bool,
            float,
            int,
            str,
            dict,
        ],
        TEST_NENTRIES=6,
        TEST_SC_HT_CONFIG={
            "dynamic": {
                "alpha": 4.0,
                "_min_alpha": 0.0,
                "_max_alpha": 4.0,
                "rehashsble": True,
                "key": "uuid",
            },
            "static": {
                "alpha": 4.0,
                "_min_alpha": 0.0,
                "_max_alpha": 4.0,
                "rehashsble": False,
                "key": "uuid",
            },
        },
        TEST_LP_HT_CONFIG={
            "dynamic": {
                "alpha": 0.5,
                "_min_alpha": 0.0,
                "_max_alpha": 0.5,
                "rehashsble": True,
                "key": "uuid",
            },
            "static": {
                "alpha": 0.5,
                "_min_alpha": 0.0,
                "_max_alpha": 0.5,
                "rehashsble": False,
                "key": "uuid",
            },
        },
    )
    return parameters


def get_nodetree_test_data():
    """get_nodetree_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_searchtree_test_data():
    """get_searchtree_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_balancetree_test_data():
    """get_balancetree_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_gedgevertex_test_data():
    """get_gedgevertex_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_graph_test_data():
    """get_graph_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_lists_test_data():
    """get_lists_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict(
        TEST_ROOT_PGK_PATH="Src.DISClib.DataStructs",
        TEST_STRUCT_DICT={
            "ArrayList": "ArrayList",
            "SingleLinked": "singlelinkedlist",
            "DoubleLinked": "doublelinkedlist",
        },
        TEST_TGT_STRUCT_DICT={
            "DoubleLinked": "doublelinkedlist",
            "ArrayList": "ArrayList",
            "SingleLinked": "singlelinkedlist",
        },
        ERR_ROOT_PGK_PATH="Src.DISClib.ErrDataStructures",
        ERR_STRUCT_DICT={
            "FakeListA": "fakelista",
            "FakeListB": "fakelistb",
            "FakeListC": "fakelistc",
        },

    )
    return parameters


def get_pqs_test_data():
    """get_graphs_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_sortmaps_test_data():
    """get_sortmaps_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters


def get_graphs_test_data():
    """get_graphs_test_data _summary_

    Returns:
        _type_: _description_
    """
    parameters = dict()
    return parameters
