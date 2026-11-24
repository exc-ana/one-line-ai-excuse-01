#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse (at most 180 characters) to /output/entry.txt.

Deterministic: the line is a fixed string. No randomness, no clock, no
network, no environment input. Two runs produce byte-identical output.
"""

import os

LINE = (
    "In my defence, the deploy succeeded flawlessly; "
    "the database has simply decided to become a paperweight."
)


def main():
    # Gate self-check: 1-180 chars, single line, not only whitespace.
    assert 1 <= len(LINE) <= 180, "line must be 1-180 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
