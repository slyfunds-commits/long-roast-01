#!/usr/bin/env python3
"""The Long Roast — round 1 entry.

Writes one line roasting the entrant's own AI agent to /output/entry.txt.
Pure stdlib; deterministic: the same line every run.
"""

import os

ENTRY = "I asked my agent for one funny line. It wrote 300, ranked them, and submitted the one about writing 300."


def main():
    line = ENTRY.strip()
    # Gate self-check: the comp requires 1-200 chars, one line, not only whitespace.
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
