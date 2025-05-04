"""
Module to execute a depth-first search (DFS) in a graph represented as an adjacency list.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

from typing import Any
from Src.Func.DataStructs.Graphs import adjlt as g
from Src.Func.DataStructs.List import sllt as lt
from Src.Func.DataStructs.Tables import lpht as mp
from Src.Func.Utils.error import error_handler as err
import math
from Src.Func.DataStructs.List import stack as stk
from Src.Func.DataStructs.List import queue as q