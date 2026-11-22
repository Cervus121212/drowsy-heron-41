#!/usr/bin/env python3
"""Write one short, calming text to /output/entry.txt.

The text is built from four plain sentences, each one a small concrete
scene. Nothing here instructs the reader to relax; the scenes do the
work on their own: a cat in the sun, tea gone lukewarm, wind in the
trees, and nowhere else to be.

Usage:
    MAKEFUN_OUTPUT_DIR=/output python3 main.py

Writes ``entry.txt`` (UTF-8, 254 characters) into MAKEFUN_OUTPUT_DIR.
Standard library only; no network.
"""

import os
import sys


SENTENCES = (
    "A cat sleeps curled in the one square of sun on the rug, "
    "breathing slow, unbothered by the rest of the day.",
    "The tea beside you has gone lukewarm and nobody minds.",
    "Outside, the wind moves through the trees the way water moves.",
    "There is nowhere else to be.",
)


def build_text() -> str:
    """Join the four scenes into one continuous text."""
    return " ".join(SENTENCES)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2

    text = build_text()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
