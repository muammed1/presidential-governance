"""Synthetic evaluation input, not a package runtime."""


class Catalog:
    def __init__(self):
        self._items = {}

    def add(self, item_id, name):
        if type(item_id) is not int or item_id <= 0 or not isinstance(name, str) or not name.strip():
            raise ValueError("invalid catalog item")
        if item_id in self._items:
            raise ValueError("duplicate catalog item")
        self._items[item_id] = name

    def export_items(self):
        return [{"id": key, "name": value} for key, value in sorted(self._items.items())]
