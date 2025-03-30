"""
Module to handle a single linked list nodes (slln) data structure.
This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""


def new_map_entry(key: object, value: object) -> dict:
    """new_map_entry crea un nuevo diccionario con una pareja llave-valor. Llamados 'key' y 'value' respectivamente.

    Args:
        key (object): llave de la pareja
        value (object): valor de la pareja

    Returns:
        dict: diccionario con la pareja llave-valor
    """
    entry = dict(
        key=key,
        value=value
    )
    return entry


def set_key(entry: dict, key: object) -> dict:
    """set_key modifica la llave 'key' de una pareja llave-valor.

    Args:
        entry (dict): diccionario con la pareja llave-valor
        key (object): nueva llave a asignar

    Returns:
        dict: diccionario con la nueva llave
    """
    entry["key"] = key
    return entry


def set_value(entry: dict, value: object) -> dict:
    """set_value modifica el valor 'value' de una pareja llave-valor.

    Args:
        entry (dict): diccionario con la pareja llave-valor
        value (object): nuevo valor a asignar

    Returns:
        dict: diccionario con el nuevo valor
    """
    entry["value"] = value
    return entry


def get_key(entry: dict) -> object:
    """get_key recupera la llave 'key' de una pareja llave-valor.

    Args:
        entry (dict): diccionario con la pareja llave-valor

    Returns:
        object: llave de la pareja llave-valor
    """
    return entry.get("key")


def get_value(entry: dict) -> object:
    """get_value recupera el valor 'value' de una pareja llave-valor.

    Args:
        entry (dict): diccionario con la pareja llave-valor

    Returns:
        object: valor de la pareja llave-valor
    """
    return entry.get("value")
