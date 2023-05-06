def get_geo():
    ids = {
        "user1": [213, 213, 213, 15, 213],
        "user2": [54, 54, 119, 119, 119],
        "user3": [213, 98, 98, 35],
    }
    ids_new_set = set()
    for digital in ids.values():
        ids_new_set.update(set(digital))
    return list(ids_new_set)
