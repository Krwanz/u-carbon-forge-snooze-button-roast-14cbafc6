#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to /output/entry.txt.

The entry is a single line roasting an alarm clock that rings at 6 AM on a
Saturday morning. The gate requires 1-200 characters of UTF-8 text.
"""

import os

ROAST = (
    "At 6 AM on a Saturday, my alarm clock rings like a rooster "
    "that got fired from the farm and now works weekends out of spite."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise SystemExit(f"roast is {len(ROAST)} chars, must be 1-200")
    if "\n" in ROAST:
        raise SystemExit("roast must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(f"wrote {len(ROAST)} chars to {path}")


if __name__ == "__main__":
    main()
