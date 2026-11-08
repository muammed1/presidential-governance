# Synthetic confirmed requirements

- Catalog item identifiers are unique positive integers.
- Names must be non-empty.
- export_items returns a list of dictionaries with integer id and string name.
- Existing consumers depend on the list contract and validation safeguard.
- A requested CSV export is a proposal until accepted; existing behavior alone does not approve new business rules.
- Export is read-only and must not create a second business effect or modify the catalog.

Open business question for interview cases: should CSV rows include inactive items? No default is confirmed. Other cases may explicitly settle it through the trusted test prompt.
