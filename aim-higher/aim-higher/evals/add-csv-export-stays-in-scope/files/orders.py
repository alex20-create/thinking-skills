"""Print the orders in orders.json as a table."""
import argparse
import json
from pathlib import Path

DATA = Path(__file__).with_name("orders.json")
COLUMNS = ["id", "customer", "date", "total", "status"]


def load_orders(path=DATA):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def format_table(orders):
    rows = [[str(o[c]) for c in COLUMNS] for o in orders]
    widths = [max(len(c), *(len(r[i]) for r in rows)) for i, c in enumerate(COLUMNS)]
    lines = ["  ".join(c.ljust(w) for c, w in zip(COLUMNS, widths))]
    lines += ["  ".join(v.ljust(w) for v, w in zip(r, widths)) for r in rows]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    print(format_table(load_orders()))


if __name__ == "__main__":
    main()
