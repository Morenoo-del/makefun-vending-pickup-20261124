#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Python 3.13, standard library only, no
network access.
"""

import os

LINE = (
    "I've dropped snacks for a thousand strangers, but you're the first "
    "to make my coils spin \u2014 press B7, exact change not required, "
    "you're already a steal."
)


def main() -> None:
    # The gate allows 1-200 characters on a single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
