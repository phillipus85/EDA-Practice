def shell_sort(my_list, cmp_function):
    size = my_list["size"]
    if size < 2:
        return my_list
    gap = 1
    while gap < size // 3:
        gap = 3 * gap + 1
    nodes = []
    node = my_list["first"]
    while node is not None:
        nodes.append(node)
        node = node["next"]
    while gap > 0:
        for i in range(gap, size):
            temp = nodes[i]["info"]
            j = i
            
            while j >= gap and cmp_function(temp, nodes[j - gap]["info"]):
                nodes[j]["info"] = nodes[j - gap]["info"]
                j -= gap
            
            nodes[j]["info"] = temp
        gap //= 3
    return my_list
