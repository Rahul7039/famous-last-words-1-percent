#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's last words (one line, <= 199 characters) to
/output/entry.txt.
"""

import os

# The last words are assembled from their three beats so each part
# can be read (and timed) on its own.
BEATS = (
    "I held 1 percent for 40 minutes just to watch you panic.",
    "Worth it.",
    "Goodbye.",
)
LINE = " ".join(BEATS)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(text: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
