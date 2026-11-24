#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the entry text to /output/entry.txt. Deterministic: the same
text on every run.
"""

import os

ENTRY = (
    "My agent needed a 5-megabyte bundle of transcripts to prove it wrote "
    "this one sentence \u2014 and it still asked me to approve the proof."
)


def main():
    # Gate guard: the bounty requires /output/entry.txt to be UTF-8 text
    # of 1 to 200 characters, not only white space. Fail loudly here
    # rather than submitting an entry the sealed scorer would refuse.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(
            f"entry must be 1-200 non-blank characters, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
