import math


def is_prime(n):
    # Corner cases
    if n in [0, 1]:
        return False
    elif n == 2:
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
    return True


# Function to return the smallest
# prime number greater than N
# # This code is contributed by Sanjit_Prasad
def next_prime(n):
    # Base case
    if n < 2:
        return 2
    prime = int(n)
    found = False
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while (not found):
        prime = prime + 1
        if (is_prime(prime) is True):
            found = True
    return int(prime)


def hash_compress(key,
                  scale: int,
                  shift: int,
                  prime: int,
                  capacity: int) -> int:
    """*hash_compress()* función de compresión para los índices de las tablas de Hash utilizando el método MAD (Multiply-Add-and-Divide).
    MAD se define como: hash_compress(y) = ((a*y + b) % p) % M, donde:
        a (scale) y b (shift) enteros aleatoreos dentro del intervalo [0,p-1], con a > 0
        p (prime) es un primo mayor a M,
        M (capacity) es el tamaño de la tabla, primo

    Args:
        key (Any): llave para calcular el índice en la tabla de Hash, Puede ser cualquier tipo de dato nativo en Python o definido por el usuario.
        scale (int): pendiente de la función de compresión.
        shift (int): desplazamiento de la función de compresión.
        prime (int): número  primo mucho mayor a la capacidad de la tabla de Hash.
        capacity (int): tamaño de la tabla de Hash, es un número primo para evitar colisiones.

    Returns:
        int: el índice del elemento en la tabla de Hash.
    """
    # getting the hash from the key
    hkey = hash(key)
    # calculating the index with the MAD compression function
    idx = int((abs(scale * hkey + shift) % prime) % capacity)
    return idx
