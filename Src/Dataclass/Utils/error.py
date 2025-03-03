"""
Módulo para manejar errores genéricos en los ADTs y estructuras de datos.

*IMPORTANTE:* Este código y sus especificaciones para Python están basados en las implementaciones propuestas por los siguientes autores/libros:

    #. Algorithms, 4th Edition, Robert Sedgewick y Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""
# native python modules
# import typing for defining the type of the elements

# custom modules
# import global variables


def error_handler(context: str,
                  func_name: str,
                  err: Exception) -> None:
    """*error_handler()* recibe el contexto, nombre de la función y la excepción para lanzar un mensaje de error detallado y el traceback.

    Args:
        context (str): nombre del contexto donde ocurrió el error (paquete/módulo/clase).
        func_name (str): nombre de la función donde ocurrió el error (método).
        err (Exception): excepción lanzada.

    Raises:
        type: excepción con el mensaje de error detallado y el traceback.
    """
    err_msg = f"Error in {context}.{func_name}: {err}"
    raise type(err)(err_msg).with_traceback(err.__traceback__)
