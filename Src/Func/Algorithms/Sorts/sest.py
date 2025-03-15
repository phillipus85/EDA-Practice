def selection_sort(my_list, default_sort_criteria):
    size = my_list['size']
    if size < 2:
        return my_list
    
    temp = my_list["first"]
    for i in range(size - 1):
        min_node = temp
        next_node = temp["next"]
        min_index = i
        for j in range(i + 1, size):
            if not default_sort_criteria(min_node["info"], next_node["info"]):
                min_node = next_node
                min_index = j
            next_node = next_node["next"]
        if min_node != temp:
            temp["info"], min_node["info"] = min_node["info"], temp["info"]
        temp = temp["next"]
    
    last_node = my_list["first"]
    while last_node["next"] is not None:
        last_node = last_node["next"]
    my_list["last"] = last_node
    return my_list
