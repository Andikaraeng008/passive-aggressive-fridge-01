#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge - make.fun entry.

Writes one passive-aggressive note from a smart fridge to
output/entry.txt (gate: 1-200 UTF-8 characters, single line).
Standard library only; no dependencies.
"""

import os

# One concrete scene (the promised leftovers) + a twist in the final
# phrase (the food filed the report; the fridge is the witness).
NOTE = "The leftovers you promised to eat tomorrow have filed a missing-person report. I am their only witness."


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
