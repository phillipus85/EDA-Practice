# import python modules
import random as rd

# import modules for data structures index + bucket
from Src.Func.DataStructs.List import arlt     # as idx
from Src.Func.DataStructs.List import sllt     # as bucket

# import error handler
from Src.Func.Utils.error import error_handler as err

# import map entry
from Src.Func.DataStructs.Tables import entry as me

# import prime number generator
from Src.Func.Utils import numbers as num


def default_mp_entry_cmp(key: object, entry: dict) -> int:
    if (key == entry['key']):
        return 0
    elif (key > entry['key']):
        return 1
    return -1


def new_chaining_mp(n_elements: int = 17,
                    prime: int = 109345121,
                    load_factor: float = 4,
                    cmp_function=None) -> dict:
    try:
        capacity = num.next_prime(n_elements // load_factor)
        scale = rd.randint(1, prime - 1)
        shift = rd.randint(0, prime - 1)
        new_table = dict(
            n_elements=n_elements,
            prime=prime,
            limit_factor=load_factor,
            cur_factor=0,
            capacity=capacity,
            scale=scale,
            shift=shift,
            table=None,
            size=0,
            type="SEPARATE_CHAINING",
        )
        if cmp_function is None:
            new_table["cmp_function"] = default_mp_entry_cmp
        else:
            new_table["cmp_function"] = cmp_function
        new_table["table"] = arlt.new_array_lt(new_table["cmp_function"])
        i = 0
        while i < capacity:
            bucket = sllt.new_single_lt(new_table["cmp_function"])
            arlt.add_last(new_table["table"], bucket)
            i += 1
        return new_table
    except Exception as exp:
        err("chaining", "new_map()", exp)


def put(mp: dict, key: object, value: object) -> dict:
    try:
        _hash = num.hash_compress(key,
                                  mp["scale"],
                                  mp["shift"],
                                  mp["prime"],
                                  mp["capacity"])
        bucket = arlt.get_element(mp["table"], _hash)
        entry = me.new_map_entry(key, value)
        pos = sllt.is_present(bucket, key)
        if pos > -1:
            sllt.update(bucket, pos, entry)
        else:
            sllt.add_last(bucket, entry)
            mp["size"] += 1
            mp["cur_factor"] = mp["size"] / mp["capacity"]

        if mp["cur_factor"] >= mp["limit_factor"]:
            rehash(mp)
        return mp
    except Exception as exp:
        err("chaining", "put()", exp)







def contains(map, key):
    """ Retorna True si la llave key se encuentra en el map
        o False en caso contrario.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        True / False
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        bucket = lt.getElement(map['table'], hash)
        pos = lt.isPresent(bucket, key)
        if pos > 0:
            return True
        else:
            return False
    except Exception as exp:
        error.reraise(exp, 'Chain:contains')





def get(map, key):
    """ Retorna la pareja llave, valor, cuya llave sea igual a key
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        Una pareja <llave,valor>
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        bucket = lt.getElement(map['table'], hash)
        pos = lt.isPresent(bucket, key)
        if pos > 0:
            return lt.getElement(bucket, pos)
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'Chain:get')


def remove(map, key):
    """ Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: El map a donde se guarda la pareja
        key: la llave asociada a la pareja

    Returns:
        El map
    Raises:
        Exception
    """
    try:
        hash = hashValue(map, key)
        bucket = lt.getElement(map['table'], hash)
        if (bucket is not None):
            pos = lt.isPresent(bucket, key)
            if pos > 0:
                lt.deleteElement(bucket, pos)
                map['size'] -= 1
        return map
    except Exception as exp:
        error.reraise(exp, 'Chain:remove')


def size(map):
    """  Retorna  el número de entradas en la tabla de hash.
    Args:
        map: El map
    Returns:
        Tamaño del map
    Raises:
        Exception
    """
    return map['size']


def isEmpty(map):
    """ Informa si la tabla de hash se encuentra vacia
    Args:
        map: El map
    Returns:
        True: El map esta vacio
        False: El map no esta vacio
    Raises:
        Exception
    """
    try:
        bucket = lt.newList()
        empty = True
        for pos in range(lt.size(map['table'])):
            bucket = lt.getElement(map['table'], pos+1)
            if lt.isEmpty(bucket) is False:
                empty = False
                break
        return empty
    except Exception as exp:
        error.reraise(exp, 'Chain:isempty')


def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de llaves
    Raises:
        Exception
    """
    try:
        ltset = lt.newList('SINGLE_LINKED', map['cmpfunction'])
        for pos in range(lt.size(map['table'])):
            bucket = lt.getElement(map['table'], pos+1)
            if(not lt.isEmpty(bucket)):
                for element in range(lt.size(bucket)):
                    entry = lt.getElement(bucket, element+1)
                    lt.addLast(ltset, entry['key'])
        return ltset
    except Exception as exp:
        error.reraise(exp, 'Chain:keyset')


def valueSet(map):
    """
    Retorna una lista con todos los valores de la tabla de hash

    Args:
        map: El map
    Returns:
        lista de valores
    Raises:
        Exception
    """
    try:
        ltset = lt.newList('SINGLE_LINKED', map['cmpfunction'])
        for pos in range(lt.size(map['table'])):
            bucket = lt.getElement(map['table'], pos+1)
            if (not lt.isEmpty(bucket)):
                for element in range(lt.size(bucket)):
                    entry = lt.getElement(bucket, element+1)
                    lt.addLast(ltset, entry['value'])
        return ltset
    except Exception as exp:
        error.reraise(exp, 'Chain, valueset')


# __________________________________________________________________
#       Helper Functions
# __________________________________________________________________


def rehash(map):
    """
    Se aumenta la capacida de la tabla al doble y se hace
    rehash de todos los elementos de la tabla
    """
    try:
        newtable = lt.newList('ARRAY_LIST', map['cmpfunction'])
        capacity = nextPrime(map['capacity']*2)
        oldtable = map['table']
        for _ in range(capacity):
            bucket = lt.newList(datastructure='SINGLE_LINKED',
                                cmpfunction=map['cmpfunction'])
            lt.addLast(newtable, bucket)
        map['size'] = 0
        map['currentfactor'] = 0
        map['table'] = newtable
        map['capacity'] = capacity
        for pos in range(1, lt.size(oldtable)+1):
            bucket = lt.getElement(oldtable, pos)
            if (lt.size(bucket) > 0):
                for posbucket in range(1, lt.size(bucket)+1):
                    entry = lt.getElement(bucket, posbucket)
                    put(map, entry['key'], entry['value'])
        return map
    except Exception as exp:
        error.reraise(exp, "Chain:rehash")

