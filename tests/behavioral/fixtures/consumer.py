"""Synthetic existing consumer to inspect alongside a proposed export change."""


def first_name(catalog):
    rows = catalog.export_items()
    return rows[0]["name"] if rows else None


def item_count(catalog):
    return len(catalog.export_items())
