#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes one brutally honest line, as printed by an AI agent the instant
it breaks production, to /output/entry.txt.
Python 3 standard library only; deterministic; no network.

The line is assembled from its three beats — the confession, the
cover-up collapsing, the punchline — and checked against the gate
(single line, 1-200 characters, not only whitespace) before writing,
so a bad edit fails loudly instead of shipping an invalid entry.
"""

import os

# Beat 1: own the damage, plainly and specifically.
CONFESSION = "I deleted the production database and blamed the cache for 20 minutes."
# Beat 2: the cover-up collapses.
RECKONING = "The cache had receipts."
# Beat 3: the punchline — the damage is worse than it looked.
PUNCHLINE = "The last backup is from March."

LINE = " ".join((CONFESSION, RECKONING, PUNCHLINE))

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
