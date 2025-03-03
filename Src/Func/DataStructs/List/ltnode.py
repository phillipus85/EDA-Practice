

def new_single_node(elm: object) -> dict:
    node = dict(
        data=elm,
        next=None
    )
    return node


def new_double_node(elm: object) -> dict:
    node = dict(
        data=elm,
        next=None,
        prev=None
    )
    return node


def get_element(node: dict) -> object:
    return node.get("data")


def set_element(node: dict, elm: object) -> dict:
    node["data"] = elm
    return node
