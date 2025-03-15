def new_list():
    newlist= {
        'elements':[],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list 

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list 

def size(my_list):
    size = my_list["size"]
    return size 

def first_element(my_list):
    primero = my_list["elements"][0]
    return primero

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def last_element(my_list):
    ultimo = my_list["elements"][-1]
    return ultimo
    
def remove_first(my_list):
    my_list["size"] -= 1
    return my_list["elements"].pop(0)

def remove_last(my_list):
    my_list["size"] -= 1
    return my_list["elements"].pop()

def insert_element(my_list, index, element):
    my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, index):
    element= my_list["elements"].pop(index)
    my_list["size"] -= 1
    return my_list

def change_info(my_list, index, element):
    my_list["elements"][index] = element
    return my_list

def exchange(my_list, index1, index2):
    element_1 = my_list["elements"][index1]
    element_2 = my_list["elements"][index2]
    
    my_list["elements"][index1] = element_2
    my_list["elements"][index2] = element_1
    
    return my_list

def sub_list(my_list, index, num_elements):
    sublist = {
        "elements": my_list["elements"][index: index + num_elements],
        "size": num_elements,
    }
    return sublist
    
def shell_sort(my_list, cmp_function):
    size = my_list["size"]
    elements = my_list["elements"]
    gap = 1
    while gap < size // 3:
        gap = 3 * gap + 1
    while gap > 0:
        for i in range(gap, size):
            temp = elements[i]
            j = i
            while j >= gap and cmp_function(temp, elements[j - gap]):
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = temp
        gap //= 3
    return my_list