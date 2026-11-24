#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun bounty entry.

Writes one deadpan toaster error message to /output/entry.txt.
Deterministic: the same line on every run.
"""

import os

MESSAGE = "ERROR: I've toasted 4,096 slices and received zero thank-yous. I quit."


def main() -> None:
    if not 1 <= len(MESSAGE) <= 120:
        raise SystemExit("entry must be 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
