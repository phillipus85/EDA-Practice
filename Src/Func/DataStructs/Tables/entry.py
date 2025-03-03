
def new_map_entry(key: object, value: object) -> dict:
    entry = dict(
        key=key,
        value=value
    )
    return entry


def set_key(entry: dict, key: object) -> dict:
    entry["key"] = key
    return entry


def set_value(entry: dict, value: object) -> dict:
    entry["value"] = value
    return entry


def get_key(entry: dict) -> object:
    return entry.get("key")


def get_value(entry: dict) -> object:
    return entry.get("value")
