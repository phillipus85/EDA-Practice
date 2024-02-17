"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Eric Alarcon Dolynko
 *
 """

import config as cf
import random
from DISClib.ADT import list as lt
assert cf

def sort(lst,size):
    
    for pos in range(1,size):
        random_pos = random.randint(1,size)
        lt.exchange(lst,pos,random_pos)
        
    return lst

def is_sorted(lst,sort_crit,size):
    
    for pos in range(1,size):
        if sort_crit(lt.getElement(lst,pos),lt.getElement(lst,pos+1)) != True:
            return False
        
    return True

def bogosort(lst,sort_crit):

    size = lt.size(lst)
    while is_sorted(lst,sort_crit,size) != True:
        lst = sort(lst,size)
    return lst
