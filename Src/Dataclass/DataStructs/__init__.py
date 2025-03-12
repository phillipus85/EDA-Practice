# native python modules
# import modules for defining the list types
from typing import Union

# custom modules
# M1
from Src.Dataclass.DataStructs.Lists.arlt import Arraylist
from Src.Dataclass.DataStructs.Lists.sllt import Singlelinked
from Src.Dataclass.DataStructs.Lists.dllt import Doublelinked

# # M2
# from Src.Dataclass.DataStructs.Tables.scht import SeparateChaining
# from Src.Dataclass.DataStructs.Tables.lpht import LinearProbing

# union of available list types for sorting
# :arg: List: list type
List = Union[Arraylist, Singlelinked, Doublelinked]
