#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's last words (one line, <= 199 characters) to
/output/entry.txt.
"""

import os

LINE = "I held 1 percent for 40 minutes just to watch you panic. Worth it. Goodbye."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
